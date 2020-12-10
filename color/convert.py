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

def get_int(tprm):
    prm = int(tprm)
    prm = HLS_to_RGB(prm, 0.5, 1)
    prm = RGB_to_intensity(prm)
    return prm