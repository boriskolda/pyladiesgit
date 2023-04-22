def vyhodnot(retezec):
    if "xxx" in retezec:
        return "x"
    if "ooo" in retezec:
        return "o"
    if "-" not in retezec:
        return "!"
    return "-"
    
print(vyhodnot("xoxoxoxoxoxoxox"))

pole = "x" * 19

print(pole)

def tah(pole, pozice, symbol):
    if pozice > 19 and pozice < 0:
        return ValueError
    else:
        nove = ""
        nove = pole[:pozice] + symbol + pole[pozice+1:] 
        return nove



print(tah(pole, -10, "o"))


# def tah_hrace(pole, symbol):