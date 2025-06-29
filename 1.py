import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)
Z = np.sqrt(np.abs(X**7 + Y**7))  # 添加绝对值确保实数解

surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
ax.set_title('z = √(x⁷ + y⁷)')
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()