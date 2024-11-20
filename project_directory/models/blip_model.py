from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

def generate_caption(image_path):
    # Load the image as a PIL.Image
    image = Image.open(image_path).convert("RGB")
    
    # Initialize processor and model
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    
    # Process the image and generate caption
    inputs = processor(images=image, return_tensors="pt").to(torch.device('cpu'))
    outputs = model.generate(**inputs)
    caption = processor.decode(outputs[0], skip_special_tokens=True)
    
    return caption
