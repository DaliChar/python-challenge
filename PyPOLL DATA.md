

```python
#directing python to our intended file 
import pandas as pd
import numpy as np
df = pd.read_csv("C:\\Users\\Dalit\\OneDrive\\Desktop\\Python Bootcamp\\Python Assignment 1\\Pypoll\\election_data.csv")
```


```python
#reading cvs file
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
      <th>Ballot ID</th>
      <th>County</th>
      <th>Candidate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1323913</td>
      <td>Jefferson</td>
      <td>Charles Casper Stockham</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1005842</td>
      <td>Jefferson</td>
      <td>Charles Casper Stockham</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1880345</td>
      <td>Jefferson</td>
      <td>Charles Casper Stockham</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1600337</td>
      <td>Jefferson</td>
      <td>Charles Casper Stockham</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1835994</td>
      <td>Jefferson</td>
      <td>Charles Casper Stockham</td>
    </tr>
  </tbody>
</table>
</div>




```python
#computing how many votes each candidate received and adding them together for total sum
df['Candidate'].value_counts()

```




    Diana DeGette              272892
    Charles Casper Stockham     85213
    Raymon Anthony Doane        11606
    Name: Candidate, dtype: int64




```python
#calculating percentages, highest % means winner
df['Candidate'].value_counts(normalize=True)
```




    Diana DeGette              0.738122
    Charles Casper Stockham    0.230485
    Raymon Anthony Doane       0.031392
    Name: Candidate, dtype: float64




```python

```
