import nltk
from setfit import SetFitModel

"""
This function does a sentiment based analysis on the text using a pre-trained model 
and finds the probalility of for the sentence to be negative/positive/neutral.
"""

def sentiment_analysis(text):
    model = SetFitModel.from_pretrained("StatsGary/setfit-ft-sentinent-eval")
    preds = model([text])
    res = "Neutral"
    if preds[0] == 1:
        res = "Positive"
    elif preds[0] == 0:
        res = "Negative"
    return res


def is_sentence(text: str) -> bool:
    
    # download nltk if its not install otherwise just execute
    if not nltk:
        nltk.download('punkt')
        
    # Tokenize the text into sentences.
    sentences = nltk.sent_tokenize(text)
    # Check if there is at least one sentence.
    if sentences:
        return True
    else:
        return False