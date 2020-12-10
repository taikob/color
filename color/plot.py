from matplotlib import pyplot as plt
import convert as c
import cv2
import numpy as np

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

def make_image(H,L=None,S=None):
    if L is None or S is None:
        L=0.5
        S=1
        title='H'+str(int(H))+'.jpg'
    else:
        title='H'+str(int(H))+'_L'+str(int(L))+'_S'+str(int(S))+'.jpg'

    imsize=[120,160]
    RGB=c.HLS_to_RGB(H, L, S)

    im=np.ndarray([imsize[0],imsize[1],3])

    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            im[i,j,:]=np.array([RGB[2],RGB[1],RGB[0]])*255

    cv2.imwrite(title, im)