#Importerar alla moduler som används senare
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Läser in filen(dataframe)
df = pd.read_csv("National_Daily_Deaths.csv")

#Skapar en variabel för att x-labeln bara ska stå var tionde dag
x_labels = np.arange(0, len(df), 10)

#Eftersom det blir väldigt rörigt med vågräta x-labels så roteras dem här 45 grader.
plt.xticks(x_labels, rotation=45)

#Skapar ett diagram med "datum" på x-axeln och antalet döda på y-axeln
plt.plot(df["Date"], df["National_Daily_Deaths"])

#Titel för diagrammet
plt.title("Antal döda/dag")

#Här visas diagrammet
plt.show()