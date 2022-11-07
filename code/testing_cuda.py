import torch
print("Is CUDA supported by this system?") 
print(torch.cuda.is_available())
print("CUDA version:", torch.version.cuda)