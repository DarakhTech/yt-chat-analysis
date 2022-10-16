import re
from numpy import mat
import pandas as pd

score_dict = {}

'''running once in main file for making emoji scoring dictionary'''
def making_emoji_scores(): 

    df = pd.read_csv('data\dataset.csv')
    for ind in df.index:
        emoji_score = (df['Positive'][ind]-df['Negative'][ind])/(df['Negative'][ind]+df['Neutral'][ind]+df['Positive'][ind])
        score_dict[df['Unicode name'][ind].lower()] = round(emoji_score,3)

# print(score_dict)


'''returns a tuple of (sentence without emojis , average emoji  score) '''
def emoji_scraper(sentence):

    sentence = sentence.lower()
    matchList = re.findall(r":(.*?):",sentence)
    emoji_avg_score = []

    try:
        for match in matchList:
            try:
                # calculating avg score for all emojis
                if match in score_dict:
                    emoji_avg_score.append(score_dict[match])
                    # print(score_dict[match])
                
                sentence = sentence.replace(":"+match+':','')
            except:
                pass
    except:
        pass
    try:
        return (sentence,sum(emoji_avg_score)/(len(emoji_avg_score)))
    except:
        return (sentence,0)

making_emoji_scores()
print(emoji_scraper(input()))