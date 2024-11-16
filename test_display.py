
import generate
import matplotlib.pyplot as plt
import numpy as np

metrics = generate.gen_initial()

plt.plot(np.array(metrics.astronaut1.heartrate_bpm))
plt.show()