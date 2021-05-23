#Importerar alla moduler som används senare
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Läser in filen(dataframe)
df = pd.read_csv("Regional_Totals_Data.csv")

#Plot 1 med row 2, 3 columner och 1 i plotten
plt.subplot(2,3,1)
#Skapar x-labels (xticks) med en rotation på 90 grader
plt.xticks(rotation=90)
#Titel för diagrammet
plt.title("Total cases")
#Skapar diagrammet
plt.bar(df["Region"],df["Total_Cases"])


#Plot 2 med row 2, 3 columner och 2 i plotten
plt.subplot(2,3,2)
#Skapar x-labels (xticks) med en rotation på 90 grader
plt.xticks(rotation=90)
#Titel för diagrammet
plt.title("Total_Deaths")
#Skapar diagrammet
plt.bar(df["Region"],df["Total_Deaths"])

#Plot 3 med row 2, 3 columner och 3 i plotten
plt.subplot(2,3,3)
#Skapar x-labels (xticks) med en rotation på 90 grader
plt.xticks(rotation=90)
#Titel för diagrammet
plt.title("Total_ICU_Admissions")
#Skapar diagrammet
plt.bar(df["Region"],df["Total_ICU_Admissions"])

#Här visas diagrammet
plt.show()

