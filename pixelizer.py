from models.classify import classify
from models.process import Process
import sys

if len(sys.argv) <= 1:
    print("No args provided: python3 pixelizer.py <your_url>")
    quit()
else:
    classifier = classify(str(sys.argv[1]))
    postprocess = Process(classifier)
    judge = (postprocess.judge())
    final = postprocess.sentiment(str(judge))
    print(final)

