#productos = {modelo: [marca, pantalla, RAM, disco, GB de DD, procesador, video], ...]
productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'], 
}

#stock = {modelo: [precio, stock], ...]
stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0], 
}

def stock_Marcas(modelo):
    total_stock = 0
    for codigo, stock in productos.items():
     if stock[i].hower() == productos.lower():
      total_stock = stock[codigo][1]
        

def busqueda_precio (p_minimo, p_maximo):
    try:
        p_minimo= int(p_minimo)
        p_maximo= int(p_maximo)
    except ValueError:
        print("Debe ingresar Datos Validos")
        return

resultado =[]
p_minimo=int()
p_maximo=int()
Marca=[]


for codigo, (precio, stock)in stock.items():
    if p_minimo <= precio <= p_maximo and stock>0:
        nombre = productos[codigo][i]
        resultado.append(f"{nombre}--{codigo}")
if resultado:
    resultado.sort()
    print(resultado)
else:
    print("No hay marcas en ese rango de precio")

print("***MENU PRINCIPAL***")
print("1. Stock Marca.")
print("2. Búqueda por precio.")
print("3. Actualizar precio.")
print("4. Salir")
opcion = input("Eligue una opcion de 1-4")

while True:
    try: 
        if opcion == "1":
         print("Ingrese el nombre de la Marca")
         print(f"{nombre}--{codigo}")
        if opcion =="2":
         print(f"Ingrese el {p_minimo} y el {p_maximo}:")
        if opcion == "3":
           Saldo_nuevo=input(f"Ingrese el {codigo} un nuevon Precio ")
           print("Codigo actualizado y nuevo precio")
        if opcion== "4":
           print("Que tenga un lindo dia")
           break
    except ValueError:
       print("Debe ingresar datos validos")
    else:
       print("Error en introducir datos")
       break







        