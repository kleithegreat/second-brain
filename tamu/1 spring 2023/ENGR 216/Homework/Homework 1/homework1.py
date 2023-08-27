import pandas as pd

data = pd.read_csv("Concrete_Data.csv")

#a) The mean, median, and mode of the water component (COLUMN INDEX 3)
meanWater = data["Water  (component 4)(kg in a m^3 mixture)"].mean()
medianWater = data["Water  (component 4)(kg in a m^3 mixture)"].median()
modeWater = data["Water  (component 4)(kg in a m^3 mixture)"].mode()

#b) The range, variance, and standard deviation of the fine aggregate component
rangeFineAgg = data["Fine Aggregate (component 7)(kg in a m^3 mixture)"].max() - data["Fine Aggregate (component 7)(kg in a m^3 mixture)"].min()
varianceFineAgg = data["Fine Aggregate (component 7)(kg in a m^3 mixture)"].var()
stdevFineAgg = data["Fine Aggregate (component 7)(kg in a m^3 mixture)"].std()

#c) The mean and standard error of the cement component
meanCement = data["Cement (component 1)(kg in a m^3 mixture)"].mean()
errorCement = data["Cement (component 1)(kg in a m^3 mixture)"].sem()

#d) The mean and standard error of the concrete compressive strength
meanCompress = data["Concrete compressive strength(MPa, megapascals) "].mean()
errorCompress = data["Concrete compressive strength(MPa, megapascals) "].sem()

print(f"{meanWater}, {medianWater}, {modeWater}")
print(f"{rangeFineAgg}, {varianceFineAgg}, {stdevFineAgg}")
print(f"{meanCement}, {errorCement}")
print(f"{meanCompress}, {errorCompress}")
