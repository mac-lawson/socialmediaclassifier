# Pixelizer - Image Classification with Vision Transformer (ViT)
# Author: Mac Lawson

from transformers import ViTImageProcessor, ViTForImageClassification, pipeline
from PIL import Image
from requests import get
import warnings
import functools


def classify(url: str):
    """
    Classifies an image using the Vision Transformer (ViT) model based on the provided URL.

    Args:
        url (str): The URL of the image to classify.

    Returns:
        str: The predicted class label for the image.
    """
    try:
        # Open the image from the provided URL
        image = Image.open(get(url, stream=True).raw)

        # Load the ViT image processor and model
        processor = ViTImageProcessor.from_pretrained('google/vit-base-patch16-224')
        model = ViTForImageClassification.from_pretrained('google/vit-base-patch16-224')

        # Preprocess the image using the image processor
        inputs = processor(images=image, return_tensors="pt")

        # Forward pass through the ViT model
        outputs = model(**inputs)
        logits = outputs.logits

        # Predict the class label by selecting the class index with the highest probability
        predicted_class_idx = logits.argmax(-1).item()

        # Retrieve the predicted class label from the model's configuration
        predicted_class_label = model.config.id2label[predicted_class_idx]

        return predicted_class_label
    except:
        # Return an error message if an exception occurs during the classification process
        return ("Pixelizer encountered an error. We apologize for the inconvenience.\nPlease try again later.")
