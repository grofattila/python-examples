height = 14

for i in range(0,height):
    for j in range (height,i,-1):
        print(" ", end='')
    for k in range (0,i*2-1):
        print("*", end='')
    print()
