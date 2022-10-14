import pytchat
import time
import json

chat = pytchat.create(video_id="vRFrMnCOwlQ")
while chat.is_alive():
    for c in chat.get().sync_items():
        # print(c.amountValue)
        print(c.message)
    # time.sleep(1)