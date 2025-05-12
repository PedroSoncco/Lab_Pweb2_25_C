import os
import sys
from colors import color

def draw(picture, scale=1):
    """
    Dibuja una imagen de Picture en la consola
    Args:
        picture: Objeto Picture a dibujar
        scale: Factor de escala (1=normal, 2=doble tamaño, etc.)
    """
    # Esto lo agregue para limpiar pantalla para mejor visualizacion
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # esto escalara la imagen si es necesario
    scaled_img = []
    if scale > 1:
        for row in picture.img:
            scaled_row = ""
            for char in row:
                scaled_row += char * scale
            for _ in range(scale):
                scaled_img.append(scaled_row)
    else:
        scaled_img = picture.img
    
    # esto dibujara cada línea con colores aproximados
    for row in scaled_img:
        colored_row = []
        for char in row:
            if char in color:
                
                color_code = {
                    (255, 255, 255): '\033[97m',  # blanco
                    (0, 0, 0): '\033[30m',        # negro
                    (200, 200, 200): '\033[37m',  # gris claro
                    (127, 127, 127): '\033[90m',  # gris
                    (50, 50, 50): '\033[90m',     # grs oscuro
                    (0, 0, 255): '\033[94m',      # azul
                }.get(color[char], '\033[0m')
                colored_row.append(f"{color_code}{char}\033[0m")
            else:
                colored_row.append(char)
        print(''.join(colored_row))
