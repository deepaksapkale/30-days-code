Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:27:37) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import pandas_datareader.data as web
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import pandas_datareader.data as web
ImportError: No module named 'pandas_datareader'
>>> import pandas_datareader.data as web
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    import pandas_datareader.data as web
ImportError: No module named 'pandas_datareader'
>>> import pandas_datareader.data as web

>>> import datetime as dt
>>> start = dt.datetime(1985,1,29)
>>> end = dt.datetime.today()
>>> stock = 'JSWSTEEL.BO'
>>> df = web.DataREader(stock,'yahoo',start,end)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    df = web.DataREader(stock,'yahoo',start,end)
AttributeError: module 'pandas_datareader.data' has no attribute 'DataREader'
>>> df = web.DataReader(stock,'yahoo',start,end)
>>> print(df.head())
                 High      Low     Open      Close   Volume  Adj Close
Date                                                                  
2000-01-03  16.685699  15.2000  15.8857  16.685699  39200.0   1.948783
2000-01-04  16.799999  14.9714  15.4286  15.200000  26731.0   1.775263
2000-01-05  15.428600  13.7143  15.2000  14.857100  29269.0   1.735214
2000-01-06  16.000000  14.1714  14.8571  14.857100  39988.0   1.735214
2000-01-07  16.000000  13.1429  13.9429  14.628600  44888.0   1.708527
>>> stock = 'AVANTI.BO'
>>> df = web.DataReader(stock,'yahoo',start,end)
>>> print(df.head())
               High      Low     Open    Close   Volume  Adj Close
Date                                                              
2001-12-31  1.66333  1.63333  1.63333  1.63333   9000.0  -0.000377
2002-01-02  1.52000  1.37667  1.52000  1.37667  37500.0  -0.000318
2002-01-03  1.64667  1.26667  1.26667  1.50667  13500.0  -0.000348
2002-01-04  1.60000  1.59333  1.59333  1.60000   6000.0  -0.000369
2002-01-07  1.53333  1.53333  1.53333  1.53333  15000.0  -0.000354
>>> stock = 'JSWSTEEL.BO'
>>> print(df.head())
               High      Low     Open    Close   Volume  Adj Close
Date                                                              
2001-12-31  1.66333  1.63333  1.63333  1.63333   9000.0  -0.000377
2002-01-02  1.52000  1.37667  1.52000  1.37667  37500.0  -0.000318
2002-01-03  1.64667  1.26667  1.26667  1.50667  13500.0  -0.000348
2002-01-04  1.60000  1.59333  1.59333  1.60000   6000.0  -0.000369
2002-01-07  1.53333  1.53333  1.53333  1.53333  15000.0  -0.000354
>>> df = web.DataReader(stock,'yahoo',start,end)
>>> print(df.head())
                 High      Low     Open      Close   Volume  Adj Close
Date                                                                  
2000-01-03  16.685699  15.2000  15.8857  16.685699  39200.0   1.948783
2000-01-04  16.799999  14.9714  15.4286  15.200000  26731.0   1.775263
2000-01-05  15.428600  13.7143  15.2000  14.857100  29269.0   1.735214
2000-01-06  16.000000  14.1714  14.8571  14.857100  39988.0   1.735214
2000-01-07  16.000000  13.1429  13.9429  14.628600  44888.0   1.708527
>>> df = df.rename(columns ={'Adj Close':'close'})
>>> print(df.head())
                 High      Low     Open      Close   Volume     close
Date                                                                 
2000-01-03  16.685699  15.2000  15.8857  16.685699  39200.0  1.948783
2000-01-04  16.799999  14.9714  15.4286  15.200000  26731.0  1.775263
2000-01-05  15.428600  13.7143  15.2000  14.857100  29269.0  1.735214
2000-01-06  16.000000  14.1714  14.8571  14.857100  39988.0  1.735214
2000-01-07  16.000000  13.1429  13.9429  14.628600  44888.0  1.708527
>>> df = df.loc[:,['Open','High','Low','close','Volume']]
>>> print(df.tail())
                  Open        High         Low       close    Volume
Date                                                                
2019-07-18  271.700012  271.700012  265.000000  266.250000  212030.0
2019-07-19  268.000000  269.000000  258.149994  259.049988  222662.0
2019-07-22  259.049988  265.250000  256.500000  264.299988  177978.0
2019-07-23  266.750000  266.750000  259.850006  263.299988  121815.0
2019-07-24  263.250000  263.600006  247.000000  255.300003  368199.0
>>> print(df.tail())
                  Open        High         Low       close    Volume
Date                                                                
2019-07-18  271.700012  271.700012  265.000000  266.250000  212030.0
2019-07-19  268.000000  269.000000  258.149994  259.049988  222662.0
2019-07-22  259.049988  265.250000  256.500000  264.299988  177978.0
2019-07-23  266.750000  266.750000  259.850006  263.299988  121815.0
2019-07-24  263.250000  263.600006  247.000000  255.300003  368199.0
>>> print(df.tail())
                  Open        High         Low       close    Volume
