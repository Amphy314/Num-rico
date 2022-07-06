import pandas as pd 
import matplotlib.pyplot as plt 

x = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24]
y = [22, 20.5, 19, 18.5, 18, 18, 18.5, 19, 21, 23, 24, 24.5, 25, 26, 27, 28, 28, 26, 24.5, 23, 22, 22, 21.5, 21, 22]

coordenadas = pd.DataFrame({"x": x, "y": y})
coordenadas
print("\n\n")

plt.figure(figsize=(12, 10))
plt.scatter(coordenadas.x, coordenadas.y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()