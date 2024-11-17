import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../data')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'predictor')))
from data import Metrics
from predictor import HealthMetricsDataset, TransformerModel, testing_data
from typing import List
import matplotlib.pyplot as plt
import torch
from torch.utils.data import DataLoader

model = TransformerModel()
model.load_state_dict(torch.load('health_transformer_sav2.pth'))

model.eval()

test_data = testing_data()

dataset = HealthMetricsDataset(test_data, 10)
dataloader = DataLoader(dataset, batch_size=32, shuffle=False)

predictions = []

with torch.no_grad():
    for src, tgt in dataloader:
        pred_tgt = model(src)

        for i in range(32):
            try:
                predictions.append(pred_tgt[i,-1,:])
            except IndexError:
                # we're at the end of our data, our batch is less than 32
                break

        # fig, axs = plt.subplots(2, 1, figsize=(16, 8))
        # axs[0].plot(tgt[8,:360])
        # axs[0].set_title(f"actual")
        # axs[1].plot(pred_tgt[8,-1,:360])
        # axs[1].set_title(f"predicted")
        # # Adjust layout
        # plt.tight_layout()
        # plt.show()
        # input("press enter to continue...")

print(len(predictions))
print(predictions[3].shape)

pred_structs = [Metrics.from_vector(p.tolist()) for p in predictions]

Metrics.multi_to_jsonf("predictions.json", pred_structs)
