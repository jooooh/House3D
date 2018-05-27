import numpy as np

def noam_learning_rate_decay(init_lr, global_step, warmup_steps=2000):
  warmup_steps = float(warmup_steps)
  step = global_step + 1
  lr = init_lr * warmup_steps**0.5 * np.minimum(
      step * warmup_steps**-1.5, step**-0.5)

  return lr
