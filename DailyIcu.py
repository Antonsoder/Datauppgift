#Importerar alla moduler som används senare
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Läser in filen(dataframe)
df = pd.read_csv("National_Daily_ICU_Admissions.csv")

#Skapar en variabel för att x-labeln bara ska stå var tionde dag
x_labels = np.arange(0, len(df), 10)

#Eftersom det blir väldigt rörigt med vågräta x-labels så roteras dem här 45 grader.
plt.xticks(x_labels, rotation=45)

#Skapar ett diagram med "datum" på x-axeln och antalet intensivvårdade på y-axeln.
plt.plot(df["Date"], df["National_Daily_ICU_Admissions"])

#Titel för diagrammet
plt.title("Antal intensivvård/dag")

#För att kunna se diagrammet krävs en plt.show() för att visa det.
plt.show()