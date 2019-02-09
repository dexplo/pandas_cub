
# How to use pandas_cub

The README.ipynb notebook will serve as the documentation and usage guide to pandas_cub.

## Installation

`pip install pandas-cub`

## What is pandas_cub?
pandas_cub is a simple data analysis library that emulates the functionality of the pandas library. The library is not meant for serious work. It was built as an assignment for one of Ted Petrou's Python classes. If you would like to complete the assignment on your own, visit [this repository][1]. There are about 40 steps and 100 tests that you must pass in order to rebuild the library. It is a good challenge and teaches you the fundamentals of how to build your own data analysis library.

## pandas_cub functionality

pandas_cub has limited functionality but is still capable of a wide variety of data analysis tasks.

* Subset selection with the brackets
* Arithmetic and comparison operators (+, -, <, !=, etc...)
* Aggregation of columns with most of the common functions (min, max, mean, median, etc...)
* Grouping via pivot tables
* String-only methods for columns containing strings
* Reading in simple comma-separated value files
* Several other methods


## pandas_cub DataFrame

pandas_cub has a single main object, the DataFrame, to hold all of the data. The DataFrame is capable of holding 4 data types - booleans, integers, floats, and strings. All data is stored in NumPy arrays. panda_cub DataFrames have no index (as in pandas). The columns must be strings.

### Missing value representation
Boolean and integer columns will have no missing value representation. The NumPy NaN is used for float columns and the Python None is used for string columns.

## Code Examples

pandas_cub syntax is very similar to pandas, but implements much fewer methods. The below examples will cover just about all of the API.

[1]: https://github.com/tdpetrou/pandas_cub

### Reading data with `read_csv`

pandas_cub consists of a single function, `read_csv`, that has a single parameter, the location of the file you would like to read in as a DataFrame. This function can only handle simple CSV's and the delimiter must be a comma. A sample employee dataset is provided in the data directory. Notice that the visual output of the DataFrame is nearly identical to that of a pandas DataFrame. The `head` method returns the first 5 rows by default.


```python
import pandas_cub as pdc
```


```python
df = pdc.read_csv('data/employee.csv')
df.head()
```




<table><thead><tr><th></th><th>dept      </th><th>race      </th><th>gender    </th><th>salary    </th></tr></thead><tbody><tr><td><strong>0</strong></td><td>Houston Police Department-HPD</td><td>White     </td><td>Male      </td><td>     45279</td></tr><tr><td><strong>1</strong></td><td>Houston Fire Department (HFD)</td><td>White     </td><td>Male      </td><td>     63166</td></tr><tr><td><strong>2</strong></td><td>Houston Police Department-HPD</td><td>Black     </td><td>Male      </td><td>     66614</td></tr><tr><td><strong>3</strong></td><td>Public Works & Engineering-PWE</td><td>Asian     </td><td>Male      </td><td>     71680</td></tr><tr><td><strong>4</strong></td><td>Houston Airport System (HAS)</td><td>White     </td><td>Male      </td><td>     42390</td></tr></tbody></table>



### DataFrame properties

The `shape` property returns a tuple of the number of rows and columns


```python
df.shape
```




    (1535, 4)



The `len` function returns just the number of rows.


```python
len(df)
```




    1535



The `dtypes` property returns a DataFrame of the column names and their respective data type.


```python
df.dtypes
```




<table><thead><tr><th></th><th>Column Name</th><th>Data Type </th></tr></thead><tbody><tr><td><strong>0</strong></td><td>dept      </td><td>string    </td></tr><tr><td><strong>1</strong></td><td>race      </td><td>string    </td></tr><tr><td><strong>2</strong></td><td>gender    </td><td>string    </td></tr><tr><td><strong>3</strong></td><td>salary    </td><td>int       </td></tr></tbody></table>



The `columns` property returns a list of the columns.


```python
df.columns
```




    ['dept', 'race', 'gender', 'salary']



Set new columns by assigning the `columns` property to a list.


```python
df.columns = ['department', 'race', 'gender', 'salary']
df.head()
```




<table><thead><tr><th></th><th>department</th><th>race      </th><th>gender    </th><th>salary    </th></tr></thead><tbody><tr><td><strong>0</strong></td><td>Houston Police Department-HPD</td><td>White     </td><td>Male      </td><td>     45279</td></tr><tr><td><strong>1</strong></td><td>Houston Fire Department (HFD)</td><td>White     </td><td>Male      </td><td>     63166</td></tr><tr><td><strong>2</strong></td><td>Houston Police Department-HPD</td><td>Black     </td><td>Male      </td><td>     66614</td></tr><tr><td><strong>3</strong></td><td>Public Works & Engineering-PWE</td><td>Asian     </td><td>Male      </td><td>     71680</td></tr><tr><td><strong>4</strong></td><td>Houston Airport System (HAS)</td><td>White     </td><td>Male      </td><td>     42390</td></tr></tbody></table>



The `values` property returns a single numpy array of all the data.


```python
df.values
```




    array([['Houston Police Department-HPD', 'White', 'Male', 45279],
           ['Houston Fire Department (HFD)', 'White', 'Male', 63166],
           ['Houston Police Department-HPD', 'Black', 'Male', 66614],
           ...,
           ['Houston Police Department-HPD', 'White', 'Male', 43443],
           ['Houston Police Department-HPD', 'Asian', 'Male', 55461],
           ['Houston Fire Department (HFD)', 'Hispanic', 'Male', 51194]],
          dtype=object)



### Subset selection

Subset selection is handled with the brackets. To select a single column, place that column name in the brackets.


```python
df['race'].head()
```




<table><thead><tr><th></th><th>race      </th></tr></thead><tbody><tr><td><strong>0</strong></td><td>White     </td></tr><tr><td><strong>1</strong></td><td>White     </td></tr><tr><td><strong>2</strong></td><td>Black     </td></tr><tr><td><strong>3</strong></td><td>Asian     </td></tr><tr><td><strong>4</strong></td><td>White     </td></tr></tbody></table>



Select multiple columns with a list of strings.


```python
df[['race', 'salary']].head()
```




<table><thead><tr><th></th><th>race      </th><th>salary    </th></tr></thead><tbody><tr><td><strong>0</strong></td><td>White     </td><td>     45279</td></tr><tr><td><strong>1</strong></td><td>White     </td><td>     63166</td></tr><tr><td><strong>2</strong></td><td>Black     </td><td>     66614</td></tr><tr><td><strong>3</strong></td><td>Asian     </td><td>     71680</td></tr><tr><td><strong>4</strong></td><td>White     </td><td>     42390</td></tr></tbody></table>



