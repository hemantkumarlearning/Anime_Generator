import torch
import numpy as np
import os
from torchvision.utils import save_image
import torchvision.transforms as transforms
import streamlit as st
from model.model_loader import load_model
from PIL import Image

device = 'cpu'
model = load_model()

st.title('Anime Face Generator')

def sampler(num_image):
    return torch.randn(num_image, 512)

def tensor_to_pill(tensor):
    tensor = tensor.detach().cpu().squeeze(0)
    tensor = (tensor - tensor.min()) / (tensor.max() - tensor.min())
    image = transforms.ToPILImage()(tensor)
    return image

button  = st.button('Generate Images')
if button:
    num_images = 15
    input = (sampler(num_images), sampler(num_images))
    image_tensor,_ = model(input,injection=4)
    # save_path = os.path.join('generated_images', 'generated_image.png')
    # save_image(image_tensor, save_path, normalize=True,nrow=5)
    # st.image('generated_images/generated_image.png')
    pil_images = [tensor_to_pill(img) for img in image_tensor]
    cols = st.columns(5)  # 5 images per row
    for i, img in enumerate(pil_images):
        col = cols[i % 5]  # Select the appropriate column for the image
        with col:
            st.image(img, use_container_width=True)
    

