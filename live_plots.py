import matplotlib.pyplot as plt

class LivePlot():
    def __init__(self,height,width,row,col,title,subplotTitles) -> None:
        self.fig = plt.figure(title,figsize=(width,height))
        self.subplots = []
        for i in range(row*col):
            self.subplots.append(plt.subplot(row,col,i+1))
        
        for i in range(row*col):
            self.subplots[i].set_title(subplotTitles[i])

        self.queues = [[] for _ in range(row*col)]

    def updateSubplot(self,data,index):

        self.subplots[index].clear()
        self.queues[index].append(data)
        
        if len(self.queues[index])>20:
            self.queues[index].pop(0)
        
        self.subplots[index].plot(self.queues[index])
        plt.pause(0.01)
    
    