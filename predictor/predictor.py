import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../generator')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../data')))
import generate
import data
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

model = TransformerModel().to(device)
loss_fn = nn.MSELoss()  # Predicting continuous values
optimizer = optim.Adam(model.parameters(), lr=1e-3)

data = [generate.gen_initial()]
for i in range(9999):
    data.append(generate.gen_from_history(data))

print("data generated")
data = [d.to_vector() for d in data]

# Example data (replace with your actual dataset)
# data = torch.randn(1000, input_dim)  # 1000 days of health metrics
dataset = HealthMetricsDataset(data, seq_length)
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

print("training")

epochs = 10
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