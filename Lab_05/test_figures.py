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
    casillero_negro = square.negative()
    casillero_blanco = square
    fila_impar = casillero_negro.join(casillero_blanco).horizontalRepeat(4)
    fila_par = casillero_blanco.join(casillero_negro).horizontalRepeat(4)
    tablero = fila_impar.up(fila_par).verticalRepeat(4)
    draw(tablero)

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
