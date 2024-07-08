# YT Live Chat Sentiment Analysis

1. [x] Chat Extraction
2. Sending chunks of chat to server
3. Cleaning of data (emojis and empty spaces and irrelevant links and spam)
4. Analysis
5. Send back data to live 

## Dashboard Elements:

1. Positive / Negative -> Graph & Meter
2. Most repeated words
3. Indicate the streamer to interact with the user (questions in a chunk)
4. Views
5. Revenue
6. **subscribers gained while streaming
7. Elapsed Time



# Algorithm

for indicating the streamer to stop.
- Chat rate flow at the last chunk of data sent and question tags of last data.

=> Sentiment Analysis of YT chats : 
    - Sentiment Analyis
    - Sentiment -> binary classification 
                   * Stanford Sentiment Tree Bank
                   * fine grained (50%)
                          1. Rule based
                          2. Feature based
                          3. Embedded
                    Try all of them and see which one is best. (47%)
                        -> Optimise the best approach through small things:\
                                1. emoji consderation
                                2. ... ...

# Images
## Emoji Sentiment Map
<img width="500" alt="Screenshot 2024-07-09 at 3 43 03 AM" src="https://github.com/DarakhTech/yt-chat-analysis/assets/54445464/245163ec-7e5d-4d56-a085-7a111c256502">

## Reconfigured emoji Dataset into CSV format

<img width="378" alt="image" src="https://github.com/DarakhTech/yt-chat-analysis/assets/54445464/11b00bc3-cad5-4759-93d5-04a959b478cb">

## Labels for Categorizing
<img width="670" alt="Screenshot 2024-07-09 at 3 49 58 AM" src="https://github.com/DarakhTech/yt-chat-analysis/assets/54445464/70240d3e-3d07-4762-ab46-0bef5d063ab3">

                                
