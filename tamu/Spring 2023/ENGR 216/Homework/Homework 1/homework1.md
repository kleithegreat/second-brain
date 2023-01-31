#### HW 1: Descriptive Statistics and Measurement Error  
#### 31 January 2023  
#### Kevin Lei  
#### 432009232  
#### ENGR 216-445  
#### Page 1 of x  
---

### Given:
An excel spreadsheet of proportions of concrete ingredients and its compressive strength

### Find:
a) The mean, median, and mode of the water component  
b) The range, variance, and standard deviation of the fine aggregate component  
c) The mean and standard error of the cement component  
d) The mean and standard error of the concrete compressive strength

### Diagram:
Not applicable

### Theory:
The mean of a set of data is the sum of all the terms divided by the number of terms.  
The median of a set of data is the middle value when the data is sorted. If there is an even amount of values, then the median is the mean of the middle two values.  
The mode is the value that appears most frequently in a set of data.
The range of a set of data is the distance between its mininum and maximum values.  
The variance of a set of data is the sum of the squares of the difference between each value and the mean all divided by the number of terms.  
The standard deviation is the average distance from the mean for each value in a set of data. It can be calculated by taking the square root of the variance.  
The standard error measures the accuracy of a sample and is calculated by dividing the standard deviation of the sample by the square root of the number of terms.  

### Assumptions:
???  

### Solution:
```python
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
meanCompress = data["Concrete compressive strength(MPa, megapascals)"].mean()
errorCompress = data["Concrete compressive strength(MPa, megapascals)"].sem()
```
**a)**  
**b)**  
**c)**  
**d)**  