import torch
from supervised import VisionModel, device, eval_transformer, num_stacked_images, stack_transformer
from model_car_env import ModelCar
from collections import deque
import numpy as np

model = torch.load('ctrl_model_130.pth', map_location="cuda:0")
model.to(device)
model.eval()

env = ModelCar()
obs = env.reset()

images = deque(maxlen=num_stacked_images)
for i in range(num_stacked_images-1): images.append(stack_transformer(obs))

while True:
    images.append(stack_transformer(obs))
    image = np.stack(images, axis=0)
    image = torch.Tensor(image).to(device)
    image = eval_transformer(image)

    steering = model(torch.unsqueeze(image, 0))

    obs, _, _, _ = env.step([steering, 1.0])
