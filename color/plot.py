from matplotlib import pyplot as plt
import csv

def show_colormap(colorlist,sw):
    nh=len(colorlist) #num Hue
    fig = plt.figure()

    if sw==0:
        nl=len(colorlist[0]) #num Lightness
    elif sw==1:
        plt.subplots_adjust(wspace=0)
        nh=0

    i=1
    for cl in colorlist:
        if sw==0:
            for c in cl:
                plt.subplot(nh, nl, i, facecolor=c)
                plt.tick_params(labelbottom=False,
                               labelleft=False,
                               labelright=False,
                               labeltop=False,
                               bottom=False,
                               left=False,
                               right=False,
                               top=False)
                i+=1
        elif sw==1:
            plt.subplot(1, nl, i, facecolor=cl)
            plt.tick_params(labelbottom=False,
                           labelleft=False,
                           labelright=False,
                           labeltop=False,
                           bottom=False,
                           left=False,
                           right=False,
                           top=False)
            i+=1

    plt.show()