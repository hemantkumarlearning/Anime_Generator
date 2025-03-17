import torch
from torchvision.utils import save_image
import torchvision.transforms as transforms
import streamlit as st
from model.model_loader import load_model


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = load_model().to(device)

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
    with torch.no_grad():
        image_tensor,_ = model(input,injection=4)
    pil_images = [tensor_to_pill(img) for img in image_tensor]
    cols = st.columns(5) 
    for i, img in enumerate(pil_images):
        col = cols[i % 5] 
        with col:
            st.image(img, use_container_width=True)
    

