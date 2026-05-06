import numpy as np
import matplotlib.pyplot as plt

# Tamaño del dominio (cm)
Lx, Ly = 40, 30
nx, ny = 200, 150

dx = Lx / nx
dy = Ly / ny

V = np.zeros((ny, nx))

# Coordenadas
x = np.linspace(0, Lx, nx)
y = np.linspace(0, Ly, ny)
X, Y = np.meshgrid(x, y)

# --- Geometría ---

# Electrodo circular
radio = 5
cx, cy = 25, 15
circle = (X - cx)**2 + (Y - cy)**2 <= radio**2

# Barra metálica (20 cm desde el borde del círculo)
barra_x = cx - radio - 20
barra = np.abs(X - barra_x) < dx

# Potenciales
V[circle] = 20
V[barra] = 0

# --- Relajación ---
for _ in range(3000):
    V_old = V.copy()
    
    V[1:-1,1:-1] = 0.25 * (
        V_old[1:-1,2:] + V_old[1:-1,:-2] +
        V_old[2:,1:-1] + V_old[:-2,1:-1]
    )
    
    V[circle] = 20
    V[barra] = 0

# Campo eléctrico
Ey, Ex = np.gradient(-V, dy, dx)

# --- Gráfica ---
plt.figure(figsize=(8,6))

# SOLO las equipotenciales pedidas
niveles = [2, 5, 10, 15, 18]
cont = plt.contour(X, Y, V, levels=niveles)

# Etiquetas
plt.clabel(cont, inline=True)

# Líneas de campo
plt.streamplot(X, Y, Ex, Ey, density=1)

# Electrodos
plt.contourf(X, Y, circle, levels=[0.5,1])
plt.contourf(X, Y, barra, levels=[0.5,1])

plt.title("Equipotenciales (2, 5, 10, 15, 18 V)")
plt.xlabel("cm")
plt.ylabel("cm")
plt.axis("equal")

plt.show()
