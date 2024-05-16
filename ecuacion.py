n = int(input('Digite el grado de la funcion: '))
variable = float(input('Digite el valor de la variable x: '))

grades = {}

for i in range(n):
    grades[n-i]= float(input(f'Digite el coeficiente de la variable de grado {n-i}: '))

var_independiente = float(input('Digite el valor de la variable independiente: '))

solucion = var_independiente

for key, value in grades.items():
    solucion += value*(variable**key)

print(solucion)