Simultaneously select rows and columns by passing the brackets the row selection followed by the column selection separated by a comma. Here we use integers for rows and strings for columns.


```python
rows = [10, 50, 100]
cols = ['salary', 'race']
df[rows, cols]
```




<table><thead><tr><th></th><th>salary    </th><th>race      </th></tr></thead><tbody><tr><td><strong>0</strong></td><td>     77076</td><td>Black     </td></tr><tr><td><strong>1</strong></td><td>     81239</td><td>White     </td></tr><tr><td><strong>2</strong></td><td>     81239</td><td>White     </td></tr></tbody></table>



You can use integers for the columns as well.


```python
rows = [10, 50, 100]
cols = [2, 0]
df[rows, cols]
```




<table><thead><tr><th></th><th>gender    </th><th>department</th></tr></thead><tbody><tr><td><strong>0</strong></td><td>Male      </td><td>Houston Police Department-HPD</td></tr><tr><td><strong>1</strong></td><td>Male      </td><td>Houston Police Department-HPD</td></tr><tr><td><strong>2</strong></td><td>Male      </td><td>Houston Police Department-HPD</td></tr></tbody></table>



You can use a single integer and not just a list.


```python
df[99, 3]
```




<table><thead><tr><th></th><th>salary    </th></tr></thead><tbody><tr><td><strong>0</strong></td><td>     66614</td></tr></tbody></table>



Or a single string for the columns


```python
df[99, 'salary']
```




<table><thead><tr><th></th><th>salary    </th></tr></thead><tbody><tr><td><strong>0</strong></td><td>     66614</td></tr></tbody></table>



You can use a slice for the rows


```python
df[20:100:10, ['race', 'gender']]
```




<table><thead><tr><th></th><th>race      </th><th>gender    </th></tr></thead><tbody><tr><td><strong>0</strong></td><td>White     </td><td>Male      </td></tr><tr><td><strong>1</strong></td><td>White     </td><td>Male      </td></tr><tr><td><strong>2</strong></td><td>Hispanic  </td><td>Male      </td></tr><tr><td><strong>3</strong></td><td>White     </td><td>Male      </td></tr><tr><td><strong>4</strong></td><td>White     </td><td>Male      </td></tr><tr><td><strong>5</strong></td><td>Hispanic  </td><td>Male      </td></tr><tr><td><strong>6</strong></td><td>Hispanic  </td><td>Male      </td></tr><tr><td><strong>7</strong></td><td>Black     </td><td>Female    </td></tr></tbody></table>



You can also slice the columns with either integers or strings


```python
df[20:100:10, :2]
```




<table><thead><tr><th></th><th>department</th><th>race      </th></tr></thead><tbody><tr><td><strong>0</strong></td><td>Houston Police Department-HPD</td><td>White     </td></tr><tr><td><strong>1</strong></td><td>Houston Fire Department (HFD)</td><td>White     </td></tr><tr><td><strong>2</strong></td><td>Houston Police Department-HPD</td><td>Hispanic  </td></tr><tr><td><strong>3</strong></td><td>Houston Police Department-HPD</td><td>White     </td></tr><tr><td><strong>4</strong></td><td>Houston Fire Department (HFD)</td><td>White     </td></tr><tr><td><strong>5</strong></td><td>Houston Police Department-HPD</td><td>Hispanic  </td></tr><tr><td><strong>6</strong></td><td>Houston Fire Department (HFD)</td><td>Hispanic  </td></tr><tr><td><strong>7</strong></td><td>Houston Police Department-HPD</td><td>Black     </td></tr></tbody></table>




```python
df[20:100:10, 'department':'gender']
```




<table><thead><tr><th></th><th>department</th><th>race      </th><th>gender    </th></tr></thead><tbody><tr><td><strong>0</strong></td><td>Houston Police Department-HPD</td><td>White     </td><td>Male      </td></tr><tr><td><strong>1</strong></td><td>Houston Fire Department (HFD)</td><td>White     </td><td>Male      </td></tr><tr><td><strong>2</strong></td><td>Houston Police Department-HPD</td><td>Hispanic  </td><td>Male      </td></tr><tr><td><strong>3</strong></td><td>Houston Police Department-HPD</td><td>White     </td><td>Male      </td></tr><tr><td><strong>4</strong></td><td>Houston Fire Department (HFD)</td><td>White     </td><td>Male      </td></tr><tr><td><strong>5</strong></td><td>Houston Police Department-HPD</td><td>Hispanic  </td><td>Male      </td></tr><tr><td><strong>6</strong></td><td>Houston Fire Department (HFD)</td><td>Hispanic  </td><td>Male      </td></tr><tr><td><strong>7</strong></td><td>Houston Police Department-HPD</td><td>Black     </td><td>Female    </td></tr></tbody></table>



You can do boolean selection if you pass the brackets a one-column boolean DataFrame.


```python
filt = df['salary'] > 100000
filt.head()
```




<table><thead><tr><th></th><th>salary    </th></tr></thead><tbody><tr><td><strong>0</strong></td><td>False</td></tr><tr><td><strong>1</strong></td><td>False</td></tr><tr><td><strong>2</strong></td><td>False</td></tr><tr><td><strong>3</strong></td><td>False</td></tr><tr><td><strong>4</strong></td><td>False</td></tr></tbody></table>




```python
df[filt].head()
```




<table><thead><tr><th></th><th>department</th><th>race      </th><th>gender    </th><th>salary    </th></tr></thead><tbody><tr><td><strong>0</strong></td><td>Public Works & Engineering-PWE</td><td>White     </td><td>Male      </td><td>    107962</td></tr><tr><td><strong>1</strong></td><td>Health & Human Services</td><td>Black     </td><td>Male      </td><td>    180416</td></tr><tr><td><strong>2</strong></td><td>Houston Fire Department (HFD)</td><td>Hispanic  </td><td>Male      </td><td>    165216</td></tr><tr><td><strong>3</strong></td><td>Health & Human Services</td><td>White     </td><td>Female    </td><td>    100791</td></tr><tr><td><strong>4</strong></td><td>Houston Airport System (HAS)</td><td>White     </td><td>Male      </td><td>    120916</td></tr></tbody></table>




```python
df[filt, ['race', 'salary']].head()
```




<table><thead><tr><th></th><th>race      </th><th>salary    </th></tr></thead><tbody><tr><td><strong>0</strong></td><td>White     </td><td>    107962</td></tr><tr><td><strong>1</strong></td><td>Black     </td><td>    180416</td></tr><tr><td><strong>2</strong></td><td>Hispanic  </td><td>    165216</td></tr><tr><td><strong>3</strong></td><td>White     </td><td>    100791</td></tr><tr><td><strong>4</strong></td><td>White     </td><td>    120916</td></tr></tbody></table>



