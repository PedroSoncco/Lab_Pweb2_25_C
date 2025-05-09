from colors import *
class Picture:
  def __init__(self, img):
    self.img = img;

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    """ Devuelve el espejo vertical de la imagen """
    vertical = []
    for value in self.img:
    	vertical.append(value[::-1])
    return Picture(vertical)

  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    return Picture(self.img[::-1])

  def negative(self):
    """ Devuelve un negativo de la imagen """
     negative_img = []
        for row in self.img:
            negative_row = ''.join([self._invColor(c) for c in row])
            negative_img.append(negative_row)
    return Picture(negative_img)

  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento 
        al lado derecho de la figura actual """
    if len(self.img) != len(p.img):
            raise ValueError("Las imágenes deben tener la misma altura para unirlas horizontalmente")
        
        joined_img = []
        for i in range(len(self.img)):
            joined_row = self.img[i] + p.img[i]
            joined_img.append(joined_row)
    return Picture(joined_img)

  def up(self, p):
    return Picture(p.img + self.img)

  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """
    return Picture(self.img + p.img)
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        n veces """
     if n <= 0:
            raise ValueError("n debe ser un entero positivo")
        
        repeated_img = []
        for row in self.img:
            repeated_row = row * n
            repeated_img.append(repeated_row)
    return Picture(repeated_img)

  def verticalRepeat(self, n):
     """ Devuelve una nueva figura repitiendo la figura actual debajo n veces """
        if n <= 0:
            raise ValueError("n debe ser un entero positivo")
    return Picture(self.img * n)

  #Extra
  def rotate(self):
    """ Devuelve una figura rotada en 90 grados en sentido horario """
     if not self.img:
            return Picture([])
        
        # Transponer la matriz y luego invertir cada fila
        rotated_img = []
        for i in range(len(self.img[0])):
            rotated_row = ''.join([row[i] for row in self.img][::-1])
            rotated_img.append(rotated_row)
    return Picture(rotated_img)
