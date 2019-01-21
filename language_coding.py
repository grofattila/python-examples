

def kodolo(szoveg):
    maganhangzok = "aáeéiíoóöőuúüű"

    eredmeny = ""

    for betu in szoveg:
        if betu in maganhangzok:
            eredmeny += betu + "v" + betu
        else:
            eredmeny += betu
    return eredmeny

print(kodolo("Mindjárt itt van karácsony!!!"))
