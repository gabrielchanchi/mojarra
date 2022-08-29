def calcular_area_rombo():
  diagonal_mayor = float (input ('Ingresa el valor de diagonal mayor: '))
  diagonal_menor = float (input ('Ingresa el valor de diagonal menor: '))
  area=diagonal_mayor*diagonal_menor/2
  print ('Valor de area: ' + repr (area))

calcular_area_rombo()
