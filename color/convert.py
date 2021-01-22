import numpy as np
import os


def RGB_to_intensity(RGB):
    I=0.298912 * RGB[0] + 0.586611 * RGB[1] + 0.114478 * RGB[2]
    return I

def RGB_to_colorcode(RGB):
    code='#'
    for c in RGB:
        if c < 16:
            code += str(0)
        code+=str(hex(int(c))).replace('0x','')
    return code

def HLS_to_RGB(H, L, S):
    if not L == 0 or not L == 1:
        if not S == 0:
            tmp = S * (1 - abs(2 * L - 1)) / 2
            Max = L + tmp
            Min = L - tmp
            while H >= 360:
                H -= 360
            if 0 <= H < 60:
                return [Max, Min + (Max - Min) * H / 60, Min]
            if 60 <= H < 120:
                return [Min + (Max - Min) * (120 - H) / 60, Max, Min]
            if 120 <= H < 180:
                return [Min, Max, Min + (Max - Min) * (H - 120) / 60]
            if 180 <= H < 240:
                return [Min, Min + (Max - Min) * (240 - H) / 60, Max]
            if 240 <= H < 300:
                return [Min + (Max - Min) * (H - 240) / 60, Min, Max]
            if 300 <= H < 360:
                return [Max, Min, Min + (Max - Min) * (360 - H) / 60]
        else:
            return [L, L, L]
    elif L == 0:
        return [0, 0, 0]
    elif L == 1:
        return [1, 1, 1]

def RGB_to_colorcode(RGB):
    code='#'
    for c in RGB:
        if c < 16:
            code += str(0)
        code+=str(hex(int(c))).replace('0x','')
    return code

def get_int(H):
    prm = int(H)
    prm = HLS_to_RGB(prm, 0.5, 1)
    return RGB_to_intensity(prm)

def get_colorcode(H):
    H = int(H)
    RGB = HLS_to_RGB(H, 0.5, 1)
    return RGB_to_colorcode([int(255*RGB[0]), int(255*RGB[1]), int(255*RGB[2])])

def xyY_to_XYZ(xyY):
    X = xyY[2] * xyY[0] / xyY[1]
    Y = xyY[2]
    Z = xyY[2] * ( 1 - xyY[0] - xyY[1] ) / xyY[1]
    return [X, Y, Z]

def XYZ_to_RGB(XYZ, wp='D65'):
    if wp=='c':
        R =  1.9099 * XYZ[0] - 0.5324 * XYZ[1] - 0.2882 * XYZ[2]
        G = -0.9846 * XYZ[0] + 1.9991 * XYZ[1] - 0.0283 * XYZ[2]
        B =  0.0583 * XYZ[0] - 0.1184 * XYZ[1] + 0.8979 * XYZ[2]
    else:
        R =  3.2410 * XYZ[0] - 1.5374 * XYZ[1] - 0.4986 * XYZ[2]
        G = -0.9692 * XYZ[0] + 1.8760 * XYZ[1] + 0.0416 * XYZ[2]
        B =  0.0556 * XYZ[0] - 0.2040 * XYZ[1] + 1.0507 * XYZ[2]

    return [R, G, B]

def get_coe():
    xR=3.38E-01
    xG=3.1E-01
    xB=1.789E-01
    yR=3.12E-01
    yG=6E-01
    yB=4.7E-02

    kXR = 0.4124
    kXG = 0.3576
    kXB = 0.1805

    kYR = 0.2126
    kYG = 0.7152
    kYB = 0.0722

    kZR = 0.0193
    kZG = 0.1192
    kZB = 0.9505

    k = np.matrix([[kXR,kXG,kXB],[kYR,kYG,kYB],[kZR,kZG,kZB]])

    l = np.matrix([[xR/yR, xG/yG, xB/yB], [1, 1, 1],[(1-xR-yR)/yR, (1-xG-yG)/yG, (1-xB-yB)/yB]])
    l = l**-1

    return [k,l]

def interplt(data,P):

    di=data[1][0] - data[0][0]
    if data[0][1] > P:
        Pi = [int(di * P / data[0][1])]
    else:
        for i in range(data.shape[0]-1, -1, -1):
            if data[i][1]<P:
                if i==data.shape[1]: Pi=data[data.shape[0]-1][0]
                Pi=[int(data[i][0]+di*(P-data[i][1])/(data[i+1][1]-data[i][1]))]
                break
    return Pi

def YRGB_to_RGB(YRGB):
    Rdata=np.loadtxt(os.path.dirname(__file__)+'/R.csv', delimiter=',')
    Gdata=np.loadtxt(os.path.dirname(__file__)+'/G.csv', delimiter=',')
    Bdata=np.loadtxt(os.path.dirname(__file__)+'/B.csv', delimiter=',')
    RGB=list()
    RGB.append(interplt(Rdata,YRGB[0]))
    RGB.append(interplt(Gdata,YRGB[1]))
    RGB.append(interplt(Bdata,YRGB[2]))

    print(RGB)

def get_fixRGB(rRGB):
    #rRGB is real RGB
    if rRGB[0]>1 or rRGB[1]>1 or rRGB[2]>1:
        rRGB[0]/=255
        rRGB[1]/=255
        rRGB[2]/=255

    coe=get_coe()
    k=coe[0]
    l=coe[1]
    rRGB=np.matrix([[rRGB[0]],[rRGB[1]],[rRGB[2]]])

    YRGB=np.dot(l, np.dot(k, rRGB))

    RGB=YRGB_to_RGB(YRGB)
    return RGB

YRGB_to_RGB([2.22e-2,0,0])
