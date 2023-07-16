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

    def judge(self):
        """
        Uses a sentiment analysis model to judge the content based on the keywords.

        Returns:
            str: The sentiment judgment of the content.
        """
        sentiment_pipeline = pipeline(model="finiteautomata/bertweet-base-sentiment-analysis")
        return sentiment_pipeline("The post contains " + self.keywords)

    def sentiment(self, judgement: str):
        """
        Translates the sentiment judgment into a human-readable format.

        Args:
            judgement (str): The sentiment judgment.

        Returns:
            str: The translated sentiment judgment.
        """
        if 'NEU' in judgement:
            return 'Content is safe, but might need to be age filtered.'
        if 'POS' in judgement:
            return 'Content is safe'
        if 'NEG' in judgement:
            return 'Content is unsafe'
