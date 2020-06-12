# pandas操作
### 读取文件
- **读取csv**
```python
pd.read_csv(filepath_or_buffer,sep=',',header='infer',delimiter=None,names=None,index_col=None,dtype=None)
```
- **读取excel**
```python
pd.read_excel(filepath_or_buffer,header=0,skiprows=None)
```
- **读取html**
```python
pd.read_html(url,flavor=None, header=None, index_col=None, skiprows=None, attrs=None, parse_dates=False,encoding=None, decimal='.')
```
- **读取sql**
```python
pd.read_sql(sql, con, index_col=None, coerce_float=True, params=None, parse_dates=None, columns=None, chunksize=None)
# sql: sql query语句
# con: 数据库连接信息
```

***

### 查看DataFrame信息
- **查看前几行**	```df.head()```
- **查看行列**	```df.shape```
- **查看空缺**	```df.isnull().sum()```
- **查看基本统计学信息**	```df.describe()```

***

### DataFrame操作
- **排序**	```df.sort_values([val1,val2])``````df.sort_index([ind1,ind2])```
- **set_index**	```df.set_index([ind1,ind2])```
- **reset_index**	```df.reset_index(drop=False) #drop:是否删除index的数据```
- **loc/iloc** ```df.loc[list1,list2]``` ```df.iloc[list1,list2]```
- **pivot_table**	```df.pivot_table(values,index,columns,fill_values=0)```

***

### 缺失值处理
- **找到缺失值**	```df.isna().any()```	```df.isna().sum()```
- **删除含有缺失值的数据** ```df.dropna()```
- **填充缺失值** ```df.fillna(method)```

***

### 统计特征
- **均值** ```df[columns].mean(axis=None)```
- **中位数** ```df[columns].median(axis=None)```
- **最大/最小值**	```df[columns].min()/max()```
- **agg函数** ```df[columns].agg(myfunc_list)```
- **累计函数** ```df.cumsum()/cummax()/cummin()/cumprod()```
- **去除重复值** ```df.drop_duplicates(col_list)```
- **统计计数**	```df[columns].value_counts(normalize=False,sort=descending)```
- **groupby** ```df.groupby(column)```

### 合并两个DateFrame
- **append**	```df1.append(df2)``` 前后拼接
- **concat**	```pd.concat([df1, df2]) ``` 前后拼接/左右拼接；仅限对于index的inner join 和outer join
- **merge**	```df1.join(df2)``` inner/outer/left/right join 对于index
- **join**	```pd.merge([df1, df2])``` inner/outer/left/right join 对于指定列