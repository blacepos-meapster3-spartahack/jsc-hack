from typing import List
from data.data import Metrics
import generator.generate as generate
import matplotlib.pyplot as plt
import numpy as np


history: List[Metrics] = [generate.gen_initial()]
history.append(generate.gen_from_history(history))
history.append(generate.gen_from_history(history))
history.append(generate.gen_from_history(history))
history.append(generate.gen_from_history(history))
history.append(generate.gen_from_history(history))
history.append(generate.gen_from_history(history))
history.append(generate.gen_from_history(history))

Metrics.multi_to_jsonf(history)

# Create a figure
fig, axs = plt.subplots(4, 4, figsize=(16, 4))  # 1 row, 4 columns

# Plot in each subplot
for day in range(4):
    axs[0, day].plot(history[day].astronaut1.heartrate_bpm)
    axs[0, day].set_title(f"plot {day}, 0")
    axs[1, day].plot(history[day].astronaut2.heartrate_bpm)
    axs[1, day].set_title(f"plot {day}, 1")
    axs[2, day].plot(history[day].astronaut3.heartrate_bpm)
    axs[2, day].set_title(f"plot {day}, 2")
    axs[3, day].plot(history[day].astronaut4.heartrate_bpm)
    axs[3, day].set_title(f"plot {day}, 3")

# Adjust layout
plt.tight_layout()
plt.show()