### Assigning Columns
You can only assign an entire new column or overwrite an old one. You cannot assign a subset of the data. You can assign a new column with a single value like this:


```python
df['bonus'] = 1000
df.head()
```




<table><thead><tr><th></th><th>department</th><th>race      </th><th>gender    </th><th>salary    </th><th>bonus     </th></tr></thead><tbody><tr><td><strong>0</strong></td><td>Houston Police Department-HPD</td><td>White     </td><td>Male      </td><td>     45279</td><td>      1000</td></tr><tr><td><strong>1</strong></td><td>Houston Fire Department (HFD)</td><td>White     </td><td>Male      </td><td>     63166</td><td>      1000</td></tr><tr><td><strong>2</strong></td><td>Houston Police Department-HPD</td><td>Black     </td><td>Male      </td><td>     66614</td><td>      1000</td></tr><tr><td><strong>3</strong></td><td>Public Works & Engineering-PWE</td><td>Asian     </td><td>Male      </td><td>     71680</td><td>      1000</td></tr><tr><td><strong>4</strong></td><td>Houston Airport System (HAS)</td><td>White     </td><td>Male      </td><td>     42390</td><td>      1000</td></tr></tbody></table>



You can assign with a numpy array the same length as a column.


```python
import numpy as np
df['bonus'] = np.random.randint(100, 5000, len(df))
df.head()
```




<table><thead><tr><th></th><th>department</th><th>race      </th><th>gender    </th><th>salary    </th><th>bonus     </th></tr></thead><tbody><tr><td><strong>0</strong></td><td>Houston Police Department-HPD</td><td>White     </td><td>Male      </td><td>     45279</td><td>      3536</td></tr><tr><td><strong>1</strong></td><td>Houston Fire Department (HFD)</td><td>White     </td><td>Male      </td><td>     63166</td><td>      1296</td></tr><tr><td><strong>2</strong></td><td>Houston Police Department-HPD</td><td>Black     </td><td>Male      </td><td>     66614</td><td>       511</td></tr><tr><td><strong>3</strong></td><td>Public Works & Engineering-PWE</td><td>Asian     </td><td>Male      </td><td>     71680</td><td>      4267</td></tr><tr><td><strong>4</strong></td><td>Houston Airport System (HAS)</td><td>White     </td><td>Male      </td><td>     42390</td><td>      3766</td></tr></tbody></table>



You can assign a new column with a one column DataFrame.


```python
df['salary'] + df['bonus']
```




<table><thead><tr><th></th><th>salary    </th></tr></thead><tbody><tr><td><strong>0</strong></td><td>     48815</td></tr><tr><td><strong>1</strong></td><td>     64462</td></tr><tr><td><strong>2</strong></td><td>     67125</td></tr><tr><td><strong>3</strong></td><td>     75947</td></tr><tr><td><strong>4</strong></td><td>     46156</td></tr><tr><td><strong>5</strong></td><td>    110001</td></tr><tr><td><strong>6</strong></td><td>     53738</td></tr><tr><td><strong>7</strong></td><td>    185348</td></tr><tr><td><strong>8</strong></td><td>     32575</td></tr><tr><td><strong>9</strong></td><td>     57918</td></tr><tr><strong><td>...</td></strong><td>...</td></tr><tr><td><strong>1525</strong></td><td>     32936</td></tr><tr><td><strong>1526</strong></td><td>     49294</td></tr><tr><td><strong>1527</strong></td><td>     34218</td></tr><tr><td><strong>1528</strong></td><td>     82795</td></tr><tr><td><strong>1529</strong></td><td>    104900</td></tr><tr><td><strong>1530</strong></td><td>     46408</td></tr><tr><td><strong>1531</strong></td><td>     67050</td></tr><tr><td><strong>1532</strong></td><td>     47368</td></tr><tr><td><strong>1533</strong></td><td>     60013</td></tr><tr><td><strong>1534</strong></td><td>     52624</td></tr></tbody></table>




```python
df['total salary'] = df['salary'] + df['bonus']
df.head()
```




<table><thead><tr><th></th><th>department</th><th>race      </th><th>gender    </th><th>salary    </th><th>bonus     </th><th>total salary</th></tr></thead><tbody><tr><td><strong>0</strong></td><td>Houston Police Department-HPD</td><td>White     </td><td>Male      </td><td>     45279</td><td>      3536</td><td>     48815</td></tr><tr><td><strong>1</strong></td><td>Houston Fire Department (HFD)</td><td>White     </td><td>Male      </td><td>     63166</td><td>      1296</td><td>     64462</td></tr><tr><td><strong>2</strong></td><td>Houston Police Department-HPD</td><td>Black     </td><td>Male      </td><td>     66614</td><td>       511</td><td>     67125</td></tr><tr><td><strong>3</strong></td><td>Public Works & Engineering-PWE</td><td>Asian     </td><td>Male      </td><td>     71680</td><td>      4267</td><td>     75947</td></tr><tr><td><strong>4</strong></td><td>Houston Airport System (HAS)</td><td>White     </td><td>Male      </td><td>     42390</td><td>      3766</td><td>     46156</td></tr></tbody></table>



### Arithmetic and comparison operators


```python
df1 = df[['salary', 'bonus']] * 5
df1.head()
```




<table><thead><tr><th></th><th>salary    </th><th>bonus     </th></tr></thead><tbody><tr><td><strong>0</strong></td><td>    226395</td><td>     17680</td></tr><tr><td><strong>1</strong></td><td>    315830</td><td>      6480</td></tr><tr><td><strong>2</strong></td><td>    333070</td><td>      2555</td></tr><tr><td><strong>3</strong></td><td>    358400</td><td>     21335</td></tr><tr><td><strong>4</strong></td><td>    211950</td><td>     18830</td></tr></tbody></table>




```python
df1 = df[['salary', 'bonus']] > 100000
df1.head()
```




<table><thead><tr><th></th><th>salary    </th><th>bonus     </th></tr></thead><tbody><tr><td><strong>0</strong></td><td>False</td><td>False</td></tr><tr><td><strong>1</strong></td><td>False</td><td>False</td></tr><tr><td><strong>2</strong></td><td>False</td><td>False</td></tr><tr><td><strong>3</strong></td><td>False</td><td>False</td></tr><tr><td><strong>4</strong></td><td>False</td><td>False</td></tr></tbody></table>




