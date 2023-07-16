from requests import get
from numpy import asarray, median


dataset = get("https://pixelizerrlhf.vercel.app/getdata")

    


narray = asarray(dataset.text)

