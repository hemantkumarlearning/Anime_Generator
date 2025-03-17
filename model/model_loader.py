import torch
from model.generator import Generator

def load_model(model_path='StyleGAN2_animeface_128pix.pt',device='cpu'):
    model = Generator(
        image_size=128, image_channels=3, style_dim=512,
        channels=32, max_channels=512, block_num_conv=2,
        map_num_layers=8, map_lr=0.01
    )
    model.load_state_dict(torch.load(model_path,map_location=device))
    model.to(device)
    model.eval()
    return model

