
### Dependents
***


```python
import pandas as pd
import matplotlib.pyplot as plt
```


```python
stations = pd.read_csv('../hawaii_stations.csv')
measure = pd.read_csv('../hawaii_measurements.csv', parse_dates=['date'])
```

### Data Analysis and implementing fixes - Station Data
***


```python
# Printing the data
stations
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>station</th>
      <th>name</th>
      <th>latitude</th>
      <th>longitude</th>
      <th>elevation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>USC00519397</td>
      <td>WAIKIKI 717.2, HI US</td>
      <td>21.27160</td>
      <td>-157.81680</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>USC00513117</td>
      <td>KANEOHE 838.1, HI US</td>
      <td>21.42340</td>
      <td>-157.80150</td>
      <td>14.6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>USC00514830</td>
      <td>KUALOA RANCH HEADQUARTERS 886.9, HI US</td>
      <td>21.52130</td>
      <td>-157.83740</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>USC00517948</td>
      <td>PEARL CITY, HI US</td>
      <td>21.39340</td>
      <td>-157.97510</td>
      <td>11.9</td>
    </tr>
    <tr>
      <th>4</th>
      <td>USC00518838</td>
      <td>UPPER WAHIAWA 874.3, HI US</td>
      <td>21.49920</td>
      <td>-158.01110</td>
      <td>306.6</td>
    </tr>
    <tr>
      <th>5</th>
      <td>USC00519523</td>
      <td>WAIMANALO EXPERIMENTAL FARM, HI US</td>
      <td>21.33556</td>
      <td>-157.71139</td>
      <td>19.5</td>
    </tr>
    <tr>
      <th>6</th>
      <td>USC00519281</td>
      <td>WAIHEE 837.5, HI US</td>
      <td>21.45167</td>
      <td>-157.84889</td>
      <td>32.9</td>
    </tr>
    <tr>
      <th>7</th>
      <td>USC00511918</td>
      <td>HONOLULU OBSERVATORY 702.2, HI US</td>
      <td>21.31520</td>
      <td>-157.99920</td>
      <td>0.9</td>
    </tr>
    <tr>
      <th>8</th>
      <td>USC00516128</td>
      <td>MANOA LYON ARBO 785.2, HI US</td>
      <td>21.33310</td>
      <td>-157.80250</td>
      <td>152.4</td>
    </tr>
  </tbody>
</table>
</div>




```python
stations.dtypes
```




    station       object
    name          object
    latitude     float64
    longitude    float64
    elevation    float64
    dtype: object




```python
# Note that the 'name' column is actually city, state, country and other
stations['name']
```




    0                      WAIKIKI 717.2, HI US
    1                      KANEOHE 838.1, HI US
    2    KUALOA RANCH HEADQUARTERS 886.9, HI US
    3                         PEARL CITY, HI US
    4                UPPER WAHIAWA 874.3, HI US
    5        WAIMANALO EXPERIMENTAL FARM, HI US
    6                       WAIHEE 837.5, HI US
    7         HONOLULU OBSERVATORY 702.2, HI US
    8              MANOA LYON ARBO 785.2, HI US
    Name: name, dtype: object




```python
# Creating a lamba function to read each row and find the comma...then split the field
fix_comma = lambda x: pd.Series([i for i in reversed(x.split(','))])
```


```python
# Applying the lamba function on each row
stat_info = stations['name'].apply(fix_comma)
print(stat_info)
```

            0                                1
    0   HI US                    WAIKIKI 717.2
    1   HI US                    KANEOHE 838.1
    2   HI US  KUALOA RANCH HEADQUARTERS 886.9
    3   HI US                       PEARL CITY
    4   HI US              UPPER WAHIAWA 874.3
    5   HI US      WAIMANALO EXPERIMENTAL FARM
    6   HI US                     WAIHEE 837.5
    7   HI US       HONOLULU OBSERVATORY 702.2
    8   HI US            MANOA LYON ARBO 785.2



```python
# Function created two columns 0 and 1. Note that column 0 created state and country
stat_info[0]
```




    0     HI US
    1     HI US
    2     HI US
    3     HI US
    4     HI US
    5     HI US
    6     HI US
    7     HI US
    8     HI US
    Name: 0, dtype: object




```python
stat_info[1]
```




    0                      WAIKIKI 717.2
    1                      KANEOHE 838.1
    2    KUALOA RANCH HEADQUARTERS 886.9
    3                         PEARL CITY
    4                UPPER WAHIAWA 874.3
    5        WAIMANALO EXPERIMENTAL FARM
    6                       WAIHEE 837.5
    7         HONOLULU OBSERVATORY 702.2
    8              MANOA LYON ARBO 785.2
    Name: 1, dtype: object




```python
# Creating another lamba function to find spaces and split the each value
fix_space_0 = lambda x: pd.Series([i for i in reversed(x.split(' '))])
```


```python
# Apply new function to the column entries
stat_info_st = stat_info[0].apply(fix_space_0)
print(stat_info_st)
```

        0   1 2
    0  US  HI  
    1  US  HI  
    2  US  HI  
    3  US  HI  
    4  US  HI  
    5  US  HI  
    6  US  HI  
    7  US  HI  
    8  US  HI  



```python
stat_info_st[[0,1]]
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>US</td>
      <td>HI</td>
    </tr>
    <tr>
      <th>1</th>
      <td>US</td>
      <td>HI</td>
    </tr>
    <tr>
      <th>2</th>
      <td>US</td>
      <td>HI</td>
    </tr>
    <tr>
      <th>3</th>
      <td>US</td>
      <td>HI</td>
    </tr>
    <tr>
      <th>4</th>
      <td>US</td>
      <td>HI</td>
    </tr>
    <tr>
      <th>5</th>
      <td>US</td>
      <td>HI</td>
    </tr>
    <tr>
      <th>6</th>
      <td>US</td>
      <td>HI</td>
    </tr>
    <tr>
      <th>7</th>
      <td>US</td>
      <td>HI</td>
    </tr>
    <tr>
      <th>8</th>
      <td>US</td>
      <td>HI</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Concatenating the two pd.series
