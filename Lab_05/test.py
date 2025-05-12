from chessPictures import *
from interpreter import draw

# ejemplo siple de uso
draw(rock)  # Dibuja una torre
draw(king)  # Dibuja un rey

# ejemplo complejo
tablero = square.join(square.negative()).horizontalRepeat(4)
draw(tablero, scale=2) 
