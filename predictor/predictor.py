import os
import sys
from typing import List
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../generator')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../data')))
from data import Metrics
import generate
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

input_dim = 1548  # Dimensions of your health metrics vector
embed_dim = 64  # Embedding dimensions
num_heads = 4   # Number of attention heads
hidden_dim = 128  # Hidden layer size in feedforward network
num_layers = 2  # Number of transformer layers
seq_length = 10  # Sequence length

class TransformerModel(nn.Module):
    def __init__(self):
        super(TransformerModel, self).__init__()
        self.embedding = nn.Linear(input_dim, embed_dim)
        self.positional_encoding = nn.Parameter(torch.zeros(1, seq_length, embed_dim))
        self.transformer = nn.Transformer(
            d_model=embed_dim,
            nhead=num_heads,
            num_encoder_layers=num_layers,
            dim_feedforward=hidden_dim,
            dropout=0.1,
            batch_first=True
        )
        self.fc_out = nn.Linear(embed_dim, input_dim)

    def forward(self, src):
        src = self.embedding(src) + self.positional_encoding[:, :src.size(1), :]
        output = self.transformer.encoder(src)
        return self.fc_out(output)


class HealthMetricsDataset(Dataset):
    def __init__(self, sequences, seq_length):
        self.sequences = sequences
        self.seq_length = seq_length

    def __len__(self):
        return len(self.sequences) - self.seq_length

    def __getitem__(self, idx):
        input_seq = self.sequences[idx:idx + self.seq_length]
        target_token = self.sequences[idx + self.seq_length]  # The next token after input_seq
        return torch.tensor(input_seq, dtype=torch.float32), torch.tensor(target_token, dtype=torch.float32)


def run():
    model = TransformerModel().to(device)
    loss_fn = nn.MSELoss()  # Predicting continuous values
    optimizer = optim.Adam(model.parameters(), lr=1e-3)


    print("training")
    data = training_data()

    dataset = HealthMetricsDataset(data, seq_length)
    dataloader = DataLoader(dataset, batch_size=32, shuffle=False)

    epochs = 8
    for epoch in range(epochs):
        model.train()
        total_loss = 0
        for src, tgt in dataloader:
            optimizer.zero_grad()
            output = model(src)  # Shape: (batch_size, seq_length, input_dim)
            loss = loss_fn(output[:, -1, :], tgt)  # Only compare the final prediction with the target
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
        print(f"Epoch {epoch+1}, Loss: {total_loss / len(dataloader)}")

    torch.save(model.state_dict(), 'health_transformer.pth')


    print("testing")
    data = testing_data()

    model.eval()
    with torch.no_grad():
        for src, tgt in dataloader:
            output = model(src)  # Shape: (batch_size, seq_length, input_dim)
            loss = loss_fn(output[:, -1, :], tgt)  # Only compare the final prediction with the target
            total_loss += loss.item()
        print(f"Test total loss: {total_loss / len(dataloader)}")

def training_data() -> List[List[float]]:
    print("generating training data")
    data_amount = 20000
    data = [generate.gen_initial()]
    for i in range(data_amount-1): # -1 because first day is from gen_initial
        if i % (data_amount//100) == 0:
            print("{}%".format(i // (data_amount//100)))
        data.append(generate.gen_from_history(data))

    print("data generated")
    data = [d.to_vector() for d in data]

    return data

def testing_data() -> List[List[float]]:
    print("generate testing data")
    data_amount = 100
    data = [generate.gen_initial()]
    for i in range(data_amount-1): # -1 because first day is from gen_initial
        if i % (data_amount//100) == 0:
            print("{}%".format(i // (data_amount//100)))
        data.append(generate.gen_from_history(data))

    Metrics.multi_to_jsonf("testing_data.json", data)

    print("data generated")
    data = [d.to_vector() for d in data]

    return data

if __name__ == "__main__":
    run()