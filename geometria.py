from math import sqrt
def distancia (x1, y1, x2, y2):
    respuesta=sqrt((x2 - x1)**2+(y2-y1)**2)
    return respuesta
def calcular_distancia(x1, y1, x2, y2):
    """
    Calcula la distancia euclidiana entre dos puntos en un plano bidimensional.
    Parámetros:
    x1 (float): Coordenada x del primer punto.
    y1 (float): Coordenada y del primer punto.
    x2 (float): Coordenada x del segundo punto.
    y2 (float): Coordenada y del segundo punto.
    Retorna:
    float: La distancia euclidiana entre los dos puntos.
    Ejemplo:
    >>> calcular_distancia(1, 2, 4, 6)
    5.0
    """
    distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return distancia