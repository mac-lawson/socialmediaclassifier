# Pixelizer
Project for Coding@Tufts

Goal is to identify dangerous and/or inappropriate text/image posts on social media through a machine learning algorithm.

## Installation
```
pip install -r requirements.txt
```

## Options to run
### Integrate into your own app
Copy the `models` directory in your project folder

Import our modules
```python
from models.classify import classify
from models.process import Process
```
Classify an image URL
``` python
    classifier = classify("https://loremflickr.com/400/400/dog")
    print(classifier)
    postprocess = Process(classifier)
    judge = (postprocess.judge())
    final = postprocess.sentiment(str(judge))
```



