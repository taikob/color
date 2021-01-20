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
