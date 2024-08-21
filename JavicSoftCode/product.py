class Product:
  # Variable que pertenece a la clase en sí, no a las instancias individuales de esa clase.
  # Esto significa que todas las instancias de la clase comparten el mismo valor para ese atributo,
  # a menos que sea explícitamente modificado.
  next = 0

  def __init__(self, descrip="Ninguno", preci=0, stock=0):
    # Método constructor para inicializar los atributos de la clase Product
    Product.next += 1
    # Variables de instancias
    self.__id = Product.next  # Asigna el ID único a la instancia
    self.descrip = descrip
    self.preci = preci
    self.__stock = stock  # Atributo privado para almacenar el stock del producto

  @property
  def stock(self):
    # Getter para obtener el valor del atributo privado __stock
    return self.__stock

  def __repr__(self):
    # Método especial para representar la clase Product como una cadena
    return f'Producto:{self.__id} {self.descrip} {self.preci} {self.stock}'

  def __str__(self):
    # Método especial para representar la clase Product como una cadena
    return f'Producto:{self.__id} {self.descrip} {self.preci} {self.stock}'

  def getJson(self):
    # Método para obtener una representación JSON del producto
    return {"id": self.__id, "descripcion": self.descrip, "precio": self.preci, "stock": self.stock}

  def show(self):
    # Método para imprimir los detalles del producto en la consola
    print(f'{self.__id}  {self.descrip}           {self.preci}  {self.stock}')


if __name__ == "__main__":
  product1 = Product("Aceite", 2, 1000)
  print(product1)

  product2 = Product("Colas", 3, 5000)
  product3 = Product("Leche", 1, 300)

  products = [product1, product2, product3]

  print('Id Descripcion Precio Stock')
  for prod in products:
    prod.show()

  prods = [prod.getJson() for prod in products]
  print(prods)
