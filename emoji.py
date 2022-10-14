import re

def emoji_scraper(sentence):

    matchList = re.findall(r":(.*?):",sentence)
    try:
        for match in matchList:
            try:
                sentence = sentence.replace(":"+match+':','')
            except:
                pass
    except:
        pass
    return sentence
