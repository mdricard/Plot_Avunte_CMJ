import matplotlib.pyplot as plt
import numpy as np
file_name = "D:/Avunte SUPER Jump/AvunteCMJ.csv"
data = np.genfromtxt(file_name, delimiter=",", skip_header=2)
time = data[:, 0]           # take the first column all rows
force = data[:, 1]          # take the second column all rows

plt.plot(force)
plt.show()