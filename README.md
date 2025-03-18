# Anime Face Generator Streamlit App

This project demonstrates how to generate anime faces using a pre-trained generator model and its weights, without the need to clone the entire repository or use CUDA. I downloaded this generator model and their weight.pt from here. The app uses Streamlit to provide an easy-to-use interface for generating anime faces in real-time. You only need the generator code and the .pt weight file to run the app!

## Features

- No CUDA Required: Unlike most traditional models, this app does not require a GPU or CUDA support. It runs efficiently on any system with basic hardware.
  
- Lightweight: Only the generator and its weights are necessary to generate anime faces.
  
- Streamlit UI: A simple, interactive web app built with Streamlit, making it easy to use for generating anime faces.
  
- Easy Deployment: Deployed on Streamlit Cloud, making it accessible from anywhere with just a browser.
  
## How it Works

- Generator Code: The generator model code is used to generate anime faces. The pre-trained weights for the model are saved in .pt format.
  
- Streamlit App: The app takes user input (such as random noise or user-defined parameters) and feeds it to the generator to create a new anime face image.
  
- No Need to Clone Repo: You don’t need to clone the full GitHub repository. Simply download the generator code and the .pt weight file, and you can use the app without complex setup.
  
- No CUDA Support: The app runs entirely on the CPU, which eliminates the issues related to CUDA compatibility, ensuring it works on more systems.
  
## Deployment on Streamlit Cloud

The app is deployed and hosted on Streamlit Cloud. You can directly access the app via the provided link to generate anime faces.

## Setup & Installation

If you want to run the app locally, here’s how you can set it up:

### Steps to Run Locally

1. Clone the repository:

```
git clone https://github.com/hemantkumarlearning/Anime_Generator.git
cd Anime_Generator
```

2. Install the required dependencies:

```
pip install -r requirements.txt
```

3. Run the Streamlit app:
   
```
streamlit run app.py
```

## Usage

- Open the Streamlit app in your browser.
  
- Adjust the parameters or press the "Generate" button to create a new anime face image.
  
- You can save the generated image if you like!
## Demo

You can see a live demo of the app deployed on Streamlit Cloud here.
