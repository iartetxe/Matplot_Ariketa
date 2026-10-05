import pandas as pd
import matplotlib.pyplot as plt
 
df = pd.read_csv("eguraldia.csv")
 
plt.bar(df["eguna"], df["euria_mm"], color="steelblue", label="Euria (mm)")
plt.plot(df["eguna"], df["tenperatura"], "r-o", label="Tenperatura (°C)")
 
plt.title("Egun bakoitzeko eguraldia")
plt.xlabel("Eguna")
plt.ylabel("Balioa")
plt.ylim(0, 30)
plt.legend()
plt.grid(True)
 
plt.savefig("eguraldia_grafikoa.png")
plt.show()