```python
df1 = df['race'] == 'White'
df1.head()
```




<table><thead><tr><th></th><th>race      </th></tr></thead><tbody><tr><td><strong>0</strong></td><td>True</td></tr><tr><td><strong>1</strong></td><td>True</td></tr><tr><td><strong>2</strong></td><td>False</td></tr><tr><td><strong>3</strong></td><td>False</td></tr><tr><td><strong>4</strong></td><td>True</td></tr></tbody></table>



### Aggregation

Most of the common aggregation methods are available. They only work down the columns and not across the rows.


```python
df.min()
```




<table><thead><tr><th></th><th>department</th><th>race      </th><th>gender    </th><th>salary    </th><th>bonus     </th><th>total salary</th></tr></thead><tbody><tr><td><strong>0</strong></td><td>Health & Human Services</td><td>Asian     </td><td>Female    </td><td>     24960</td><td>       101</td><td>     25913</td></tr></tbody></table>



Columns that the aggregation does not work are dropped.


```python
df.mean()
```




<table><thead><tr><th></th><th>salary    </th><th>bonus     </th><th>total salary</th></tr></thead><tbody><tr><td><strong>0</strong></td><td> 56278.746</td><td>  2594.283</td><td> 58873.029</td></tr></tbody></table>




```python
df.argmax()
```




<table><thead><tr><th></th><th>department</th><th>race      </th><th>gender    </th><th>salary    </th><th>bonus     </th><th>total salary</th></tr></thead><tbody><tr><td><strong>0</strong></td><td>         3</td><td>         0</td><td>         0</td><td>       145</td><td>      1516</td><td>       145</td></tr></tbody></table>




```python
df['salary'].argmin()
```




<table><thead><tr><th></th><th>salary    </th></tr></thead><tbody><tr><td><strong>0</strong></td><td>       347</td></tr></tbody></table>



Check if all salaries are greater than 20000


```python
df1 = df['salary'] > 20000
df1.all()
```




<table><thead><tr><th></th><th>salary    </th></tr></thead><tbody><tr><td><strong>0</strong></td><td>True</td></tr></tbody></table>



Count the number of non-missing values


```python
df.count()
```




<table><thead><tr><th></th><th>department</th><th>race      </th><th>gender    </th><th>salary    </th><th>bonus     </th><th>total salary</th></tr></thead><tbody><tr><td><strong>0</strong></td><td>      1535</td><td>      1535</td><td>      1535</td><td>      1535</td><td>      1535</td><td>      1535</td></tr></tbody></table>



Get number of unique values.


```python
df.nunique()
```




<table><thead><tr><th></th><th>department</th><th>race      </th><th>gender    </th><th>salary    </th><th>bonus     </th><th>total salary</th></tr></thead><tbody><tr><td><strong>0</strong></td><td>         6</td><td>         5</td><td>         2</td><td>       548</td><td>      1318</td><td>      1524</td></tr></tbody></table>



### Non-Aggregating Methods
These are methods that do not return a single value.

Get the unique values of each column. The `unique` method returns a list of DataFrames containing the unique values for each column.


```python
dfs = df.unique()
```


```python
dfs[0]
```




<table><thead><tr><th></th><th>department</th></tr></thead><tbody><tr><td><strong>0</strong></td><td>Health & Human Services</td></tr><tr><td><strong>1</strong></td><td>Houston Airport System (HAS)</td></tr><tr><td><strong>2</strong></td><td>Houston Fire Department (HFD)</td></tr><tr><td><strong>3</strong></td><td>Houston Police Department-HPD</td></tr><tr><td><strong>4</strong></td><td>Parks & Recreation</td></tr><tr><td><strong>5</strong></td><td>Public Works & Engineering-PWE</td></tr></tbody></table>




```python
dfs[1]
```




<table><thead><tr><th></th><th>race      </th></tr></thead><tbody><tr><td><strong>0</strong></td><td>Asian     </td></tr><tr><td><strong>1</strong></td><td>Black     </td></tr><tr><td><strong>2</strong></td><td>Hispanic  </td></tr><tr><td><strong>3</strong></td><td>Native American</td></tr><tr><td><strong>4</strong></td><td>White     </td></tr></tbody></table>




```python
dfs[2]
```




<table><thead><tr><th></th><th>gender    </th></tr></thead><tbody><tr><td><strong>0</strong></td><td>Female    </td></tr><tr><td><strong>1</strong></td><td>Male      </td></tr></tbody></table>



Rename columns with a dictionary.


```python
df.rename({'department':'dept', 'bonus':'BONUS'}).head()
```




<table><thead><tr><th></th><th>dept      </th><th>race      </th><th>gender    </th><th>salary    </th><th>BONUS     </th><th>total salary</th></tr></thead><tbody><tr><td><strong>0</strong></td><td>Houston Police Department-HPD</td><td>White     </td><td>Male      </td><td>     45279</td><td>      3536</td><td>     48815</td></tr><tr><td><strong>1</strong></td><td>Houston Fire Department (HFD)</td><td>White     </td><td>Male      </td><td>     63166</td><td>      1296</td><td>     64462</td></tr><tr><td><strong>2</strong></td><td>Houston Police Department-HPD</td><td>Black     </td><td>Male      </td><td>     66614</td><td>       511</td><td>     67125</td></tr><tr><td><strong>3</strong></td><td>Public Works & Engineering-PWE</td><td>Asian     </td><td>Male      </td><td>     71680</td><td>      4267</td><td>     75947</td></tr><tr><td><strong>4</strong></td><td>Houston Airport System (HAS)</td><td>White     </td><td>Male      </td><td>     42390</td><td>      3766</td><td>     46156</td></tr></tbody></table>



Drop columns with a string or list of strings.


```python
df.drop('race').head()
```




<table><thead><tr><th></th><th>department</th><th>gender    </th><th>salary    </th><th>bonus     </th><th>total salary</th></tr></thead><tbody><tr><td><strong>0</strong></td><td>Houston Police Department-HPD</td><td>Male      </td><td>     45279</td><td>      3536</td><td>     48815</td></tr><tr><td><strong>1</strong></td><td>Houston Fire Department (HFD)</td><td>Male      </td><td>     63166</td><td>      1296</td><td>     64462</td></tr><tr><td><strong>2</strong></td><td>Houston Police Department-HPD</td><td>Male      </td><td>     66614</td><td>       511</td><td>     67125</td></tr><tr><td><strong>3</strong></td><td>Public Works & Engineering-PWE</td><td>Male      </td><td>     71680</td><td>      4267</td><td>     75947</td></tr><tr><td><strong>4</strong></td><td>Houston Airport System (HAS)</td><td>Male      </td><td>     42390</td><td>      3766</td><td>     46156</td></tr></tbody></table>




