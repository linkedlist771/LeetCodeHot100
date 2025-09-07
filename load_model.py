import torch

model_path = "10M.ckpt"

model_dic = torch.load(model_path, map_location="cpu")