stat_info_merge = pd.concat([stat_info[1], stat_info_st[[0,1]]], axis=1)
```


```python
stat_info_merge
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>1</th>
      <th>0</th>
      <th>1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>WAIKIKI 717.2</td>
      <td>US</td>
      <td>HI</td>
    </tr>
    <tr>
      <th>1</th>
      <td>KANEOHE 838.1</td>
      <td>US</td>
      <td>HI</td>
    </tr>
    <tr>
      <th>2</th>
      <td>KUALOA RANCH HEADQUARTERS 886.9</td>
      <td>US</td>
      <td>HI</td>
    </tr>
    <tr>
      <th>3</th>
      <td>PEARL CITY</td>
      <td>US</td>
      <td>HI</td>
    </tr>
    <tr>
      <th>4</th>
      <td>UPPER WAHIAWA 874.3</td>
      <td>US</td>
      <td>HI</td>
    </tr>
    <tr>
      <th>5</th>
      <td>WAIMANALO EXPERIMENTAL FARM</td>
      <td>US</td>
      <td>HI</td>
    </tr>
    <tr>
      <th>6</th>
      <td>WAIHEE 837.5</td>
      <td>US</td>
      <td>HI</td>
    </tr>
    <tr>
      <th>7</th>
      <td>HONOLULU OBSERVATORY 702.2</td>
      <td>US</td>
      <td>HI</td>
    </tr>
    <tr>
      <th>8</th>
      <td>MANOA LYON ARBO 785.2</td>
      <td>US</td>
      <td>HI</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Concatenating the two pd.series with a pd.DataFrame
