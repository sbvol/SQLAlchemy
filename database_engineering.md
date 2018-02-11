
### Dependents
***


```python
import pandas as pd
```


```python
# Important to parse_dates on the 'date' column. Otherwise the dtype for that column will be loss on the read statement
stations = pd.read_csv('../clean_stations.csv')
measures = pd.read_csv('../clean_measure.csv')
```

### Ensure data loads
***


```python
# Printing the data
stations.head()
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
      <td>21.2716</td>
      <td>-157.8168</td>
      <td>3.0</td>
      <td>WAIKIKI 717.2</td>
      <td>US</td>
      <td>HI</td>
    </tr>
    <tr>
      <th>1</th>
      <td>USC00513117</td>
      <td>21.4234</td>
      <td>-157.8015</td>
      <td>14.6</td>
      <td>KANEOHE 838.1</td>
      <td>US</td>
      <td>HI</td>
    </tr>
    <tr>
      <th>2</th>
      <td>USC00514830</td>
      <td>21.5213</td>
      <td>-157.8374</td>
      <td>7.0</td>
      <td>KUALOA RANCH HEADQUARTERS 886.9</td>
      <td>US</td>
      <td>HI</td>
    </tr>
    <tr>
      <th>3</th>
      <td>USC00517948</td>
      <td>21.3934</td>
      <td>-157.9751</td>
      <td>11.9</td>
      <td>PEARL CITY</td>
      <td>US</td>
      <td>HI</td>
    </tr>
    <tr>
      <th>4</th>
      <td>USC00518838</td>
      <td>21.4992</td>
      <td>-158.0111</td>
      <td>306.6</td>
      <td>UPPER WAHIAWA 874.3</td>
      <td>US</td>
      <td>HI</td>
    </tr>
  </tbody>
</table>
</div>




```python
measures['date'] = pd.to_datetime(measures['date'])
```


```python
measures.dtypes
```




    station            object
    date       datetime64[ns]
    precip            float64
    tobs                int64
    dtype: object




```python
measures = measures[['station', 'precip', 'tobs', 'date']]
```


```python
measures.head()
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
      <th>precip</th>
      <th>tobs</th>
      <th>date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>USC00519397</td>
      <td>0.08</td>
      <td>65</td>
      <td>2010-01-01</td>
    </tr>
    <tr>
      <th>1</th>
      <td>USC00519397</td>
      <td>0.00</td>
      <td>63</td>
      <td>2010-01-02</td>
    </tr>
    <tr>
      <th>2</th>
      <td>USC00519397</td>
      <td>0.00</td>
      <td>74</td>
      <td>2010-01-03</td>
    </tr>
    <tr>
      <th>3</th>
      <td>USC00519397</td>
      <td>0.00</td>
      <td>76</td>
      <td>2010-01-04</td>
    </tr>
    <tr>
      <th>4</th>
      <td>USC00519397</td>
      <td>0.00</td>
      <td>73</td>
      <td>2010-01-06</td>
    </tr>
  </tbody>
</table>
</div>



### Database Creation
***


```python
# Importing all dependencies
import sqlalchemy
from sqlalchemy import create_engine, MetaData, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Numeric, Text, Float, DateTime
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
```


```python
# Create an engine to SQLite database call 'hawaii.sqlite'.
engine = create_engine("sqlite:///hawaii.sqlite")
```


```python
# Create a connection to the engine
conn = engine.connect()
```


```python
# Establishing the class/tables including column name, type, length
Base = declarative_base()

class Stations(Base):
    __tablename__ = 'stations'
    
    id = Column(Integer, primary_key=True)
    station = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    elevation = Column(Float)
    name = Column(String)
    country = Column(String)
    state = Column(String)
    
    def __repr__(self):
        return f"id={self.id}, name={self.name}"

class Measurements(Base):
    __tablename__ = 'measure'
    
    id = Column(Integer, primary_key=True)
    station = Column(String)
    precip = Column(Float)
    tobs = Column(Integer)
    date = Column(DateTime(30))
    
    def __repr__(self):
        return f"id={self.id}, name={self.name}"
```


```python
# Building the classes in the SQLite db
Base.metadata.create_all(engine)
```


```python
# Inpecting tables to ensure the create_all command worked
inspector = inspect(engine)
```


```python
inspector.get_table_names()
```




    ['measure', 'stations']




```python
# Converting the DataFrames into dictionaries
data_stations = stations.to_dict(orient='records')
```


```python
data_measures = measures.to_dict(orient='records')
```


