lab = [[False, True, False, False, True],
       [False, False, False, False, False],
       [False, True, False, True, False],
       [True, True, False, False, False],
       [True, True, True, True, "Salida"]]

cam = [[1, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0]]

def dondevoy(x, y, a, b):

    if ((lab[x+1][y] == False) or (lab [x+1][y] == "Salida")) and (cam[x + 1][y] != 1) and ((x+1)<=4):
        a = x
        x = x+1

        cam[x][y] = 1

    elif ((lab[x][y+1] == False) or (lab [x][y+1] == "Salida")) and (cam[x][y + 1] != 1) and ((y+1)<=4):
        b = y
        y = y+1

        cam[x][y] = 1

    else:
        if (lab[x+1][y] == True) and (lab[x][y+1] == True):
            cam[x+1][y] = 1
            cam[x][y+1]= 1
            x = a
            y = b

    if (x<4) or (y<4):
        for i in cam:
            print(i)
        print ('\n')

        dondevoy(x, y, a, b)
    else:
        for i in cam:
            print(i)
        print ('\n')
        print('SALISTE')

a = 0
b = 0
x = 0
y = 0

dondevoy(x, y, a, b)