clean_stations = pd.concat([stations, stat_info_merge], axis=1)
```


```python
clean_stations
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>station</th>
      <th>name</th>
      <th>latitude</th>
      <th>longitude</th>
      <th>elevation</th>
      <th>1</th>
      <th>0</th>
      <th>1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>USC00519397</td>
      <td>WAIKIKI 717.2, HI US</td>
      <td>21.27160</td>
      <td>-157.81680</td>
      <td>3.0</td>
      <td>WAIKIKI 717.2</td>
      <td>US</td>
      <td>HI</td>
    </tr>
    <tr>
      <th>1</th>
      <td>USC00513117</td>
      <td>KANEOHE 838.1, HI US</td>
      <td>21.42340</td>
      <td>-157.80150</td>
      <td>14.6</td>
      <td>KANEOHE 838.1</td>
      <td>US</td>
      <td>HI</td>
    </tr>
    <tr>
      <th>2</th>
      <td>USC00514830</td>
      <td>KUALOA RANCH HEADQUARTERS 886.9, HI US</td>
      <td>21.52130</td>
      <td>-157.83740</td>
      <td>7.0</td>
      <td>KUALOA RANCH HEADQUARTERS 886.9</td>
      <td>US</td>
      <td>HI</td>
    </tr>
    <tr>
      <th>3</th>
      <td>USC00517948</td>
      <td>PEARL CITY, HI US</td>
      <td>21.39340</td>
      <td>-157.97510</td>
      <td>11.9</td>
      <td>PEARL CITY</td>
      <td>US</td>
      <td>HI</td>
    </tr>
    <tr>
      <th>4</th>
      <td>USC00518838</td>
      <td>UPPER WAHIAWA 874.3, HI US</td>
      <td>21.49920</td>
      <td>-158.01110</td>
      <td>306.6</td>
      <td>UPPER WAHIAWA 874.3</td>
      <td>US</td>
      <td>HI</td>
    </tr>
    <tr>
      <th>5</th>
      <td>USC00519523</td>
      <td>WAIMANALO EXPERIMENTAL FARM, HI US</td>
      <td>21.33556</td>
      <td>-157.71139</td>
      <td>19.5</td>
      <td>WAIMANALO EXPERIMENTAL FARM</td>
      <td>US</td>
      <td>HI</td>
    </tr>
    <tr>
      <th>6</th>
      <td>USC00519281</td>
      <td>WAIHEE 837.5, HI US</td>
      <td>21.45167</td>
      <td>-157.84889</td>
      <td>32.9</td>
      <td>WAIHEE 837.5</td>
      <td>US</td>
      <td>HI</td>
    </tr>
    <tr>
      <th>7</th>
      <td>USC00511918</td>
      <td>HONOLULU OBSERVATORY 702.2, HI US</td>
      <td>21.31520</td>
      <td>-157.99920</td>
      <td>0.9</td>
      <td>HONOLULU OBSERVATORY 702.2</td>
      <td>US</td>
      <td>HI</td>
    </tr>
    <tr>
      <th>8</th>
      <td>USC00516128</td>
      <td>MANOA LYON ARBO 785.2, HI US</td>
      <td>21.33310</td>
      <td>-157.80250</td>
      <td>152.4</td>
      <td>MANOA LYON ARBO 785.2</td>
      <td>US</td>
      <td>HI</td>
    </tr>
  </tbody>
</table>
</div>




```python
clean_stations.drop(['name'], axis=1, inplace=True)
```


```python
# Neat way to rename columns and order appropriately
clean_stations.columns = ['station', 'latitude', 'longitude', 'elevation', 'name', 'country', 'state']
```


