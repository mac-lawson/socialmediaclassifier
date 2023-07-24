# Pixelizer - Image Classification with Vision Transformer (ViT)
# Author: Mac Lawson

from classify import classify
from process import Process
import warnings
import functools

class Pixelizer:
    def __init__(self, mode="production"):
        """
        Initializes an instance of the Pixelizer class.

        Args:
            mode (str): The mode to use for the Pixelizer instance. Valid values are:
                        - "production": Use for the production web app (default)
                        - "load": Download and reload models for use

        Returns:
            None
        """
        self.mode = mode


    def classify_image_only(self, imgurl: str):
        """
        Classifies an image using the classify function.

        Args:
            imgurl (str): The URL of the image to classify.

        Returns:
            The classification result.
        """
        return classify(imgurl)


    def classify_judge_image(self, imgurl: str):
        """
        Classifies and judges an image using the classify and Process classes.

        Args:
            imgurl (str): The URL of the image to classify and judge.

        Returns:
            The sentiment result based on the judged image.
        """
        processor = Process(classify(imgurl))
        judgement = processor.judge()
        print(judgement)
        return(processor.sentiment(str(judgement)))

