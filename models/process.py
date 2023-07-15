from transformers import ViTImageProcessor, ViTForImageClassification, pipeline

green = '\033[92m'
end = '\033[0m'

class Process:
    def __init__(self, keywords):
        self.keywords = keywords

    def judge(self):
        unmasker = pipeline('fill-mask', model='distilbert-base-uncased')
        judgements = unmasker(self.keywords + " are a [MASK] thing .")
        index = 0
        final_judgement = ""
        for judgement in judgements:
            if index == 0:

                return float(judgement['score']), judgement['token_str']
            index +=1
