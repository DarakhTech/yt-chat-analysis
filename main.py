from asyncore import write
import pytchat
from timeit import default_timer as timer
from random import randint

from emoji import emoji_scraper

import csv

from fast import FastTextSentiment

ft = FastTextSentiment('./model/sst5.ftz')

def update_session_stats(chunk):
    global total_chats
    global total_donation

    total_chats += len(chunk)
    # print(chunk)

    for c in chunk:
        print(c.message, ft.predict(emoji_scraper(c.message), False))
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

    # chat = pytchat.create(video_id="vRFrMnCOwlQ")
    chat = pytchat.create(video_id="rEGDNd-9PAU")
    # chat = pytchat.create(video_id="eOuqg7_5DZc")
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