```python
df.drop(['race', 'gender']).head()
```




<table><thead><tr><th></th><th>department</th><th>salary    </th><th>bonus     </th><th>total salary</th></tr></thead><tbody><tr><td><strong>0</strong></td><td>Houston Police Department-HPD</td><td>     45279</td><td>      3536</td><td>     48815</td></tr><tr><td><strong>1</strong></td><td>Houston Fire Department (HFD)</td><td>     63166</td><td>      1296</td><td>     64462</td></tr><tr><td><strong>2</strong></td><td>Houston Police Department-HPD</td><td>     66614</td><td>       511</td><td>     67125</td></tr><tr><td><strong>3</strong></td><td>Public Works & Engineering-PWE</td><td>     71680</td><td>      4267</td><td>     75947</td></tr><tr><td><strong>4</strong></td><td>Houston Airport System (HAS)</td><td>     42390</td><td>      3766</td><td>     46156</td></tr></tbody></table>



### Non-aggregating methods that keep all columns
The next several methods are non-aggregating methods that return a DataFrame with the same exact shape as the original. They only work on boolean, integer and float columns and ignore string columns.

Absolute value


```python
df.abs().head()
```




<table><thead><tr><th></th><th>department</th><th>race      </th><th>gender    </th><th>salary    </th><th>bonus     </th><th>total salary</th></tr></thead><tbody><tr><td><strong>0</strong></td><td>Houston Police Department-HPD</td><td>White     </td><td>Male      </td><td>     45279</td><td>      3536</td><td>     48815</td></tr><tr><td><strong>1</strong></td><td>Houston Fire Department (HFD)</td><td>White     </td><td>Male      </td><td>     63166</td><td>      1296</td><td>     64462</td></tr><tr><td><strong>2</strong></td><td>Houston Police Department-HPD</td><td>Black     </td><td>Male      </td><td>     66614</td><td>       511</td><td>     67125</td></tr><tr><td><strong>3</strong></td><td>Public Works & Engineering-PWE</td><td>Asian     </td><td>Male      </td><td>     71680</td><td>      4267</td><td>     75947</td></tr><tr><td><strong>4</strong></td><td>Houston Airport System (HAS)</td><td>White     </td><td>Male      </td><td>     42390</td><td>      3766</td><td>     46156</td></tr></tbody></table>



Cumulative min, max, and sum


```python
df.cummax().head()
```




<table><thead><tr><th></th><th>department</th><th>race      </th><th>gender    </th><th>salary    </th><th>bonus     </th><th>total salary</th></tr></thead><tbody><tr><td><strong>0</strong></td><td>Houston Police Department-HPD</td><td>White     </td><td>Male      </td><td>     45279</td><td>      3536</td><td>     48815</td></tr><tr><td><strong>1</strong></td><td>Houston Fire Department (HFD)</td><td>White     </td><td>Male      </td><td>     63166</td><td>      3536</td><td>     64462</td></tr><tr><td><strong>2</strong></td><td>Houston Police Department-HPD</td><td>Black     </td><td>Male      </td><td>     66614</td><td>      3536</td><td>     67125</td></tr><tr><td><strong>3</strong></td><td>Public Works & Engineering-PWE</td><td>Asian     </td><td>Male      </td><td>     71680</td><td>      4267</td><td>     75947</td></tr><tr><td><strong>4</strong></td><td>Houston Airport System (HAS)</td><td>White     </td><td>Male      </td><td>     71680</td><td>      4267</td><td>     75947</td></tr></tbody></table>



Clip values to be within a range.


```python
df.clip(40000, 60000).head()
```




<table><thead><tr><th></th><th>department</th><th>race      </th><th>gender    </th><th>salary    </th><th>bonus     </th><th>total salary</th></tr></thead><tbody><tr><td><strong>0</strong></td><td>Houston Police Department-HPD</td><td>White     </td><td>Male      </td><td>     45279</td><td>     40000</td><td>     48815</td></tr><tr><td><strong>1</strong></td><td>Houston Fire Department (HFD)</td><td>White     </td><td>Male      </td><td>     60000</td><td>     40000</td><td>     60000</td></tr><tr><td><strong>2</strong></td><td>Houston Police Department-HPD</td><td>Black     </td><td>Male      </td><td>     60000</td><td>     40000</td><td>     60000</td></tr><tr><td><strong>3</strong></td><td>Public Works & Engineering-PWE</td><td>Asian     </td><td>Male      </td><td>     60000</td><td>     40000</td><td>     60000</td></tr><tr><td><strong>4</strong></td><td>Houston Airport System (HAS)</td><td>White     </td><td>Male      </td><td>     42390</td><td>     40000</td><td>     46156</td></tr></tbody></table>



Round numeric columns


```python
df.round(-3).head()
```




<table><thead><tr><th></th><th>department</th><th>race      </th><th>gender    </th><th>salary    </th><th>bonus     </th><th>total salary</th></tr></thead><tbody><tr><td><strong>0</strong></td><td>Houston Police Department-HPD</td><td>White     </td><td>Male      </td><td>     45000</td><td>      4000</td><td>     49000</td></tr><tr><td><strong>1</strong></td><td>Houston Fire Department (HFD)</td><td>White     </td><td>Male      </td><td>     63000</td><td>      1000</td><td>     64000</td></tr><tr><td><strong>2</strong></td><td>Houston Police Department-HPD</td><td>Black     </td><td>Male      </td><td>     67000</td><td>      1000</td><td>     67000</td></tr><tr><td><strong>3</strong></td><td>Public Works & Engineering-PWE</td><td>Asian     </td><td>Male      </td><td>     72000</td><td>      4000</td><td>     76000</td></tr><tr><td><strong>4</strong></td><td>Houston Airport System (HAS)</td><td>White     </td><td>Male      </td><td>     42000</td><td>      4000</td><td>     46000</td></tr></tbody></table>



Copy the DataFrame


```python
df.copy().head()
```




