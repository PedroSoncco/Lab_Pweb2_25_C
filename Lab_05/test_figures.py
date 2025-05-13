# Aqui estan las imagenes requeridas en los ejercicios propuestos

from chess.picture import Picture
from chess.pieces import KNIGHT, QUEEN, SQUARE, ROCK, BISHOP, KING, PAWN
from chess.colors import *

def draw(picture):
    for row in picture.img:
        print(row)

def figura_a():
    caballo_blanco = Picture(KNIGHT) 
    caballo_negro = caballo_blanco.negative()
    fila_superior = caballo_blanco.join(caballo_negro)
    fila_inferior = caballo_negro.join(caballo_blanco)
    figura = fila_superior.up(fila_inferior)
    draw(figura)

def figura_b():
    caballo_blanco = Picture(KNIGHT)
    caballo_negro = caballo_blanco.negative()
    fila_superior = caballo_blanco.join(caballo_negro)
    fila_inferior = caballo_negro.verticalMirror().join(caballo_blanco.verticalMirror())
    figura = fila_superior.up(fila_inferior)
    draw(figura)

def figura_c():
    reina_blanca = Picture(QUEEN)
    figura = reina_blanca.horizontalRepeat(4)
    draw(figura)

def figura_d():
    casillero_negro = Picture(SQUARE).negative()
    casillero_blanco = Picture(SQUARE)
    patron = casillero_negro.join(casillero_blanco)
    figura = patron.horizontalRepeat(4)
    draw(figura)

def figura_e():
    casillero_negro = Picture(SQUARE).negative()
    casillero_blanco = Picture(SQUARE)
    patron = casillero_blanco.join(casillero_negro)
    figura = patron.horizontalRepeat(4)
    draw(figura)

def figura_f():
    casillero_negro = Picture(SQUARE).negative()
    casillero_blanco = Picture(SQUARE)
    fila_impar = casillero_negro.join(casillero_blanco).horizontalRepeat(4)
    fila_par = casillero_blanco.join(casillero_negro).horizontalRepeat(4)
    figura = fila_impar.up(fila_par).verticalRepeat(2)
    draw(figura)

def figura_g():
    casillero_blanco = Picture(SQUARE)
    casillero_negro = Picture(SQUARE).negative()

    piezas_negras = [
        Picture(ROCK).negative(),
        Picture(KNIGHT).negative(),
        Picture(BISHOP).negative(),
        Picture(QUEEN).negative(),
        Picture(KING).negative(),
        Picture(BISHOP).negative(),
        Picture(KNIGHT).negative(),
        Picture(ROCK).negative()
    ]

    peones_negros = [Picture(PAWN).negative() for _ in range(8)]

    peones_blancos = [Picture(PAWN) for _ in range(8)]

    piezas_blancas = [
        Picture(ROCK),
        Picture(KNIGHT),
        Picture(BISHOP),
        Picture(QUEEN),
        Picture(KING),
        Picture(BISHOP),
        Picture(KNIGHT),
        Picture(ROCK)
    ]

    def superponer_pieza(casillero, pieza):
        casillero_rows = casillero.img
        pieza_rows = pieza.img
        if len(casillero_rows) != len(pieza_rows) or len(casillero_rows[0]) != len(pieza_rows[0]):
            raise ValueError("El casillero y la pieza deben tener las mismas dimensiones")
        combined_rows = []
        for cas_row, pz_row in zip(casillero_rows, pieza_rows):
            combined_row = ''.join([pz_char if pz_char.strip() else cas_char for cas_char, pz_char in zip(cas_row, pz_row)])
            combined_rows.append(combined_row)
        return Picture(combined_rows)

    tablero_filas = []

    fila1_casilleros = []
    for i in range(8):
        casillero = casillero_negro if i % 2 == 0 else casillero_blanco
        pieza = superponer_pieza(casillero, piezas_negras[i])
        fila1_casilleros.append(pieza)
    fila1 = fila1_casilleros[0]
    for pieza in fila1_casilleros[1:]:
        fila1 = fila1.join(pieza)
    tablero_filas.append(fila1)

    fila2_casilleros = []
    for i in range(8):
        casillero = casillero_blanco if i % 2 == 0 else casillero_negro
        peon = superponer_pieza(casillero, peones_negros[i])
        fila2_casilleros.append(peon)
    fila2 = fila2_casilleros[0]
    for peon in fila2_casilleros[1:]:
        fila2 = fila2.join(peon)
    tablero_filas.append(fila2)

    for fila_num in range(2, 6):
        if fila_num % 2 == 0:
            fila = casillero_negro.join(casillero_blanco).horizontalRepeat(4)
        else:
            fila = casillero_blanco.join(casillero_negro).horizontalRepeat(4)
        tablero_filas.append(fila)

    fila7_casilleros = []
    for i in range(8):
        casillero = casillero_negro if i % 2 == 0 else casillero_blanco
        peon = superponer_pieza(casillero, peones_blancos[i])
        fila7_casilleros.append(peon)
    fila7 = fila7_casilleros[0]
    for peon in fila7_casilleros[1:]:
        fila7 = fila7.join(peon)
    tablero_filas.append(fila7)

    fila8_casilleros = []
    for i in range(8):
        casillero = casillero_blanco if i % 2 == 0 else casillero_negro
        pieza = superponer_pieza(casillero, piezas_blancas[i])
        fila8_casilleros.append(pieza)
    fila8 = fila8_casilleros[0]
    for pieza in fila8_casilleros[1:]:
        fila8 = fila8.join(pieza)
    tablero_filas.append(fila8)

    tablero_completo = tablero_filas[0]
    for fila in tablero_filas[1:]:
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
