#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    if roman_string == "":
        return 0
    num = 0
    dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for m, n in zip(roman_string, roman_string[1:]):
        if m not in dic.keys():
            return o
        elif dic[m] >= dic[n]:
            num += dic[m]
        else:
            num -= dic[m]
    num += dic[roman_string[-1]]
    return num