<table><thead><tr><th></th><th>department</th><th>race      </th><th>gender    </th><th>salary    </th><th>bonus     </th><th>total salary</th></tr></thead><tbody><tr><td><strong>0</strong></td><td>Houston Police Department-HPD</td><td>White     </td><td>Male      </td><td>     45279</td><td>      3536</td><td>     48815</td></tr><tr><td><strong>1</strong></td><td>Houston Fire Department (HFD)</td><td>White     </td><td>Male      </td><td>     63166</td><td>      1296</td><td>     64462</td></tr><tr><td><strong>2</strong></td><td>Houston Police Department-HPD</td><td>Black     </td><td>Male      </td><td>     66614</td><td>       511</td><td>     67125</td></tr><tr><td><strong>3</strong></td><td>Public Works & Engineering-PWE</td><td>Asian     </td><td>Male      </td><td>     71680</td><td>      4267</td><td>     75947</td></tr><tr><td><strong>4</strong></td><td>Houston Airport System (HAS)</td><td>White     </td><td>Male      </td><td>     42390</td><td>      3766</td><td>     46156</td></tr></tbody></table>



Take the nth difference.


```python
df.diff(2).head(10)
```




<table><thead><tr><th></th><th>department</th><th>race      </th><th>gender    </th><th>salary    </th><th>bonus     </th><th>total salary</th></tr></thead><tbody><tr><td><strong>0</strong></td><td>Houston Police Department-HPD</td><td>White     </td><td>Male      </td><td>       nan</td><td>       nan</td><td>       nan</td></tr><tr><td><strong>1</strong></td><td>Houston Fire Department (HFD)</td><td>White     </td><td>Male      </td><td>       nan</td><td>       nan</td><td>       nan</td></tr><tr><td><strong>2</strong></td><td>Houston Police Department-HPD</td><td>Black     </td><td>Male      </td><td> 21335.000</td><td> -3025.000</td><td> 18310.000</td></tr><tr><td><strong>3</strong></td><td>Public Works & Engineering-PWE</td><td>Asian     </td><td>Male      </td><td>  8514.000</td><td>  2971.000</td><td> 11485.000</td></tr><tr><td><strong>4</strong></td><td>Houston Airport System (HAS)</td><td>White     </td><td>Male      </td><td>-24224.000</td><td>  3255.000</td><td>-20969.000</td></tr><tr><td><strong>5</strong></td><td>Public Works & Engineering-PWE</td><td>White     </td><td>Male      </td><td> 36282.000</td><td> -2228.000</td><td> 34054.000</td></tr><tr><td><strong>6</strong></td><td>Houston Fire Department (HFD)</td><td>Hispanic  </td><td>Male      </td><td> 10254.000</td><td> -2672.000</td><td>  7582.000</td></tr><tr><td><strong>7</strong></td><td>Health & Human Services</td><td>Black     </td><td>Male      </td><td> 72454.000</td><td>  2893.000</td><td> 75347.000</td></tr><tr><td><strong>8</strong></td><td>Public Works & Engineering-PWE</td><td>Black     </td><td>Male      </td><td>-22297.000</td><td>  1134.000</td><td>-21163.000</td></tr><tr><td><strong>9</strong></td><td>Health & Human Services</td><td>Black     </td><td>Male      </td><td>-125147.000</td><td> -2283.000</td><td>-127430.000</td></tr></tbody></table>



Find the nth percentage change.


```python
df.pct_change(2).head(10)
```




<table><thead><tr><th></th><th>department</th><th>race      </th><th>gender    </th><th>salary    </th><th>bonus     </th><th>total salary</th></tr></thead><tbody><tr><td><strong>0</strong></td><td>Houston Police Department-HPD</td><td>White     </td><td>Male      </td><td>       nan</td><td>       nan</td><td>       nan</td></tr><tr><td><strong>1</strong></td><td>Houston Fire Department (HFD)</td><td>White     </td><td>Male      </td><td>       nan</td><td>       nan</td><td>       nan</td></tr><tr><td><strong>2</strong></td><td>Houston Police Department-HPD</td><td>Black     </td><td>Male      </td><td>     0.471</td><td>    -0.855</td><td>     0.375</td></tr><tr><td><strong>3</strong></td><td>Public Works & Engineering-PWE</td><td>Asian     </td><td>Male      </td><td>     0.135</td><td>     2.292</td><td>     0.178</td></tr><tr><td><strong>4</strong></td><td>Houston Airport System (HAS)</td><td>White     </td><td>Male      </td><td>    -0.364</td><td>     6.370</td><td>    -0.312</td></tr><tr><td><strong>5</strong></td><td>Public Works & Engineering-PWE</td><td>White     </td><td>Male      </td><td>     0.506</td><td>    -0.522</td><td>     0.448</td></tr><tr><td><strong>6</strong></td><td>Houston Fire Department (HFD)</td><td>Hispanic  </td><td>Male      </td><td>     0.242</td><td>    -0.710</td><td>     0.164</td></tr><tr><td><strong>7</strong></td><td>Health & Human Services</td><td>Black     </td><td>Male      </td><td>     0.671</td><td>     1.419</td><td>     0.685</td></tr><tr><td><strong>8</strong></td><td>Public Works & Engineering-PWE</td><td>Black     </td><td>Male      </td><td>    -0.424</td><td>     1.037</td><td>    -0.394</td></tr><tr><td><strong>9</strong></td><td>Health & Human Services</td><td>Black     </td><td>Male      </td><td>    -0.694</td><td>    -0.463</td><td>    -0.688</td></tr></tbody></table>



Sort the DataFrame by one or more columns


```python
df.sort_values('salary').head()
```




<table><thead><tr><th></th><th>department</th><th>race      </th><th>gender    </th><th>salary    </th><th>bonus     </th><th>total salary</th></tr></thead><tbody><tr><td><strong>0</strong></td><td>Houston Police Department-HPD</td><td>Black     </td><td>Female    </td><td>     24960</td><td>       953</td><td>     25913</td></tr><tr><td><strong>1</strong></td><td>Public Works & Engineering-PWE</td><td>Hispanic  </td><td>Male      </td><td>     26104</td><td>      4258</td><td>     30362</td></tr><tr><td><strong>2</strong></td><td>Public Works & Engineering-PWE</td><td>Black     </td><td>Female    </td><td>     26125</td><td>      3247</td><td>     29372</td></tr><tr><td><strong>3</strong></td><td>Houston Airport System (HAS)</td><td>Hispanic  </td><td>Female    </td><td>     26125</td><td>       832</td><td>     26957</td></tr><tr><td><strong>4</strong></td><td>Houston Airport System (HAS)</td><td>Black     </td><td>Female    </td><td>     26125</td><td>      2461</td><td>     28586</td></tr></tbody></table>



Sort descending


```python
df.sort_values('salary', asc=False).head()
```




