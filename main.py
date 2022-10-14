from asyncore import write
import pytchat
from timeit import default_timer as timer
from random import randint

from emoji import emoji_scraper

import csv

def update_session_stats(chunk):
    global total_chats
    global total_donation

    total_chats += len(chunk)

    for c in chunk:
        print(emoji_scraper(c.message))
        total_donation += float(c.amountValue)


header = ['time','rating']
# datafile = open('./data.csv', 'w')

with open('./data.csv', 'w') as datafile:
    writer = csv.writer(datafile)
    writer.writerow(header)
    # datafile.close()

    chat = pytchat.create(video_id="vRFrMnCOwlQ")
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
                writer.writerow([timer() - time_elapsed , randint(-1,1)])
                chunk_start = timer()
                chunks = []
                chunks.append(c)
            # print(c.message)
            else:
                chunks.append(c)
            print(f"> Time: {round(timer() - time_elapsed, 4)}\t| Donation : {total_donation}\t| Chats : {total_chats}")