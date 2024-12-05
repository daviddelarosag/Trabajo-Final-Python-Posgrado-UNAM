import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Dimensiones de la cuadrícula (representando el condado)
N = 20

# Inicializar el condado: 50% secular (1) y 50% religioso (0)
grid = np.random.choice([0, 1], N * N, p=[0.5, 0.5]).reshape(N, N)

# Número de iteraciones
num_iterations = 100

# Función para actualizar el estado de la cuadrícula
def update(data):
    global grid
    new_grid = grid.copy()
    for i in range(N):
        for j in range(N):
            # Contar vecinos seculares (1) y religiosos (0)
            total_secular = int((grid[i, (j-1)%N] + grid[i, (j+1)%N] +
                                 grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                                 grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
                                 grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N]))

            # Reglas del cambio ideológico basadas en presión social
            if grid[i, j] == 1:  # Si la persona es secular
                if total_secular < 2 or total_secular > 3:
                    new_grid[i, j] = 0  # Se vuelve religiosa
            else:  # Si la persona es religiosa
                if total_secular == 3:
                    new_grid[i, j] = 1  # Se vuelve secular

    # Actualizar la cuadrícula y devolver el estado
    mat.set_data(new_grid)
    grid = new_grid
    return [mat]

# Función para limitar las iteraciones
def update_with_limit(frame):
    if frame >= num_iterations:
        ani.event_source.stop()  # Detener la animación después de las iteraciones definidas
    else:
        return update(frame)

# Configuración de la visualización
fig, ax = plt.subplots()
mat = ax.matshow(grid, cmap="coolwarm")  # Color azul para secular y rojo para religioso

# Crear la animación, limitando a 50 iteraciones
ani = animation.FuncAnimation(fig, update_with_limit, frames=num_iterations, interval=200, repeat=False)

plt.show()
