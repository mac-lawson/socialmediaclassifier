from transformers import ViTImageProcessor, ViTForImageClassification, pipeline
from PIL import Image
from requests import get
from process import Process


def classify(url: str):
    try:
        # url = url
        image = Image.open(get(url, stream=True).raw)

        processor = ViTImageProcessor.from_pretrained('google/vit-base-patch16-224')
        model = ViTForImageClassification.from_pretrained('google/vit-base-patch16-224')
        inputs = processor(images=image, return_tensors="pt")
        outputs = model(**inputs)
        logits = outputs.logits
        # model predicts one of the 1000 ImageNet classes
        predicted_class_idx = logits.argmax(-1).item()

        return model.config.id2label[predicted_class_idx]
    except:
        return ("Pixelizer ran into an error, our group is sorry! \n\n Please try again later.")



