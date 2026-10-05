import pandas as pd
import matplotlib.pyplot as plt
 
df = pd.read_csv("ikasleak_Matplot.csv")
 
kopurua = df.groupby("ikasgela")["izena"].count()
bataz_bestekoa = df.groupby("ikasgela")["nota"].mean()
 
fig, ax = plt.subplots(1, 2, figsize=(10, 4))
 
ax[0].bar(kopurua.index, kopurua)
ax[0].set_title("Ikasle kopurua ikasgelako")
 
ax[1].bar(bataz_bestekoa.index, bataz_bestekoa)
ax[1].set_title("Bataz besteko nota ikasgelako")
 
plt.tight_layout()
plt.savefig("ikasleak_grafikoa.png")
plt.show()
