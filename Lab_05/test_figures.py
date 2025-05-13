# Aqui estan las imagenes requeridas en los ejercicios propuestos

from chess.picture import Picture
from chess.pieces import *
from chess.colors import *

def draw(picture):
    for row in picture.img:
        print(row)

def figura_a():
    caballo_blanco = knight
    caballo_negro = knight.negative()
    fila_superior = caballo_blanco.join(caballo_negro)
    fila_inferior = caballo_negro.join(caballo_blanco)
    figura = fila_superior.up(fila_inferior)
    draw(figura)

def figura_b():
    caballo_blanco = knight
    caballo_negro = knight.negative()
    fila_superior = caballo_blanco.join(caballo_negro)
    # Caballos inferiores con espejo vertical
    fila_inferior = caballo_negro.verticalMirror().join(caballo_blanco.verticalMirror())
    figura = fila_superior.up(fila_inferior)
    draw(figura)

def figura_c():
    reina_blanca = queen
    figura = reina_blanca.horizontalRepeat(4)
    draw(figura)

def figura_d():
    casillero_negro = square.negative()
    casillero_blanco = square
    patron = casillero_negro.join(casillero_blanco)
    figura = patron.horizontalRepeat(4)
    draw(figura)

def figura_e():
    casillero_negro = square.negative()
    casillero_blanco = square
    patron = casillero_blanco.join(casillero_negro)
    figura = patron.horizontalRepeat(4)
    draw(figura)

def figura_f():
    casillero_negro = square.negative()
    casillero_blanco = square
    fila_impar = casillero_negro.join(casillero_blanco).horizontalRepeat(4)
    fila_par = casillero_blanco.join(casillero_negro).horizontalRepeat(4)
    figura = fila_impar.up(fila_par).verticalRepeat(2)
    draw(figura)

def figura_g():
    # Crear casillas blancas y negras
    casillero_blanco = Picture(SQUARE)
    casillero_negro = Picture(SQUARE).negative()

    fila_piezas_negras = [
        Picture(ROCK).negative(),
        Picture(KNIGHT).negative(),
        Picture(BISHOP).negative(),
        Picture(QUEEN).negative(),
        Picture(KING).negative(),
        Picture(BISHOP).negative(),
        Picture(KNIGHT).negative(),
        Picture(ROCK).negative()
    ]

    fila_peones_negros = [Picture(PAWN).negative() for _ in range(8)]

    fila_peones_blancos = [Picture(PAWN) for _ in range(8)]

    fila_piezas_blancas = [
        Picture(ROCK),
        Picture(KNIGHT),
        Picture(BISHOP),
        Picture(QUEEN),
        Picture(KING),
        Picture(BISHOP),
        Picture(KNIGHT),
        Picture(ROCK)
    ]

    # Construir el tablero completo
    tablero = []

    # Fila 1: Piezas negras
    fila_1 = casillero_negro.join(casillero_blanco).horizontalRepeat(4)
    piezas_fila_1 = fila_piezas_negras[0]
    for pieza in fila_piezas_negras[1:]:
        piezas_fila_1 = piezas_fila_1.join(pieza)
    tablero.append(piezas_fila_1.up(fila_1))

    # Fila 2: Peones negros
    fila_2 = casillero_blanco.join(casillero_negro).horizontalRepeat(4)
    peones_fila_2 = fila_peones_negros[0]
    for peon in fila_peones_negros[1:]:
        peones_fila_2 = peones_fila_2.join(peon)
    tablero.append(peones_fila_2.up(fila_2))

    # Filas 3-6: Casillas vacías
    fila_vacia_1 = casillero_negro.join(casillero_blanco).horizontalRepeat(4)
    fila_vacia_2 = casillero_blanco.join(casillero_negro).horizontalRepeat(4)
    for _ in range(2):
        tablero.append(fila_vacia_1)
        tablero.append(fila_vacia_2)

    # Fila 7: Peones blancos
    fila_7 = casillero_negro.join(casillero_blanco).horizontalRepeat(4)
    peones_fila_7 = fila_peones_blancos[0]
    for peon in fila_peones_blancos[1:]:
        peones_fila_7 = peones_fila_7.join(peon)
    tablero.append(peones_fila_7.up(fila_7))

    # Fila 8: Piezas blancas
    fila_8 = casillero_blanco.join(casillero_negro).horizontalRepeat(4)
    piezas_fila_8 = fila_piezas_blancas[0]
    for pieza in fila_piezas_blancas[1:]:
        piezas_fila_8 = piezas_fila_8.join(pieza)
    tablero.append(piezas_fila_8.up(fila_8))

    # Unir todas las filas en un solo tablero
    tablero_completo = tablero[0]
    for fila in tablero[1:]:
        tablero_completo = tablero_completo.up(fila)

    draw(tablero_completo)

# Ejecutar todas las figuras
if __name__ == "__main__":
    print("Figura a:")
    figura_a()
    
    print("\nFigura b:")
    figura_b()
    
    print("\nFigura c:")
    figura_c()
    
    print("\nFigura d:")
    figura_d()
    
    print("\nFigura e:")
    figura_e()
    
    print("\nFigura f:")
    figura_f()
    
    print("\nFigura g:")
    figura_g()
