import math

def normalizar(vector):
    norma = math.sqrt(vector[0]**2 + vector[1]**2 + vector[2]**2)
    return norma

def determinante2(*args):
    return args[0][0] * args[1][1] - args[0][1] * args[1][0]

def determinante3(*args):
    return args[0][0] * determinante2(args[1][1:3], args[2][1:3]) - args[0][1] * determinante2(args[1], args[2]) + args[0][2] * determinante2(args[1][0:2], args[2][0:2])

def determinante4(*args):
    return args[0][0] * determinante3(args[1][1:3], args[2][1:3], args[3][1:3]) - args[0][1] * determinante3(args[1], args[2], args[3]) + args[0][2] * determinante3(args[1][0:2], args[2][0:2], args[3][0:2]) - args[0][3] * determinante3(args[1][0:2], args[2][0:2], args[3][1:3])

def matriz_inversa(matriz):
    if len(matriz) == 2:
        return [[determinante2(matriz[1], matriz[0]) / determinante2(matriz[0]), -determinante2(matriz[1], matriz[0]) / determinante2(matriz[0])],
                [-determinante2(matriz[1], matriz[0]) / determinante2(matriz[0]), determinante2(matriz[1], matriz[0]) / determinante2(matriz[0])]]
    elif len(matriz) == 3:
        return [[determinante3(matriz[1], matriz[2], matriz[0]) / determinante3(matriz[0]), -determinante3(matriz[1], matriz[2], matriz[0]) / determinante3(matriz[0]), determinante3(matriz[1], matriz[2], matriz[0]) / determinante3(matriz[0])],
                [-determinante3(matriz[1], matriz[2], matriz[0]) / determinante3(matriz[0]), determinante3(matriz[1], matriz[2], matriz[0]) / determinante3(matriz[0]), -determinante3(matriz[1], matriz[2], matriz[0]) / determinante3(matriz[0])],
                [determinante3(matriz[1], matriz[2], matriz[0]) / determinante3(matriz[0]), -determinante3(matriz[1], matriz[2], matriz[0]) / determinante3(matriz[0]), -determinante3(matriz[1], matriz[2], matriz[0]) / determinante3(matriz[0])]]
    elif len(matriz) == 4:
        return [[determinante4(matriz[1], matriz[2], matriz[3], matriz[0]) / determinante4(matriz[0]), -determinante4(matriz[1], matriz[2], matriz[3], matriz[0]) / determinante4(matriz[0]), determinante4(matriz[1], matriz[2], matriz[3], matriz[0]) / determinante4(matriz[0]), -determinante4(matriz[1], matriz[2], matriz[3], matriz[0]) / determinante4(matriz[0])],
                [-determinante4(matriz[1], matriz[2], matriz[3], matriz[0]) / determinante4(matriz[0]), determinante4(matriz[1], matriz[2], matriz[3], matriz[0]) / determinante4(matriz[0]), -determinante4(matriz[1], matriz[2], matriz[3], matriz[0]) / determinante4(matriz[0]), determinante4(matriz[1], matriz[2], matriz[3], matriz[0]) / determinante4(matriz[0])],
                [determinante4(matriz[1], matriz[2], matriz[3], matriz[0]) / determinante4(matriz[0]), -determinante4(matriz[1], matriz[2], matriz[3], matriz[0]) / determinante4(matriz[0]), -determinante4(matriz[1], matriz[2], matriz[3], matriz[0]) / determinante4(matriz[0]), determinante4(matriz[1], matriz[2], matriz[3], matriz[0]) / determinante4(matriz[0])],
                [-determinante4(matriz[1], matriz[2], matriz[3], matriz[0]) / determinante4(matriz[0]), determinante4(matriz[1], matriz[2], matriz[3], matriz[0]) / determinante4(matriz[0]), determinante4(matriz[1], matriz[2], matriz[3], matriz[0]) / determinante4(matriz[0]), -determinante4(matriz[1], matriz[2], matriz[3], matriz[0]) / determinante4(matriz[0])]]
    else:
        return "Error"

def producto_cruz(v1, v2): 
    l1 = len(v1)
    l2 = len(v2)
    if l1 == l2:
        if l1 == 3:
            return [v1[1]*v2[2] - v1[2]*v2[1], 
                    v1[2]*v2[0] - v1[0]*v2[2], 
                    v1[0]*v2[1] - v1[1]*v2[0]]
        elif l1 == 2:
            return [v1[1]*v2[0] - v1[0]*v2[1]]
        else:
            return "Error"

def producto_punto(v1, v2):
    l1 = len(v1)
    l2 = len(v2)
    if l1 == l2:
        if l1 == 3:
            return v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]
        elif l1 == 2:
            return v1[0]*v2[0] + v1[1]*v2[1]
        else:
            return "Error"

