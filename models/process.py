# Pixelizer - Image Classification with Vision Transformer (ViT)
# Author: Mac Lawson

from transformers import pipeline

class Process:
    def __init__(self, keywords):
        """
        Initializes an instance of the Process class.

        Args:
            keywords (str): The keywords used for judging.

        Returns:
            None
        """
        self.keywords = keywords

    def judge(self) -> str:
        """
        Uses a sentiment analysis model to judge the content based on the keywords.

        Returns:
            str: The sentiment judgment of the content.
        """
        sentiment_pipeline = pipeline(model="finiteautomata/bertweet-base-sentiment-analysis")

        return str(sentiment_pipeline("There is a post that contains a " + self.keywords))

    def sentiment(self, judgement: str):
        """
        Name: 

        Purpose:
        Translates the sentiment judgment into a human-readable format.

        Args:
            judgement (str): The sentiment judgment.

        Returns:
            str: The translated sentiment judgment.

        Notes:


        """
        if 'NEU' in judgement:
            return 'Content is safe'
        if 'POS' in judgement:
            return 'Content is safe'
        if 'NEG' in judgement:
            return 'Content is unsafe'