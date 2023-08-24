import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
# matplotlib.use("Qt5Agg")  # Qt5Agg

max = [3.1,4.2,5.2]
step = [0.1,0.2,0.3]
z = [0,1,2]

i = random.choice(z)
# Erstelle den Vektor a
a = np.arange(step[i], max[i], step[i])
print(a)
# Berechne die Vektoren b und c
b = a **2
c = a + a

# Finde den Schnittpunkt
try:
    intersection_index = np.where(b >= c)[0][0]
except:
    intersection_index = np.where(b > c)[0][0]

intersection_a = a[intersection_index]
intersection_b = b[intersection_index]
intersection_c = c[intersection_index]

# Plotte die Kurven
plt.plot(a, b, label='b = a^2')
plt.plot(a, c, label='c = a + a')
plt.scatter(intersection_a, intersection_b, color='red', label=f'b>i ab {round(intersection_a,3)}')

# Beschriftungen
plt.xlabel('a')
plt.ylabel('Wert')
plt.title('Schnittpunkt von b und c')
plt.legend()

# Zeige den Plot
plt.show()
# new line