Date                                                                
2019-07-18  271.700012  271.700012  265.000000  266.250000  212030.0
2019-07-19  268.000000  269.000000  258.149994  259.049988  222662.0
2019-07-22  259.049988  265.250000  256.500000  264.299988  177978.0
2019-07-23  266.750000  266.750000  259.850006  263.299988  121815.0
2019-07-24  263.250000  263.600006  247.000000  255.300003  368199.0
>>> print(df.tail())
                  Open        High         Low       close    Volume
Date                                                                
2019-07-18  271.700012  271.700012  265.000000  266.250000  212030.0
2019-07-19  268.000000  269.000000  258.149994  259.049988  222662.0
2019-07-22  259.049988  265.250000  256.500000  264.299988  177978.0
2019-07-23  266.750000  266.750000  259.850006  263.299988  121815.0
2019-07-24  263.250000  263.600006  247.000000  255.300003  368199.0
>>> print(df.tail())
                  Open        High         Low       close    Volume
Date                                                                
2019-07-18  271.700012  271.700012  265.000000  266.250000  212030.0
2019-07-19  268.000000  269.000000  258.149994  259.049988  222662.0
2019-07-22  259.049988  265.250000  256.500000  264.299988  177978.0
2019-07-23  266.750000  266.750000  259.850006  263.299988  121815.0
2019-07-24  263.250000  263.600006  247.000000  255.300003  368199.0
>>> print(df.tail())
                  Open        High         Low       close    Volume
Date                                                                
2019-07-18  271.700012  271.700012  265.000000  266.250000  212030.0
2019-07-19  268.000000  269.000000  258.149994  259.049988  222662.0
2019-07-22  259.049988  265.250000  256.500000  264.299988  177978.0
2019-07-23  266.750000  266.750000  259.850006  263.299988  121815.0
2019-07-24  263.250000  263.600006  247.000000  255.300003  368199.0
>>> print(df.tail())
                  Open        High         Low       close    Volume
Date                                                                
2019-07-18  271.700012  271.700012  265.000000  266.250000  212030.0
2019-07-19  268.000000  269.000000  258.149994  259.049988  222662.0
2019-07-22  259.049988  265.250000  256.500000  264.299988  177978.0
2019-07-23  266.750000  266.750000  259.850006  263.299988  121815.0
2019-07-24  263.250000  263.600006  247.000000  255.300003  368199.0
>>> df = web.DataReader(stock,'yahoo',start,end)
>>> print(df.tail())
                  High         Low        Open       Close    Volume   Adj Close
Date                                                                            
2019-07-18  271.700012  265.000000  271.700012  266.250000  212030.0  266.250000
2019-07-19  269.000000  258.149994  268.000000  259.049988  222662.0  259.049988
2019-07-22  265.250000  256.500000  259.049988  264.299988  177978.0  264.299988
2019-07-23  266.750000  259.850006  266.750000  263.299988  121815.0  263.299988
2019-07-24  263.600006  247.000000  263.250000  253.750000  370330.0  253.750000
>>> print(df.tail())
                  High         Low        Open       Close    Volume   Adj Close
Date                                                                            
2019-07-18  271.700012  265.000000  271.700012  266.250000  212030.0  266.250000
2019-07-19  269.000000  258.149994  268.000000  259.049988  222662.0  259.049988
2019-07-22  265.250000  256.500000  259.049988  264.299988  177978.0  264.299988
2019-07-23  266.750000  259.850006  266.750000  263.299988  121815.0  263.299988
2019-07-24  263.600006  247.000000  263.250000  253.750000  370330.0  253.750000
>>> print(df.tail())
                  High         Low        Open       Close    Volume   Adj Close
Date                                                                            
2019-07-18  271.700012  265.000000  271.700012  266.250000  212030.0  266.250000
2019-07-19  269.000000  258.149994  268.000000  259.049988  222662.0  259.049988
2019-07-22  265.250000  256.500000  259.049988  264.299988  177978.0  264.299988
2019-07-23  266.750000  259.850006  266.750000  263.299988  121815.0  263.299988
2019-07-24  263.600006  247.000000  263.250000  253.750000  370330.0  253.750000
>>> print(df.tail())
                  High         Low        Open       Close    Volume   Adj Close
Date                                                                            
2019-07-18  271.700012  265.000000  271.700012  266.250000  212030.0  266.250000
2019-07-19  269.000000  258.149994  268.000000  259.049988  222662.0  259.049988
2019-07-22  265.250000  256.500000  259.049988  264.299988  177978.0  264.299988
2019-07-23  266.750000  259.850006  266.750000  263.299988  121815.0  263.299988
2019-07-24  263.600006  247.000000  263.250000  253.750000  370330.0  253.750000
>>> print(df.tail())
                  High         Low        Open       Close    Volume   Adj Close
