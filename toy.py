from random import random, uniform
import wandb
import numpy as np

with wandb.init(project="wandb-diffpatch-gamma") as run:
  for i in range(10000):
    wandb.log({
      "cool_metric":    np.random.uniform()*i,
      "amazing_metric": np.sin(i)*np.random.normal()*i,
      "extraordinary_metric": np.random.binomial(i, .5),
      "incredible_metric": np.random.poisson(1, i),
      "insane_metric": np.random.uniform()*i**2
    })