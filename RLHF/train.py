from transformers import ViTImageProcessor, ViTForImageClassification, pipeline
from PIL import Image
from requests import get

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
print(HEADER, "Welcome to the Trainer!\n", ENDC)
while True:
    url = 'https://picsum.photos/400/400'
    image = Image.open(get(url, stream=True).raw)

    processor = ViTImageProcessor.from_pretrained('google/vit-base-patch16-224')
    model = ViTForImageClassification.from_pretrained('google/vit-base-patch16-224')

    inputs = processor(images=image, return_tensors="pt")
    outputs = model(**inputs)
    logits = outputs.logits
    # model predicts one of the 1000 ImageNet classes
    predicted_class_idx = logits.argmax(-1).item()

    print(OKBLUE, "Please open this url:", url, ENDC, "\n")
    human_view = input('What do you see? ')
    print(OKGREEN, "What the model saw:", model.config.id2label[predicted_class_idx], "\n\nWhat you saw:", human_view)
