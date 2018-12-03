def draw_x(size):
    """ 'x' karakerekből fomálódik ki maga a hatalmas X."""

    #----------------------
    # változók deklarálása
    #----------------------
    range_of_x = range(1,size)
    last = len(range_of_x) + 1 #Külön változóban pedig a range hosszát tettem be és növeltem meg eggyel.

    for i in range_of_x: # Ez a for ciklus felveszi az 1-40 range összes elemének értékét, ami ahhoz kell, hogy 40 soros legyen a képünk.
        for j in range_of_x: #Ez a for ciklus is felveszi az 1-40 range összes elemének értékét, de ez a sorokban mozog.
            if j == i or j == last - i: #"""Ha a sor száma megegyezik az oszlop számával vagy a sor hossza, mínusz az oszlop számával, akor a program tesz egy X-et.
                print("x", end="") #A x printelése után nem tesz entert a program.
            else:
                print(" ", end="") #Itt minden más esetben X helyett space-t íratok ki.
        print("") #A 'j' ciklus lefutása után jöhet az enter.

if __name__ == "__main__":
    draw_x(20)