def producto_matriz_vector(matriz, vector):
    l1 = len(matriz)
    l2 = len(vector)
    if l1 == l2:
        if l1 == 3:
            return [matriz[0][0]*vector[0] + matriz[0][1]*vector[1] + matriz[0][2]*vector[2],
                    matriz[1][0]*vector[0] + matriz[1][1]*vector[1] + matriz[1][2]*vector[2],
                    matriz[2][0]*vector[0] + matriz[2][1]*vector[1] + matriz[2][2]*vector[2]]
        elif l1 == 2:
            return [matriz[0][0]*vector[0] + matriz[0][1]*vector[1],
                    matriz[1][0]*vector[0] + matriz[1][1]*vector[1]]
        else:
            return "Error"

def resta_vector(v1, v2):
    res = []
    for i in range(min(len(v1), len(v2))):
        res.append(v1[i] - v2[i])
    return res

def resta_vectorv3(v1, v2):
    return [v1.x - v2[0], v1[1] - v2[1], v1[2] - v2[2]]

def dividir(vector: tuple, norma: float):
    return tuple(map(lambda x: x / norma, vector))

def mvMatriz4 (m1, m2):
    res = []

    for i in range(4):
        c = 0
        for j in range(4):
            c += m1[i][j] * m2[j]
        res.append(c)

    return res

def mvMatriz3 (m1, m2):
    res = []

    for i in range(3):
        c = 0
        for j in range(3):
            c += m1[i][j] * m2[j]
        res.append(c)

    return res

def dMatriz (m1, m2):
    res = []

    for i in range(len(m1)):
        c = len(m1[i])
        temporal = []

        for j in range(len(m1[i])):
            temporal.append(m1[i][j] / m2)
        res.append(c)

    return res

def colAtras(a):
    resultado = [[], [], [], []]

    for i in range(4):
        resultado[i] = [a[i][0], a[i][1], a[i][2], a[i][3]]

    return resultado

def colDelante(a):
    resultado = [[], [], [], []]

    for i in range(4):
        resultado[i] = [a[i][1], a[i][2], a[i][3], a[i][0]]

    return resultado

def mMatriz4 (m1, m2):
    c = colAtras(m2)
    res = []

    for i in range(4):
        temporal = []
        for j in range(4):
            d = 0
            for k in range(4):
                d += m1[i][k] * c[j][k]
            temporal.append(d)
            d = 0
        res.append(temporal)

    return res

def mMatriz3 (m1, m2):
    c = colAtras(m2)
    res = []

    for i in range(3):
        temporal = []
        for j in range(3):
            d = 0
            for k in range(3):
                d += m1[i][k] * c[j][k]
            temporal.append(d)
            d = 0
        res.append(temporal)

    return res

def rad(angulo):
    return angulo * math.pi / 180

def reng_a_col(renglon):
    res = [[], [], [], []]
    for i in range(4):
        vec = renglon[i]
        res[0].append(vec[0])
        res[1].append(vec[1])
        res[2].append(vec[2])
        res[3].append(vec[3])


    return res

def col_a_reng(columna):
    res = [[], [], [], []]
    for i in range(4):
        vec = columna[i]
        res[0].append(vec[0])
        res[1].append(vec[1])
        res[2].append(vec[2])
        res[3].append(vec[3])

    return res

def matriz_a_vector(matriz):
    res = []
    for i in range(len(matriz)):
        res.append(matriz[i][0])
        res.append(matriz[i][1])
        res.append(matriz[i][2])
        res.append(matriz[i][3])

    return res

def M4a3(a, y, x):
    resultado = []
    for i in range(4):
        temp = []
        for j in range(4):
            if y != i and x != j:
                temp.append(a[i][j])
        if len(temp) == 3:
            resultado.append(temp)
    return resultado

def inverso_matriz(matriz):
    res = []
    b = reng_a_col(matriz)
    c = []
    d = True
    for i in range(4):
        agregacion = []
        for j in range(4):
            d = M4a3(b, i, j)
            determinante = determinante3(d)
            if d == True:
                agregacion.append(determinante)
            else:
                agregacion.append(-(determinante))
            
        d = not d
        c.append(agregacion)

    det = determinante4(matriz)

    return dMatriz(c, det)

def suma_vector(v1, v2):
    res = []
    for i in range(min(len(v1), len(v2))):
        res.append(v1[i] + v2[i])
    return res

def norm(a):
    return (sum(a[i]**2 for i in range(len(a))))**0.5

def dividir(a,b): 
    if b == 0:
        return a
    if any(isinstance(x, list) for x in a):
        return [dividir(x,b) for x in a]
    return [a[i]/b for i in range(len(a))]

# def producto_cruz(a,b):
#     return [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]]