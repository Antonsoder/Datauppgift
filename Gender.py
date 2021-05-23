#Importerar alla moduler som används senare
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Läser in filen(dataframe)
df = pd.read_csv("Gender_Data.csv")



#Plot 1


#Plot 1 med row 2, 3 columner och 1 i plotten
plt.subplot(2,3,1)
#Titel för diagrammet
plt.title("Totala Fall / kön")
#Här skapas diagrammet i subplotten och autopct gör så att andelen % syns.
plt.pie(df["Total_Cases"], autopct='%1.1f%%')
#Här skapas en legend, dvs beskrivning för varje kategori
plt.legend(["Män", "Kvinnor"])


#Plot 2 


#Plot 2 med row 2, 3 columner och 2 i plotten
plt.subplot(2,3,2)
#Titel för diagrammet
plt.title("Totalt antal Intensivvårdade / kön")
#Här skapas diagrammet i subplotten och autopct gör så att andelen % syns.
plt.pie(df["Total_ICU_Admissions"], autopct='%1.1f%%')
#Här skapas en legend, dvs beskrivning för varje kategori
plt.legend(["Män", "Kvinnor"])


#Plot 3 


#Plot 3 med row 2, 3 columner och 3 i plotten
plt.subplot(2,3,3)
#Titel för diagrammet
plt.title("Totalt antal döda / kön")
#Här skapas diagrammet i subplotten och autopct gör så att andelen % syns.
plt.pie(df["Total_Deaths"], autopct='%1.1f%%')
#Här skapas en legend, dvs beskrivning för varje kategori
plt.legend(["Män", "Kvinnor"])


#för att visa diagrammet
plt.show()
