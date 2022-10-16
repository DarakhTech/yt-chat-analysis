from asyncore import write
import pytchat
from timeit import default_timer as timer
import random 

from data_preprocess import remove_stop_words

from emoji import emoji_scraper

import csv
# from fast import FastTextSentiment

# ft = FastTextSentiment('./model/sst5.ftz')

from live_plots import LivePlot

#instance for live plot
disp = LivePlot(5,10,1,2,'YT live',["sentiment","timepass"],)


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

    summ = 0

    for c in chunk:

        # c -> sentence
        emoji_val = emoji_scraper(c.message)
        emoji_val[0] = remove_stop_words(emoji_val[0])
        print(emoji_val[0])
        # summ += rankToScoreMapping[ft.predict(emoji_val[0], False)] + emoji_val[1]*0.3
        summ += random.random() + emoji_val[1]*0.3
        print(c.message, emoji_val[1] )
        total_donation += float(c.amountValue)

    print(summ/len(chunk))

    disp.updateSubplot(summ/len(chunk),0)

    writeToFile(summ/len(chunk))

header = ['time','rating']
# datafile = open('./data.csv', 'w')

def writeToFile(n):
    datafile = open('./data.csv', 'a')
    writer = csv.writer(datafile)
    writer.writerow([timer() - time_elapsed , n])
    datafile.close()


with open('./data.csv', 'w') as datafile:
    writer = csv.writer(datafile)
    writer.writerow(header)
    # datafile.close()

    # chat = pytchat.create(video_id="vRFrMnCOwlQ") # binks
    # chat = pytchat.create(video_id="rEGDNd-9PAU") # errichto
    chat = pytchat.create(video_id="wzN4eqja8u8") # DanTDM
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
                disp.updateSubplot(total_chats,1)
                # print(chunks)
                update_session_stats(chunks)
                # writeToFile()
                chunk_start = timer()
                chunks = []
                chunks.append(c)
            # print(c.message)
            else:
                chunks.append(c)
            print(f"> Time: {round(timer() - time_elapsed, 4)}\t| Donation : {total_donation}\t| Chats : {total_chats}")
