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