<table><thead><tr><th></th><th>department</th><th>race      </th><th>gender    </th><th>salary    </th><th>bonus     </th><th>total salary</th></tr></thead><tbody><tr><td><strong>0</strong></td><td>Houston Fire Department (HFD)</td><td>White     </td><td>Male      </td><td>    210588</td><td>      3724</td><td>    214312</td></tr><tr><td><strong>1</strong></td><td>Houston Police Department-HPD</td><td>White     </td><td>Male      </td><td>    199596</td><td>       848</td><td>    200444</td></tr><tr><td><strong>2</strong></td><td>Houston Airport System (HAS)</td><td>Black     </td><td>Male      </td><td>    186192</td><td>      1778</td><td>    187970</td></tr><tr><td><strong>3</strong></td><td>Health & Human Services</td><td>Black     </td><td>Male      </td><td>    180416</td><td>      4932</td><td>    185348</td></tr><tr><td><strong>4</strong></td><td>Public Works & Engineering-PWE</td><td>White     </td><td>Female    </td><td>    178331</td><td>      2124</td><td>    180455</td></tr></tbody></table>



Sort by multiple columns


```python
df.sort_values(['race', 'salary']).head()
```




<table><thead><tr><th></th><th>department</th><th>race      </th><th>gender    </th><th>salary    </th><th>bonus     </th><th>total salary</th></tr></thead><tbody><tr><td><strong>0</strong></td><td>Houston Airport System (HAS)</td><td>Asian     </td><td>Female    </td><td>     26125</td><td>      4446</td><td>     30571</td></tr><tr><td><strong>1</strong></td><td>Houston Police Department-HPD</td><td>Asian     </td><td>Male      </td><td>     27914</td><td>      2855</td><td>     30769</td></tr><tr><td><strong>2</strong></td><td>Houston Police Department-HPD</td><td>Asian     </td><td>Male      </td><td>     28169</td><td>      2572</td><td>     30741</td></tr><tr><td><strong>3</strong></td><td>Public Works & Engineering-PWE</td><td>Asian     </td><td>Male      </td><td>     28995</td><td>      2874</td><td>     31869</td></tr><tr><td><strong>4</strong></td><td>Public Works & Engineering-PWE</td><td>Asian     </td><td>Male      </td><td>     30347</td><td>      4938</td><td>     35285</td></tr></tbody></table>



Randomly sample the DataFrame


```python
df.sample(n=3)
```




<table><thead><tr><th></th><th>department</th><th>race      </th><th>gender    </th><th>salary    </th><th>bonus     </th><th>total salary</th></tr></thead><tbody><tr><td><strong>0</strong></td><td>Houston Fire Department (HFD)</td><td>White     </td><td>Male      </td><td>     62540</td><td>      2995</td><td>     65535</td></tr><tr><td><strong>1</strong></td><td>Public Works & Engineering-PWE</td><td>White     </td><td>Male      </td><td>     63336</td><td>      1547</td><td>     64883</td></tr><tr><td><strong>2</strong></td><td>Houston Police Department-HPD</td><td>White     </td><td>Male      </td><td>     52514</td><td>      1150</td><td>     53664</td></tr></tbody></table>



Randomly sample a fraction


```python
df.sample(frac=.005)
```




<table><thead><tr><th></th><th>department</th><th>race      </th><th>gender    </th><th>salary    </th><th>bonus     </th><th>total salary</th></tr></thead><tbody><tr><td><strong>0</strong></td><td>Houston Police Department-HPD</td><td>Hispanic  </td><td>Female    </td><td>     60347</td><td>      1200</td><td>     61547</td></tr><tr><td><strong>1</strong></td><td>Public Works & Engineering-PWE</td><td>Black     </td><td>Male      </td><td>     49109</td><td>      3598</td><td>     52707</td></tr><tr><td><strong>2</strong></td><td>Health & Human Services</td><td>Black     </td><td>Female    </td><td>     48984</td><td>      4602</td><td>     53586</td></tr><tr><td><strong>3</strong></td><td>Houston Police Department-HPD</td><td>White     </td><td>Male      </td><td>     55461</td><td>      2813</td><td>     58274</td></tr><tr><td><strong>4</strong></td><td>Houston Airport System (HAS)</td><td>Black     </td><td>Female    </td><td>     29286</td><td>      1877</td><td>     31163</td></tr><tr><td><strong>5</strong></td><td>Houston Police Department-HPD</td><td>Asian     </td><td>Male      </td><td>     66614</td><td>      4480</td><td>     71094</td></tr><tr><td><strong>6</strong></td><td>Houston Fire Department (HFD)</td><td>White     </td><td>Male      </td><td>     28024</td><td>      4475</td><td>     32499</td></tr></tbody></table>



Sample with replacement


```python
df.sample(n=10000, replace=True).head()
```




<table><thead><tr><th></th><th>department</th><th>race      </th><th>gender    </th><th>salary    </th><th>bonus     </th><th>total salary</th></tr></thead><tbody><tr><td><strong>0</strong></td><td>Parks & Recreation</td><td>Black     </td><td>Female    </td><td>     31075</td><td>      1665</td><td>     32740</td></tr><tr><td><strong>1</strong></td><td>Public Works & Engineering-PWE</td><td>Hispanic  </td><td>Male      </td><td>     67038</td><td>       644</td><td>     67682</td></tr><tr><td><strong>2</strong></td><td>Houston Police Department-HPD</td><td>Black     </td><td>Male      </td><td>     37024</td><td>      1532</td><td>     38556</td></tr><tr><td><strong>3</strong></td><td>Health & Human Services</td><td>Black     </td><td>Female    </td><td>     57433</td><td>      3106</td><td>     60539</td></tr><tr><td><strong>4</strong></td><td>Public Works & Engineering-PWE</td><td>Black     </td><td>Male      </td><td>     53373</td><td>       924</td><td>     54297</td></tr></tbody></table>



### String-only methods

Use the `str` accessor to call methods available just to string columns. Pass the name of the string column as the first parameter for all these methods.


```python
df.str.count('department', 'P').head()
```




<table><thead><tr><th></th><th>department</th></tr></thead><tbody><tr><td><strong>0</strong></td><td>         2</td></tr><tr><td><strong>1</strong></td><td>         0</td></tr><tr><td><strong>2</strong></td><td>         2</td></tr><tr><td><strong>3</strong></td><td>         2</td></tr><tr><td><strong>4</strong></td><td>         0</td></tr></tbody></table>




```python
df.str.lower('department').head()
```




