import matplotlib.pyplot as plt

# Dati da visualizzare
x = [1, 5, 13, 10, 50]
y = [2, 6, 10, 14, 20]

# Creazione del grafico a linee
plt.plot(x, y)

# Personalizzazione dell'aspetto del grafico
plt.title("Grafico a linee")
plt.xlabel("X")
plt.ylabel("Y")

# Mostra il grafico
plt.show()