```python
# Finished clean df
clean_stations
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>station</th>
      <th>latitude</th>
      <th>longitude</th>
      <th>elevation</th>
      <th>name</th>
      <th>country</th>
      <th>state</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>USC00519397</td>
      <td>21.27160</td>
      <td>-157.81680</td>
      <td>3.0</td>
      <td>WAIKIKI 717.2</td>
      <td>US</td>
      <td>HI</td>
    </tr>
    <tr>
      <th>1</th>
      <td>USC00513117</td>
      <td>21.42340</td>
      <td>-157.80150</td>
      <td>14.6</td>
      <td>KANEOHE 838.1</td>
      <td>US</td>
      <td>HI</td>
    </tr>
    <tr>
      <th>2</th>
      <td>USC00514830</td>
      <td>21.52130</td>
      <td>-157.83740</td>
      <td>7.0</td>
      <td>KUALOA RANCH HEADQUARTERS 886.9</td>
      <td>US</td>
      <td>HI</td>
    </tr>
    <tr>
      <th>3</th>
      <td>USC00517948</td>
      <td>21.39340</td>
      <td>-157.97510</td>
      <td>11.9</td>
      <td>PEARL CITY</td>
      <td>US</td>
      <td>HI</td>
    </tr>
    <tr>
      <th>4</th>
      <td>USC00518838</td>
      <td>21.49920</td>
      <td>-158.01110</td>
      <td>306.6</td>
      <td>UPPER WAHIAWA 874.3</td>
      <td>US</td>
      <td>HI</td>
    </tr>
    <tr>
      <th>5</th>
      <td>USC00519523</td>
      <td>21.33556</td>
      <td>-157.71139</td>
      <td>19.5</td>
      <td>WAIMANALO EXPERIMENTAL FARM</td>
      <td>US</td>
      <td>HI</td>
    </tr>
    <tr>
      <th>6</th>
      <td>USC00519281</td>
      <td>21.45167</td>
      <td>-157.84889</td>
      <td>32.9</td>
      <td>WAIHEE 837.5</td>
      <td>US</td>
      <td>HI</td>
    </tr>
    <tr>
      <th>7</th>
      <td>USC00511918</td>
      <td>21.31520</td>
      <td>-157.99920</td>
      <td>0.9</td>
      <td>HONOLULU OBSERVATORY 702.2</td>
      <td>US</td>
      <td>HI</td>
    </tr>
    <tr>
      <th>8</th>
      <td>USC00516128</td>
      <td>21.33310</td>
      <td>-157.80250</td>
      <td>152.4</td>
      <td>MANOA LYON ARBO 785.2</td>
      <td>US</td>
      <td>HI</td>
    </tr>
  </tbody>
</table>
</div>




```python
clean_stations.to_csv('../clean_stations.csv', index=False)
```

### Data Analysis and implementing fixes - Measurement Data
***


```python
measure.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>station</th>
      <th>date</th>
      <th>prcp</th>
      <th>tobs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>USC00519397</td>
      <td>2010-01-01</td>
      <td>0.08</td>
      <td>65</td>
    </tr>
    <tr>
      <th>1</th>
      <td>USC00519397</td>
      <td>2010-01-02</td>
      <td>0.00</td>
      <td>63</td>
    </tr>
    <tr>
      <th>2</th>
      <td>USC00519397</td>
      <td>2010-01-03</td>
      <td>0.00</td>
      <td>74</td>
    </tr>
    <tr>
      <th>3</th>
      <td>USC00519397</td>
      <td>2010-01-04</td>
      <td>0.00</td>
      <td>76</td>
    </tr>
    <tr>
      <th>4</th>
      <td>USC00519397</td>
      <td>2010-01-06</td>
      <td>NaN</td>
      <td>73</td>
    </tr>
  </tbody>
</table>
</div>




```python
measure.tail()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>station</th>
      <th>date</th>
      <th>prcp</th>
      <th>tobs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>19545</th>
      <td>USC00516128</td>
      <td>2017-08-19</td>
      <td>0.09</td>
      <td>71</td>
    </tr>
    <tr>
      <th>19546</th>
      <td>USC00516128</td>
      <td>2017-08-20</td>
      <td>NaN</td>
      <td>78</td>
    </tr>
    <tr>
      <th>19547</th>
      <td>USC00516128</td>
      <td>2017-08-21</td>
      <td>0.56</td>
      <td>76</td>
    </tr>
    <tr>
      <th>19548</th>
      <td>USC00516128</td>
      <td>2017-08-22</td>
      <td>0.50</td>
      <td>76</td>
    </tr>
    <tr>
      <th>19549</th>
      <td>USC00516128</td>
      <td>2017-08-23</td>
      <td>0.45</td>
      <td>76</td>
    </tr>
  </tbody>
</table>
</div>




```python
measure.columns = ['station', 'date', 'precip', 'tobs']
```


```python
measure.dtypes
```




    station            object
    date       datetime64[ns]
    precip            float64
    tobs                int64
    dtype: object




```python
measure.describe()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>precip</th>
      <th>tobs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>18103.000000</td>
      <td>19550.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>0.160644</td>
      <td>73.097954</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.468746</td>
      <td>4.523527</td>
    </tr>
    <tr>
      <th>min</th>
      <td>0.000000</td>
      <td>53.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>0.000000</td>
      <td>70.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>0.010000</td>
      <td>73.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>0.110000</td>
      <td>76.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>11.530000</td>
      <td>87.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Info method shows the number of NaN records - more than 1400
# PD.read_csv command - parse_dates was used to convert date raw date into datetime format
measure.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 19550 entries, 0 to 19549
    Data columns (total 4 columns):
    station    19550 non-null object
    date       19550 non-null datetime64[ns]
    precip     18103 non-null float64
    tobs       19550 non-null int64
    dtypes: datetime64[ns](1), float64(1), int64(1), object(1)
    memory usage: 611.0+ KB