Date                                                                            
2019-07-18  271.700012  265.000000  271.700012  266.250000  212030.0  266.250000
2019-07-19  269.000000  258.149994  268.000000  259.049988  222662.0  259.049988
2019-07-22  265.250000  256.500000  259.049988  264.299988  177978.0  264.299988
2019-07-23  266.750000  259.850006  266.750000  263.299988  121815.0  263.299988
2019-07-24  263.600006  247.000000  263.250000  253.750000  370330.0  253.750000
>>> df = df.loc([:,'Open','High','Low','close','Volume'])
SyntaxError: invalid syntax
>>> df = df.loc[:,['Open','High','Low','close','Volume']]

Warning (from warnings module):
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\core\indexing.py", line 1494
    return self._getitem_tuple(key)
FutureWarning: 
Passing list-likes to .loc or [] with any missing label will raise
KeyError in the future, you can use .reindex() as an alternative.

See the documentation here:
https://pandas.pydata.org/pandas-docs/stable/indexing.html#deprecate-loc-reindex-listlike
>>> df = df.loc[:,['Open','High','Low','close','Volume']]
>>> print(df.tail())
                  Open        High         Low  close    Volume
Date                                                           
2019-07-18  271.700012  271.700012  265.000000    NaN  212030.0
2019-07-19  268.000000  269.000000  258.149994    NaN  222662.0
2019-07-22  259.049988  265.250000  256.500000    NaN  177978.0
2019-07-23  266.750000  266.750000  259.850006    NaN  121815.0
2019-07-24  263.250000  263.600006  247.000000    NaN  370330.0
>>> print(df.tail())
                  Open        High         Low  close    Volume
Date                                                           
2019-07-18  271.700012  271.700012  265.000000    NaN  212030.0
2019-07-19  268.000000  269.000000  258.149994    NaN  222662.0
2019-07-22  259.049988  265.250000  256.500000    NaN  177978.0
2019-07-23  266.750000  266.750000  259.850006    NaN  121815.0
2019-07-24  263.250000  263.600006  247.000000    NaN  370330.0
>>> df = web.DataReader(stock,'yahoo',start,end)
>>> print(df.tail())
                  High         Low        Open       Close    Volume   Adj Close
Date                                                                            
2019-07-18  271.700012  265.000000  271.700012  266.250000  212030.0  266.250000
2019-07-19  269.000000  258.149994  268.000000  259.049988  222662.0  259.049988
2019-07-22  265.250000  256.500000  259.049988  264.299988  177978.0  264.299988
2019-07-23  266.750000  259.850006  266.750000  263.299988  121815.0  263.299988
2019-07-24  263.600006  247.000000  263.250000  255.600006  383127.0  255.600006
>>> data_source = r'c:\python
SyntaxError: EOL while scanning string literal
>>> data_source = r'c:\python\jswsteel.xlx'
>>> data_source = r'c:\Python\jswsteel.xlx'
>>> import pandas as pd
>>> df.to_excel(data_source)
Traceback (most recent call last):
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\io\excel.py", line 1050, in __new__
    .format(ext=ext))
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\core\config.py", line 227, in __call__
    return self.__func__(*args, **kwds)
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\core\config.py", line 97, in _get_option
    key = _get_single_key(pat, silent)
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\core\config.py", line 83, in _get_single_key
    raise OptionError('No such keys(s): {pat!r}'.format(pat=pat))
pandas.core.config.OptionError: "No such keys(s): 'io.excel.xlx.writer'"

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    df.to_excel(data_source)
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\core\generic.py", line 2127, in to_excel
    engine=engine)
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\io\formats\excel.py", line 656, in write
    writer = ExcelWriter(_stringify_path(writer), engine=engine)
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\io\excel.py", line 1056, in __new__
    raise error
ValueError: No engine for filetype: 'xlx'
>>> data_source = r'c:\Python\jswsteel.xlss'
>>> data_source = r'c:\Python\jswsteel.xlsx'
>>> 
>>> df.to_excel(data_source)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    df.to_excel(data_source)
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\core\generic.py", line 2127, in to_excel
    engine=engine)
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\io\formats\excel.py", line 656, in write
    writer = ExcelWriter(_stringify_path(writer), engine=engine)
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\io\excel.py", line 1204, in __init__
    from openpyxl.workbook import Workbook
ImportError: No module named 'openpyxl'
>>> data_source - r'c:\Python\test.xlsx'
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    data_source - r'c:\Python\test.xlsx'
TypeError: unsupported operand type(s) for -: 'str' and 'str'
>>> data_source - r'c:\Python\test.xlsx'
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    data_source - r'c:\Python\test.xlsx'
TypeError: unsupported operand type(s) for -: 'str' and 'str'
>>> data_source = r'c:\Python\test.xlsx'
>>> import pandas as pd
>>> df.to_excel(data_source)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    df.to_excel(data_source)
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\core\generic.py", line 2127, in to_excel
    engine=engine)
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\io\formats\excel.py", line 656, in write
    writer = ExcelWriter(_stringify_path(writer), engine=engine)
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\io\excel.py", line 1204, in __init__
    from openpyxl.workbook import Workbook
ImportError: No module named 'openpyxl'
>>> df.to_excel(data_source)
>>> 