```python
# Printing the dictionaries
print(data_stations[:5])
```

    [{'station': 'USC00519397', 'latitude': 21.2716, 'longitude': -157.8168, 'elevation': 3.0, 'name': 'WAIKIKI 717.2', 'country': 'US', 'state': 'HI'}, {'station': 'USC00513117', 'latitude': 21.4234, 'longitude': -157.8015, 'elevation': 14.6, 'name': 'KANEOHE 838.1', 'country': 'US', 'state': 'HI'}, {'station': 'USC00514830', 'latitude': 21.5213, 'longitude': -157.8374, 'elevation': 7.0, 'name': 'KUALOA RANCH HEADQUARTERS 886.9', 'country': 'US', 'state': 'HI'}, {'station': 'USC00517948', 'latitude': 21.3934, 'longitude': -157.9751, 'elevation': 11.9, 'name': 'PEARL CITY', 'country': 'US', 'state': 'HI'}, {'station': 'USC00518838', 'latitude': 21.4992, 'longitude': -158.0111, 'elevation': 306.6, 'name': 'UPPER WAHIAWA 874.3', 'country': 'US', 'state': 'HI'}]



```python
print(data_measures[:5])
```

    [{'station': 'USC00519397', 'precip': 0.08, 'tobs': 65, 'date': Timestamp('2010-01-01 00:00:00')}, {'station': 'USC00519397', 'precip': 0.0, 'tobs': 63, 'date': Timestamp('2010-01-02 00:00:00')}, {'station': 'USC00519397', 'precip': 0.0, 'tobs': 74, 'date': Timestamp('2010-01-03 00:00:00')}, {'station': 'USC00519397', 'precip': 0.0, 'tobs': 76, 'date': Timestamp('2010-01-04 00:00:00')}, {'station': 'USC00519397', 'precip': 0.0, 'tobs': 73, 'date': Timestamp('2010-01-06 00:00:00')}]



```python
metadata = MetaData(bind=engine)
metadata.reflect()
```


```python
table = sqlalchemy.Table('stations', metadata, autoload=True)
```


```python
conn.execute(table.delete())
```




    <sqlalchemy.engine.result.ResultProxy at 0x10b8f5dd8>




```python
# Inserting all of the records for station
conn.execute(table.insert(), data_stations)
```




    <sqlalchemy.engine.result.ResultProxy at 0x107cc6a58>




```python
# Executing a select statement on the Stations tables
conn.execute("SELECT * FROM stations LIMIT 5").fetchall()
```




    [(1, 'USC00519397', 21.2716, -157.8168, 3.0, 'WAIKIKI 717.2', 'US', 'HI'),
     (2, 'USC00513117', 21.4234, -157.8015, 14.6, 'KANEOHE 838.1', 'US', 'HI'),
     (3, 'USC00514830', 21.5213, -157.8374, 7.0, 'KUALOA RANCH HEADQUARTERS 886.9', 'US', 'HI'),
     (4, 'USC00517948', 21.3934, -157.9751, 11.9, 'PEARL CITY', 'US', 'HI'),
     (5, 'USC00518838', 21.4992, -158.0111, 306.6, 'UPPER WAHIAWA 874.3', 'US', 'HI')]




```python
metadata = MetaData(bind=engine)
metadata.reflect()
```


```python
# Building the tables in the SQLite db
table = sqlalchemy.Table('measure', metadata, autoload=True)
```


```python
# Clears the tables before inserting records
conn.execute(table.delete())
```




    <sqlalchemy.engine.result.ResultProxy at 0x10b8f59e8>




```python
# Inserting all of the records for measures
conn.execute(table.insert(), data_measures)
```




    <sqlalchemy.engine.result.ResultProxy at 0x10b8f5d30>




```python
# Executing a select statement on the Measurement table
conn.execute("SELECT * FROM measure LIMIT 10").fetchall()
```




    [(1, 'USC00519397', 0.08, 65, '2010-01-01 00:00:00.000000'),
     (2, 'USC00519397', 0.0, 63, '2010-01-02 00:00:00.000000'),
     (3, 'USC00519397', 0.0, 74, '2010-01-03 00:00:00.000000'),
     (4, 'USC00519397', 0.0, 76, '2010-01-04 00:00:00.000000'),
     (5, 'USC00519397', 0.0, 73, '2010-01-06 00:00:00.000000'),
     (6, 'USC00519397', 0.06, 70, '2010-01-07 00:00:00.000000'),
     (7, 'USC00519397', 0.0, 64, '2010-01-08 00:00:00.000000'),
     (8, 'USC00519397', 0.0, 68, '2010-01-09 00:00:00.000000'),
     (9, 'USC00519397', 0.0, 73, '2010-01-10 00:00:00.000000'),
     (10, 'USC00519397', 0.01, 64, '2010-01-11 00:00:00.000000')]


