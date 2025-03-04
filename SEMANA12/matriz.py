import random

# Definimos las ciudades y los días de la semana
ciudades = ["Ciudad A", "Ciudad B", "Ciudad C"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 2  # Número de semanas

# Inicializamos la matriz 3D con temperaturas aleatorias
# Matriz: [ciudad][día][semana]
temperaturas = [[[random.randint(15, 30) for _ in range(len(dias_semana))] for _ in range(semanas)] for _ in range(len(ciudades))]

# Mostrar la matriz de temperaturas
print("Matriz de Temperaturas (Ciudad, Día, Semana):")
for i, ciudad in enumerate(ciudades):
    for j in range(semanas):
        print(f"{ciudad}, Semana {j + 1}: {temperaturas[i][j]}")

# Calcular y mostrar el promedio de temperaturas por ciudad y semana
print("\nPromedio de Temperaturas por Ciudad y Semana:")
for i, ciudad in enumerate(ciudades):
    for j in range(semanas):
        suma_temperaturas = sum(temperaturas[i][j])
        promedio = suma_temperaturas / len(dias_semana)
        print(f"{ciudad}, Semana {j + 1}: {promedio:.2f} °C")
        