```python
# Creating a df of just the nullse
measure_nan = measure[measure.isnull().any(axis=1)]
```


```python
# Counting the number of null values
measure_nan.count()
```




    station    1447
    date       1447
    precip        0
    tobs       1447
    dtype: int64




```python
# Before replacing nulls with zero determine if a group of years has more or less nulls
measure_val_2010_to_2013 = measure_nan[(measure_nan['date'] > '2010-1-1') & (measure_nan['date'] <= '2013-12-31')]
```


```python
measure_val_2010_to_2013.count()
```




    station    637
    date       637
    precip       0
    tobs       637
    dtype: int64




```python
measure_val_2014_to_2017 = measure_nan[(measure_nan['date'] > '2014-1-1') & (measure_nan['date'] <= '2017-12-31')]
```


```python
# This analysis shows that there are more nulls in last four years
measure_val_2014_to_2017.count()
```




    station    810
    date       810
    precip       0
    tobs       810
    dtype: int64




```python
# Determine count per year to see what distribution of nulls looks like
measure_val_1_2010_to_12_2010 = measure_nan[(measure_nan['date'] > '2010-1-1') & (measure_nan['date'] <= '2010-12-31')]
measure_val_1_2011_to_12_2011 = measure_nan[(measure_nan['date'] > '2011-1-1') & (measure_nan['date'] <= '2011-12-31')]
measure_val_1_2012_to_12_2012 = measure_nan[(measure_nan['date'] > '2012-1-1') & (measure_nan['date'] <= '2012-12-31')]
measure_val_1_2013_to_12_2013 = measure_nan[(measure_nan['date'] > '2013-1-1') & (measure_nan['date'] <= '2013-12-31')]
measure_val_1_2014_to_12_2014 = measure_nan[(measure_nan['date'] > '2014-1-1') & (measure_nan['date'] <= '2014-12-31')]
measure_val_1_2015_to_12_2015 = measure_nan[(measure_nan['date'] > '2015-1-1') & (measure_nan['date'] <= '2015-12-31')]
measure_val_1_2016_to_12_2016 = measure_nan[(measure_nan['date'] > '2016-1-1') & (measure_nan['date'] <= '2016-12-31')]
measure_val_1_2017_to_12_2017 = measure_nan[(measure_nan['date'] > '2017-1-1') & (measure_nan['date'] <= '2017-12-31')]
```


```python
count_2010 = measure_val_1_2010_to_12_2010.count()
count_2011 = measure_val_1_2011_to_12_2011.count()
count_2012 = measure_val_1_2012_to_12_2012.count()
count_2013 = measure_val_1_2013_to_12_2013.count()
count_2014 = measure_val_1_2014_to_12_2014.count()
count_2015 = measure_val_1_2015_to_12_2015.count()
count_2016 = measure_val_1_2016_to_12_2016.count()
count_2017 = measure_val_1_2017_to_12_2017.count()
```


```python
# 2010 and 2017 data shows the least number of null values
print(count_2010, count_2011, count_2012, count_2013, count_2014, count_2015, count_2016, count_2017)
```

    station    103
    date       103
    precip       0
    tobs       103
    dtype: int64 station    168
    date       168
    precip       0
    tobs       168
    dtype: int64 station    170
    date       170
    precip       0
    tobs       170
    dtype: int64 station    196
    date       196
    precip       0
    tobs       196
    dtype: int64 station    195
    date       195
    precip       0
    tobs       195
    dtype: int64 station    244
    date       244
    precip       0
    tobs       244
    dtype: int64 station    240
    date       240
    precip       0
    tobs       240
    dtype: int64 station    129
    date       129
    precip       0
    tobs       129
    dtype: int64



```python
# Replacing nulls with 0.
clean_measure = measure.fillna(0)
```


```python
clean_measure.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 19550 entries, 0 to 19549
    Data columns (total 4 columns):
    station    19550 non-null object
    date       19550 non-null datetime64[ns]
    precip     19550 non-null float64
    tobs       19550 non-null int64
    dtypes: datetime64[ns](1), float64(1), int64(1), object(1)
    memory usage: 611.0+ KB



```python
clean_measure.to_csv('../clean_measure.csv', index=False)
```
