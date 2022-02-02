import wandb
import numpy as np

with wandb.init(project="that_was_easy") as run:
  for i in range(10000):
    wandb.log({
      "cool_metric":    np.random.uniform()*i,
      "amazing_metric": np.sin(i)*np.random.normal()*i
    })