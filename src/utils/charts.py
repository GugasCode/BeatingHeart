import matplotlib.pyplot as plot

def drawGraph(frame, amplitude):
    fig = plot.figure(figsize=(10,7))
    ax = plot.subplot2grid((40,40), (0,0), rowspan=40, colspan=40)
    ax.plot(frame, amplitude)
    plot.subplot_adjust(bottom=.23)
    plot.grid(True)
    plot.show()
