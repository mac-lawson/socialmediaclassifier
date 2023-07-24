![logo](https://trello.com/1/cards/64b1933d3ff2014a00a6c681/attachments/64b1c53a01a31ec7db40f171/download/level.png)
# Pixelizer
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)

Project for [Coding@Tufts](https://universitycollege.tufts.edu/high-school/programs/coding-academy)

Pixelizer is a combination of two machine learning pipelines designed to identify dangerous and/or inappropriate text/image posts on social media.
#### Models Used
Pixelizer uses Hugging Face transformers and pipelines. 
* For the vision transformer (ViT), we use [vit-base-patch16-224](https://huggingface.co/google/vit-base-patch16-224) by Google. 
* For the sentiment analysis model, we use [bertweet-base-sentiment-analysis](https://huggingface.co/finiteautomata/bertweet-base-sentiment-analysis?text=terror) by finiteautomata. 

## Assist the platform
### Provide training data
**You** can help improve your model by providing training data through our [RHLF platform](https://pixelizerrlhf.vercel.app/)
## Installation
```bash
git clone https://github.com/mac-lawson/socialmediaclassifier
```
```bash
pip install -r requirements.txt
```
## Information and Limitations
- Currently, only .jpg image files are accepted

## Options to run
### 1. Integrate into your own app (better if you want to use for production)
Copy the `models` directory in your project folder

Import our modules
```python
from models.classify import classify
from models.process import Process
```
Classify an image URL
```python
    classifier = classify("https://loremflickr.com/400/400/dog")
    print(classifier)
    postprocess = Process(classifier)
    judge = (postprocess.judge())
    final = postprocess.sentiment(str(judge))
```
### 2. Run `pixelizer.py` (better if you are trying the platform out)
**Ensure that you have installed requirements.txt**
```bash
python3 pixelizer.py <image url>
```

### 3. Run web server
**Ensure that you have installed requirements.txt**
```bash
python3 app.py
```

### 4. Colab notebook
[Google Colab](https://colab.research.google.com/drive/1U1pC4Pniv_Xr6ycC-ObIPrAsec4L0Yk-?usp=sharing)
### List of testing images:
If you want to do some testing on the platform, here are some image you can try and run:
- https://static01.nyt.com/images/2021/09/14/science/07CAT-STRIPES/07CAT-STRIPES-mediumSquareAt3X-v2.jpg
- https://www.dice.com/binaries/medium/content/gallery/dice/insights/2020/03/shutterstock_1375882658-e1583354582236.jpg
- https://www.piercemfg.com/hubfs/electric-fire-truck/electric-fire-truck-reference-guide-Banner.jpg
- https://raisingchildren.net.au/__data/assets/image/0024/47742/baby-behaviour-and-awareness.jpg

### New features that would be nice to add:
#### Front end:
- #1 [Migrate the front end to React](https://towardsdatascience.com/build-deploy-a-react-flask-app-47a89a5d17d9)
- #2 Improve the web demo to display the image and other images similar too it
#### Back end:
- #1 Upgrade the image classification module
- #2 Add in a module that only uses the Hugging Face API to be able to run server publicly
- #3 Be able to upload an image along with the URL downstream.
- #4 Improve the URL downstream, long URLs and PNGs/.webp files tend to cause issues
- #5 Add caching for RLHF
- #6 javascript backend that does the same as what the Pixelizer python class does. Just port pixelizer.py over to JS
#### Graphics
- #1 Create some cool graphics for a new home page [like this](https://dribbble.com/shots/11300497-Introducing-Storytale-Platform)

**If you want to begin adding some features, put your name here to avoid multiple people working on the same issue!**

Back end #1 - Mac

Back end #2 - Mac

I can start looking at front end 1/2 when I'm free, but no promises. - Sebastian


