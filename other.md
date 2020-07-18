### 从文件读取data

```python
# loadtxt: 最基础读取file的方法，所有表格一种dtype
np.loadtxt(file, delimiter='\t', dtype='', skiprows=1, usecols=[])
# genfromtxt/recfromcsv: 自动识别表格中各列的dtype
np.genfromtxt(file, delimiter=',', names=True, dtype=None)
np.recfromcsv(file,delimiter=',',names=True, dtype=None)
```

### 读取sas文件/dta文件/hdf5/matlab文件
- **SAS**

```python
from sas7bdat import SAS7BDAT
filename = ''
with SAS7BDAT(file_name) as file:
    df_sas = file.to_data_frame()
```

- **DTA**

```python
df = pd.read_stata('disarea.dta')
```

- **HDF5**

```python
import h5py
file = ''
data = h5py.File(file, 'r') # type: dict

```
- **matlab**

```python
import scipy.io
mat = scipy.io.loadmat('albeck_gene_expression.mat') # type: dict
```

### 从SQL读取data

```python
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('sqlite:///Chinook.sqlite')

# Open engine connection: con
con = engine.connect()

# Perform query: rs
rs = con.execute('select * from Album')

# Save results of the query to DataFrame: df
df = pd.DataFrame(rs.fetchall()/rs.fetchmany(n=))

# Close connection
con.close()

# Print head of DataFrame df
print(df.head())
```

```python
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

df = pd.read_sql_query('select * from Album', engine)
```

### 从网页读取data

- **美丽汤读取网页**

```python
import requests
from bs4 import BeautifulSoup
url = ''
r = requests.get()
txt = r.text
soup = BeautifulSoup(txt)

soup.title
soup.get_text()
soup.find_all('')
```

- **读取json API**

```python
import requests
url = ''
r = requests.get()
txt = r.text
json_data = r.json()
```
