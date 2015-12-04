import multiprocessing as mp
import matplotlib.pyplot as plot

def drawGraph(data):
    """ Displays the chart """
    fig = plot.figure(figsize=(10,7))
    ax = plot.subplot2grid((40,40), (0,0), rowspan=40, colspan=40)
    ax.plot(data[0], data[1])
    plot.subplots_adjust(bottom=.23)
    plot.grid(True)
    plot.show()

def drawGraphJob(data):
    """ Starts another process where it runs the graph """
    chartJob = mp.Process(target=drawGraph, args=(data,))
    chartJob.start()
