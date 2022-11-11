

```python
#importing dataset
import pandas as pd
import os
import numpy as np
```


```python
#location of csv file on my machine
df = pd.read_csv("C:\\Users\\Dalit\\OneDrive\\Desktop\\Python Bootcamp\\Python Assignment 1\\Pybank\\budget_data.csv")
            
```


```python
#reading csv file dataset
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Profit/Losses</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Jan-10</td>
      <td>1088983</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Feb-10</td>
      <td>-354534</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Mar-10</td>
      <td>276622</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Apr-10</td>
      <td>-728133</td>
    </tr>
    <tr>
      <th>4</th>
      <td>May-10</td>
      <td>852993</td>
    </tr>
  </tbody>
</table>
</div>




```python
#calculating total number of months in dataset
print (df['Date'].count())
```

    86
    


```python
#calculating net total of profits and losses
print(df['Profit/Losses'].sum())
```

    22564198
    


```python
# calculating average changes
print (df["Profit/Losses"].diff())
```

    0           NaN
    1    -1443517.0
    2      631156.0
    3    -1004755.0
    4     1581126.0
            ...    
    81   -1627245.0
    82     616795.0
    83     628522.0
    84      90895.0
    85    -224669.0
    Name: Profit/Losses, Length: 86, dtype: float64
    


```python
print (df["Profit/Losses"].max())
```

    1141840
    


```python
print (df["Profit/Losses"].min())

```

    -1194133
    


```python
print (df["Profit/Losses"].mean())
```

    262374.3953488372
    
