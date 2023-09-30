class Articulo:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def vender(self, cantidad_vendida):
        if cantidad_vendida <= 0:
            print("La cantidad vendida debe ser mayor que cero.")
        elif cantidad_vendida > self.cantidad:
            print(f"No hay suficiente stock de {self.nombre}. Stock actual: {self.cantidad}")
        else:
            self.cantidad -= cantidad_vendida
            total_venta = cantidad_vendida * self.precio
            print(f"Venta realizada:")
            print(f"Artículo: {self.nombre}")
            print(f"Cantidad vendida: {cantidad_vendida}")
            print(f"Precio unitario: {self.precio}")
            print(f"Total de la venta: {total_venta}")
            print(f"Stock restante: {self.cantidad}")

articulo1 = Articulo("Camisa", 30, 15.99)

print("Venta 1:")
articulo1.vender(10)

print("\nVenta 2:")
articulo1.vender(30)

print("\nVenta 3:")
articulo1.vender(20)
