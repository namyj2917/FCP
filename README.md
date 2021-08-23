# Further Computer Programming Coursework
## Covid-19 Infection and Death rate in London

Using matplotlib, we will generate graphs for the rate of death and the rate of the COVID-19.
Using seaborn to visualize statistics.
Import pandas to easily manipulate the number table of Covid-19.

```c
import matplotlib.pyplot as plt
from matplotlib import rc
import seaborn as sns
import pandas as pd

```
read csv file (infection.csv / death.csv) by pandas

```c
df_infection = pd.read_csv("/Users/yunji/infection.csv")
df_death=pd.read_csv("/Users/yunji/death.csv")

```
pd.concat function to link data.

```c
df = pd.concat([df_infection[['date','cumCasesBySpecimenDate']],df_death['cumDeaths28DaysByDeathDate']],axis=1)

```
Index with index values for each row and column.
```c
df = df.iloc[::-1].reset_index(drop=True)
```
plt.subplots() is a function that returns a tuple containing figure and axis objects.
Set the infection rate to red
Set the rate of death to blue
There is a difference in the number of people each, so it makes the axis different.
```c
fig, ax = plt.subplots(1,1,figsize=(8,8))
g = df[['date','cumCasesBySpecimenDate']].plot.line(ax=ax,color='red')
ax.set_xticklabels([])
ax = ax.twinx()
df[['date','cumDeaths28DaysByDeathDate']].plot.line(ax=ax,color='blue')
ax.set_title('cumCasesBySpecimenDate vs cumDeaths28DaysByDeathDate')

```
Show the plot
```c
plt.show()
```
