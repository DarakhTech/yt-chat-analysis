from asyncore import write
import pytchat
from timeit import default_timer as timer
from random import randint

from data_preprocess import remove_stop_words

from emoji import emoji_scraper

import csv

from fast import FastTextSentiment

ft = FastTextSentiment('./model/sst5.ftz')

rankToScoreMapping = {
    5 : 1,
    4 : 0.5,
    3 : 0,
    2 : -0.5,
    1 : -1
}

def update_session_stats(chunk):
    global total_chats
    global total_donation

    total_chats += len(chunk)
    # print(chunk)

    for c in chunk:

        # c -> sentence
        emoji_val = emoji_scraper(c.message)
        emoji_val[0] = remove_stop_words(emoji_val[0])
        print(emoji_val[0])
        print(c.message, rankToScoreMapping[ft.predict(emoji_val[0], False)], emoji_val[1] )
        total_donation += float(c.amountValue)


header = ['time','rating']
# datafile = open('./data.csv', 'w')

def writeToFile():
    datafile = open('./data.csv', 'a')
    writer = csv.writer(datafile)
    writer.writerow([timer() - time_elapsed , randint(-1,1)])
    datafile.close()


with open('./data.csv', 'w') as datafile:
    writer = csv.writer(datafile)
    writer.writerow(header)
    # datafile.close()

    # chat = pytchat.create(video_id="vRFrMnCOwlQ") # binks
    # chat = pytchat.create(video_id="rEGDNd-9PAU") # errichto
    chat = pytchat.create(video_id="wzN4eqja8u8")
    chunks = []
    chunk_start = timer() 

    total_donation = 0
    time_elapsed = timer()
    total_chats = 0

    while chat.is_alive():
        for c in chat.get().sync_items():
            # print(c.amountValue)
            cur_time = timer()
            if cur_time - chunk_start > 10:
                # print(chunks)
                update_session_stats(chunks)
                writeToFile()
                chunk_start = timer()
                chunks = []
                chunks.append(c)
            # print(c.message)
            else:
                chunks.append(c)
            print(f"> Time: {round(timer() - time_elapsed, 4)}\t| Donation : {total_donation}\t| Chats : {total_chats}")