<table><thead><tr><th></th><th>department</th></tr></thead><tbody><tr><td><strong>0</strong></td><td>houston police department-hpd</td></tr><tr><td><strong>1</strong></td><td>houston fire department (hfd)</td></tr><tr><td><strong>2</strong></td><td>houston police department-hpd</td></tr><tr><td><strong>3</strong></td><td>public works & engineering-pwe</td></tr><tr><td><strong>4</strong></td><td>houston airport system (has)</td></tr></tbody></table>




```python
df.str.find('department', 'Houston').head()
```




<table><thead><tr><th></th><th>department</th></tr></thead><tbody><tr><td><strong>0</strong></td><td>         0</td></tr><tr><td><strong>1</strong></td><td>         0</td></tr><tr><td><strong>2</strong></td><td>         0</td></tr><tr><td><strong>3</strong></td><td>        -1</td></tr><tr><td><strong>4</strong></td><td>         0</td></tr></tbody></table>



### Grouping

pandas_cub provides the `value_counts` method for simple frequency counting of unique values and `pivot_table` for grouping and aggregating.

The `value_counts` method returns a list of DataFrames, one for each column.


```python
dfs = df[['department', 'race', 'gender']].value_counts()
```


```python
dfs[0]
```




<table><thead><tr><th></th><th>department</th><th>count     </th></tr></thead><tbody><tr><td><strong>0</strong></td><td>Houston Police Department-HPD</td><td>       570</td></tr><tr><td><strong>1</strong></td><td>Houston Fire Department (HFD)</td><td>       365</td></tr><tr><td><strong>2</strong></td><td>Public Works & Engineering-PWE</td><td>       341</td></tr><tr><td><strong>3</strong></td><td>Health & Human Services</td><td>       103</td></tr><tr><td><strong>4</strong></td><td>Houston Airport System (HAS)</td><td>       103</td></tr><tr><td><strong>5</strong></td><td>Parks & Recreation</td><td>        53</td></tr></tbody></table>




```python
dfs[1]
```




<table><thead><tr><th></th><th>race      </th><th>count     </th></tr></thead><tbody><tr><td><strong>0</strong></td><td>White     </td><td>       542</td></tr><tr><td><strong>1</strong></td><td>Black     </td><td>       518</td></tr><tr><td><strong>2</strong></td><td>Hispanic  </td><td>       381</td></tr><tr><td><strong>3</strong></td><td>Asian     </td><td>        87</td></tr><tr><td><strong>4</strong></td><td>Native American</td><td>         7</td></tr></tbody></table>




```python
dfs[2]
```




<table><thead><tr><th></th><th>gender    </th><th>count     </th></tr></thead><tbody><tr><td><strong>0</strong></td><td>Male      </td><td>      1135</td></tr><tr><td><strong>1</strong></td><td>Female    </td><td>       400</td></tr></tbody></table>



If your DataFrame has one column, a DataFrame and not a list is returned. You can also return the relative frequency by setting the `normalize` parameter to `True`.


```python
df['race'].value_counts(normalize=True)
```




<table><thead><tr><th></th><th>race      </th><th>count     </th></tr></thead><tbody><tr><td><strong>0</strong></td><td>White     </td><td>     0.353</td></tr><tr><td><strong>1</strong></td><td>Black     </td><td>     0.337</td></tr><tr><td><strong>2</strong></td><td>Hispanic  </td><td>     0.248</td></tr><tr><td><strong>3</strong></td><td>Asian     </td><td>     0.057</td></tr><tr><td><strong>4</strong></td><td>Native American</td><td>     0.005</td></tr></tbody></table>



The `pivot_table` method allows to group by one or two columns and aggregate values from another column. Let's find the average salary for each race and gender. All parameters must be strings.


```python
df.pivot_table(rows='race', columns='gender', values='salary', aggfunc='mean')
```




<table><thead><tr><th></th><th>race      </th><th>Female    </th><th>Male      </th></tr></thead><tbody><tr><td><strong>0</strong></td><td>Asian     </td><td> 58304.222</td><td> 60622.957</td></tr><tr><td><strong>1</strong></td><td>Black     </td><td> 48133.382</td><td> 51853.000</td></tr><tr><td><strong>2</strong></td><td>Hispanic  </td><td> 44216.960</td><td> 55493.064</td></tr><tr><td><strong>3</strong></td><td>Native American</td><td> 58844.333</td><td> 68850.500</td></tr><tr><td><strong>4</strong></td><td>White     </td><td> 66415.528</td><td> 63439.196</td></tr></tbody></table>



If you don't provide `values` or `aggfunc` then by default it will return frequency (a contingency table).


```python
df.pivot_table(rows='race', columns='gender')
```




<table><thead><tr><th></th><th>race      </th><th>Female    </th><th>Male      </th></tr></thead><tbody><tr><td><strong>0</strong></td><td>Asian     </td><td>        18</td><td>        69</td></tr><tr><td><strong>1</strong></td><td>Black     </td><td>       207</td><td>       311</td></tr><tr><td><strong>2</strong></td><td>Hispanic  </td><td>       100</td><td>       281</td></tr><tr><td><strong>3</strong></td><td>Native American</td><td>         3</td><td>         4</td></tr><tr><td><strong>4</strong></td><td>White     </td><td>        72</td><td>       470</td></tr></tbody></table>



You can group by just a single column.


```python
df.pivot_table(rows='department', values='salary', aggfunc='mean')
```




<table><thead><tr><th></th><th>department</th><th>mean      </th></tr></thead><tbody><tr><td><strong>0</strong></td><td>Health & Human Services</td><td> 51324.981</td></tr><tr><td><strong>1</strong></td><td>Houston Airport System (HAS)</td><td> 53990.369</td></tr><tr><td><strong>2</strong></td><td>Houston Fire Department (HFD)</td><td> 59960.441</td></tr><tr><td><strong>3</strong></td><td>Houston Police Department-HPD</td><td> 60428.746</td></tr><tr><td><strong>4</strong></td><td>Parks & Recreation</td><td> 39426.151</td></tr><tr><td><strong>5</strong></td><td>Public Works & Engineering-PWE</td><td> 50207.806</td></tr></tbody></table>




```python
df.pivot_table(columns='department', values='salary', aggfunc='mean')
```




<table><thead><tr><th></th><th>Health & Human Services</th><th>Houston Airport System (HAS)</th><th>Houston Fire Department (HFD)</th><th>Houston Police Department-HPD</th><th>Parks & Recreation</th><th>Public Works & Engineering-PWE</th></tr></thead><tbody><tr><td><strong>0</strong></td><td> 51324.981</td><td> 53990.369</td><td> 59960.441</td><td> 60428.746</td><td> 39426.151</td><td> 50207.806</td></tr></tbody></table>


