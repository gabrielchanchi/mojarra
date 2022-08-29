import math

def area_triangulo():

  print("Calcular Área de un Triángulo con el Teorema de Herón")
  a= int(input("Ingrese valor lado a: "))
  b= int(input("Ingrese valor lado b: "))
  c= int(input("Ingrese valor lado c: "))
  
  s = (a + b + c) / 2
  area= math.sqrt(s*(s-a)*(s-b)*(s-c))
  
  print("Área calculada: ", area)
  
  
