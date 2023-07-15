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
        sentiment_pipeline = pipeline(model="finiteautomata/bertweet-base-sentiment-analysis")
        return sentiment_pipeline("The post contains "+self.keywords)

    def sentiment(self, judgement: str):
        if 'NEU' in judgement:
            return 'safe'
        if 'POS' in judgement:
            return 'safe'
        if 'NEG' in judgement:
            return 'unsafe'

# x = Process("quilt, comforter, comfort, puff")
# x.judge()
