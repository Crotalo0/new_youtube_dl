def sec_converter(s):
    h = s // 3600
    s -= 3600 * h
    m = s // 60
    s -= 60 * m
    return h, m, s
