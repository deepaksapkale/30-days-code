Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:27:37) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> import numpy as np
>>> import datatime as dt
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    import datatime as dt
ImportError: No module named 'datatime'
>>> import datetime as dt
>>> data_source = r'c:\Python\test.xlsx'
>>> df = pd.read_excel(data_source)
Traceback (most recent call last):
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\io\excel.py", line 391, in __init__
    import xlrd
ImportError: No module named 'xlrd'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    df = pd.read_excel(data_source)
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\util\_decorators.py", line 188, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\util\_decorators.py", line 188, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\io\excel.py", line 350, in read_excel
    io = ExcelFile(io, engine=engine)
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\io\excel.py", line 653, in __init__
    self._reader = self._engines[engine](self._io)
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\io\excel.py", line 393, in __init__
    raise ImportError(err_msg)
ImportError: Install xlrd >= 1.0.0 for Excel support
>>> df = pd.read_excel(data_source)
>>> print(df.tail())
           Date        High         Low        Open       Close  Volume   Adj Close
4726 2019-07-18  271.700012  265.000000  271.700012  266.250000  212030  266.250000
4727 2019-07-19  269.000000  258.149994  268.000000  259.049988  222662  259.049988
4728 2019-07-22  265.250000  256.500000  259.049988  264.299988  177978  264.299988
4729 2019-07-23  266.750000  259.850006  266.750000  263.299988  121815  263.299988
4730 2019-07-24  263.600006  247.000000  263.250000  255.600006  383127  255.600006
>>> df = pd.read_excel(data_source, index_col = 'Date')
>>> print(df.tail())
                  High         Low        Open       Close  Volume   Adj Close
Date                                                                          
2019-07-18  271.700012  265.000000  271.700012  266.250000  212030  266.250000
2019-07-19  269.000000  258.149994  268.000000  259.049988  222662  259.049988
2019-07-22  265.250000  256.500000  259.049988  264.299988  177978  264.299988
2019-07-23  266.750000  259.850006  266.750000  263.299988  121815  263.299988
2019-07-24  263.600006  247.000000  263.250000  255.600006  383127  255.600006
>>> df.loc['2018-03-01','Volume']
417064.0
>>> ndayforward = 2
>>> df['day_chg']= df['close'.pct_change()] *100
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    df['day_chg']= df['close'.pct_change()] *100
AttributeError: 'str' object has no attribute 'pct_change'
>>> df['day_chg']= df['close'.pct_change()] *100
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    df['day_chg']= df['close'.pct_change()] *100
AttributeError: 'str' object has no attribute 'pct_change'
>>> df['day_chg'] = (df('close').pct_change()) * 100
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    df['day_chg'] = (df('close').pct_change()) * 100
TypeError: 'DataFrame' object is not callable
>>> print(df.tail())
                  High         Low        Open       Close  Volume   Adj Close
Date                                                                          
2019-07-18  271.700012  265.000000  271.700012  266.250000  212030  266.250000
2019-07-19  269.000000  258.149994  268.000000  259.049988  222662  259.049988
2019-07-22  265.250000  256.500000  259.049988  264.299988  177978  264.299988
2019-07-23  266.750000  259.850006  266.750000  263.299988  121815  263.299988
2019-07-24  263.600006  247.000000  263.250000  255.600006  383127  255.600006
>>> df('day_chg') = (df['close'].pct_change()) *100
SyntaxError: can't assign to function call
>>> df('day_chg') = (df['Close'].pct_change()) *100
SyntaxError: can't assign to function call
>>> df('day_chg') = (df['Close'].pct_change())
SyntaxError: can't assign to function call
>>> print(df.tail())
                  High         Low        Open       Close  Volume   Adj Close
Date                                                                          
2019-07-18  271.700012  265.000000  271.700012  266.250000  212030  266.250000
2019-07-19  269.000000  258.149994  268.000000  259.049988  222662  259.049988
2019-07-22  265.250000  256.500000  259.049988  264.299988  177978  264.299988
2019-07-23  266.750000  259.850006  266.750000  263.299988  121815  263.299988
2019-07-24  263.600006  247.000000  263.250000  255.600006  383127  255.600006
>>> ndayforwrd = 2
>>> df = pd.read_excel(data_source, index_col = 'Date')
>>> ndayforward = 2
>>> df['day_chg'] = (df['close',pct_change()) * 100
		 
SyntaxError: invalid syntax
>>> df['day_chg'] = (df['close',pct_change() * 100
print(df.tail())
		    
SyntaxError: invalid syntax
>>> df['day_chg'] = (df['close',pct_change() * 100
		    )
		 
SyntaxError: invalid syntax
>>> df['day_chg'] (df['Close'].pct_change()) * 100
Traceback (most recent call last):
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\core\indexes\base.py", line 2657, in get_loc
    return self._engine.get_loc(key)
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'day_chg'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    df['day_chg'] (df['Close'].pct_change()) * 100
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\core\frame.py", line 2927, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\core\indexes\base.py", line 2659, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'day_chg'
>>> df['day_chg'] (df['Close'].pct_change()) * 100
Traceback (most recent call last):
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\core\indexes\base.py", line 2657, in get_loc
    return self._engine.get_loc(key)
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'day_chg'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    df['day_chg'] (df['Close'].pct_change()) * 100
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\core\frame.py", line 2927, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\core\indexes\base.py", line 2659, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'day_chg'
>>> df['day_chg'] (df['close'].pct_change()) * 100
Traceback (most recent call last):
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\core\indexes\base.py", line 2657, in get_loc
    return self._engine.get_loc(key)
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'day_chg'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    df['day_chg'] (df['close'].pct_change()) * 100
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\core\frame.py", line 2927, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\core\indexes\base.py", line 2659, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'day_chg'
>>> df['day_chg'] =(df['close'].pct_change()) * 100
Traceback (most recent call last):
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\core\indexes\base.py", line 2657, in get_loc
    return self._engine.get_loc(key)
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'close'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    df['day_chg'] =(df['close'].pct_change()) * 100
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\core\frame.py", line 2927, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\core\indexes\base.py", line 2659, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'close'
>>> df['day_chg'] =(df['Close'].pct_change()) * 100
>>> print (df.tail())
                  High         Low        Open       Close  Volume   Adj Close   day_chg
Date                                                                                    
2019-07-18  271.700012  265.000000  271.700012  266.250000  212030  266.250000 -2.041938
2019-07-19  269.000000  258.149994  268.000000  259.049988  222662  259.049988 -2.704230
2019-07-22  265.250000  256.500000  259.049988  264.299988  177978  264.299988  2.026636
2019-07-23  266.750000  259.850006  266.750000  263.299988  121815  263.299988 -0.378358
2019-07-24  263.600006  247.000000  263.250000  255.600006  383127  255.600006 -2.924414
>>> df['ndaychg'] = df['day_chf'].shift(-ndayforward)
Traceback (most recent call last):
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\core\indexes\base.py", line 2657, in get_loc
    return self._engine.get_loc(key)
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'day_chf'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    df['ndaychg'] = df['day_chf'].shift(-ndayforward)
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\core\frame.py", line 2927, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\core\indexes\base.py", line 2659, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'day_chf'
>>> df['ndaychg'] = df['day_chg'].shift(-ndayforward)
>>> df['ndaychg'] = df['day_chg'].shift(-ndayforward)
>>> print(df.tail())
                  High         Low        Open       Close  Volume   Adj Close   day_chg   ndaychg
Date                                                                                              
2019-07-18  271.700012  265.000000  271.700012  266.250000  212030  266.250000 -2.041938  2.026636
2019-07-19  269.000000  258.149994  268.000000  259.049988  222662  259.049988 -2.704230 -0.378358
2019-07-22  265.250000  256.500000  259.049988  264.299988  177978  264.299988  2.026636 -2.924414
2019-07-23  266.750000  259.850006  266.750000  263.299988  121815  263.299988 -0.378358       NaN
2019-07-24  263.600006  247.000000  263.250000  255.600006  383127  255.600006 -2.924414       NaN
>>> dcriteria = (df.index >= '1985-01-31') & (df.index <= dt.datetime.today())
>>> tcriteria = df['day_chg'] < - 1
>>> criteria = (dcriteria) & (tcriteria)
>>> print(df(criteria).tail())
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    print(df(criteria).tail())
TypeError: 'DataFrame' object is not callable
>>> print(df[criteria].tail())
                  High         Low        Open       Close  Volume   Adj Close   day_chg   ndaychg
Date                                                                                              
2019-07-08  267.200012  259.149994  263.899994  261.899994  204524  261.899994 -1.781361 -2.857693
2019-07-10  264.000000  252.149994  261.750000  254.949997  399494  254.949997 -2.857693  0.261785
2019-07-18  271.700012  265.000000  271.700012  266.250000  212030  266.250000 -2.041938  2.026636
2019-07-19  269.000000  258.149994  268.000000  259.049988  222662  259.049988 -2.704230 -0.378358
2019-07-24  263.600006  247.000000  263.250000  255.600006  383127  255.600006 -2.924414       NaN
>>> newstock = 'BO.JSWSTEEL'
>>> newstart = '2015-01-31'
>>> import datetime as newdt
>>> newend = dt.datetime.today()
>>> import pandas as newpd
>>> newpd.core.common.is_list_like = newpd.api.types.is_list_like
>>> import pandas_datareader as newweb
>>> df = newweb.DataReader(newstock,'yahoo', newstart,newend)
Traceback (most recent call last):
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas_datareader\yahoo\daily.py", line 133, in _read_one_data
    data = j['context']['dispatcher']['stores']['HistoricalPriceStore']
KeyError: 'HistoricalPriceStore'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    df = newweb.DataReader(newstock,'yahoo', newstart,newend)
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas_datareader\data.py", line 310, in DataReader
    session=session).read()
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas_datareader\base.py", line 210, in read
    params=self._get_params(self.symbols))
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas_datareader\yahoo\daily.py", line 136, in _read_one_data
    raise RemoteDataError(msg.format(symbol, self.__class__.__name__))
pandas_datareader._utils.RemoteDataError: No data fetched for symbol BO.JSWSTEEL using YahooDailyReader
>>> newstock = 'JSWSTEEL.BO'
>>> df = newweb.DataReader(newstock,'yahoo', newstart,newend)
>>> print(df.tail())
                  High         Low        Open       Close    Volume   Adj Close
Date                                                                            
2019-07-18  271.700012  265.000000  271.700012  266.250000  212030.0  266.250000
2019-07-19  269.000000  258.149994  268.000000  259.049988  222662.0  259.049988
2019-07-22  265.250000  256.500000  259.049988  264.299988  177978.0  264.299988
2019-07-23  266.750000  259.850006  266.750000  263.299988  121815.0  263.299988
2019-07-24  263.600006  247.000000  263.250000  255.100006  430876.0  255.100006
>>> df.tail()
                  High         Low        Open       Close    Volume   Adj Close
Date                                                                            
2019-07-18  271.700012  265.000000  271.700012  266.250000  212030.0  266.250000
2019-07-19  269.000000  258.149994  268.000000  259.049988  222662.0  259.049988
2019-07-22  265.250000  256.500000  259.049988  264.299988  177978.0  264.299988
2019-07-23  266.750000  259.850006  266.750000  263.299988  121815.0  263.299988
2019-07-24  263.600006  247.000000  263.250000  255.100006  430876.0  255.100006
>>> df.drop(columns = ('Close'), inplace = True)
>>> df.tail()
                  High         Low        Open    Volume   Adj Close
Date                                                                
2019-07-18  271.700012  265.000000  271.700012  212030.0  266.250000
2019-07-19  269.000000  258.149994  268.000000  222662.0  259.049988
2019-07-22  265.250000  256.500000  259.049988  177978.0  264.299988
2019-07-23  266.750000  259.850006  266.750000  121815.0  263.299988
2019-07-24  263.600006  247.000000  263.250000  430876.0  255.100006
>>> df.rename({'Adj Close'},axis=1, inplace=True)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    df.rename({'Adj Close'},axis=1, inplace=True)
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\util\_decorators.py", line 197, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\core\frame.py", line 4025, in rename
    return super(DataFrame, self).rename(**kwargs)
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\core\generic.py", line 1091, in rename
    level=level)
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\core\internals\managers.py", line 171, in rename_axis
    obj.set_axis(axis, _transform_index(self.axes[axis], mapper, level))
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\core\internals\managers.py", line 2004, in _transform_index
    items = [func(x) for x in index]
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\core\internals\managers.py", line 2004, in <listcomp>
    items = [func(x) for x in index]
TypeError: 'set' object is not callable
>>> df.rename({'Adj Close'},axis=1, inplace=True)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    df.rename({'Adj Close'},axis=1, inplace=True)
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\util\_decorators.py", line 197, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\core\frame.py", line 4025, in rename
    return super(DataFrame, self).rename(**kwargs)
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\core\generic.py", line 1091, in rename
    level=level)
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\core\internals\managers.py", line 171, in rename_axis
    obj.set_axis(axis, _transform_index(self.axes[axis], mapper, level))
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\core\internals\managers.py", line 2004, in _transform_index
    items = [func(x) for x in index]
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\core\internals\managers.py", line 2004, in <listcomp>
    items = [func(x) for x in index]
TypeError: 'set' object is not callable
>>> df.tail()
                  High         Low        Open    Volume   Adj Close
Date                                                                
2019-07-18  271.700012  265.000000  271.700012  212030.0  266.250000
2019-07-19  269.000000  258.149994  268.000000  222662.0  259.049988
2019-07-22  265.250000  256.500000  259.049988  177978.0  264.299988
2019-07-23  266.750000  259.850006  266.750000  121815.0  263.299988
2019-07-24  263.600006  247.000000  263.250000  430876.0  255.100006
>>> df.rename({'Adj Close';'Close'}, axis=1, inplace = True)
SyntaxError: invalid syntax
>>> df.rename({'Adj Close':'Close'}, axis=1, inplace = True)
>>> df.tail()
                  High         Low        Open    Volume       Close
Date                                                                
2019-07-18  271.700012  265.000000  271.700012  212030.0  266.250000
2019-07-19  269.000000  258.149994  268.000000  222662.0  259.049988
2019-07-22  265.250000  256.500000  259.049988  177978.0  264.299988
2019-07-23  266.750000  259.850006  266.750000  121815.0  263.299988
2019-07-24  263.600006  247.000000  263.250000  430876.0  255.100006
>>> df['daychf'] = df['Close'].pct_chang() * 100
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    df['daychf'] = df['Close'].pct_chang() * 100
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\core\generic.py", line 5067, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'Series' object has no attribute 'pct_chang'
>>> df['daychg'] = df['Close'].pct_chang() * 100
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    df['daychg'] = df['Close'].pct_chang() * 100
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\core\generic.py", line 5067, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'Series' object has no attribute 'pct_chang'
>>> df['daychg'] = df['Close'].pct_change() * 100
>>> df.tail()
                  High         Low        Open    Volume       Close    daychg
Date                                                                          
2019-07-18  271.700012  265.000000  271.700012  212030.0  266.250000 -2.041938
2019-07-19  269.000000  258.149994  268.000000  222662.0  259.049988 -2.704230
2019-07-22  265.250000  256.500000  259.049988  177978.0  264.299988  2.026636
2019-07-23  266.750000  259.850006  266.750000  121815.0  263.299988 -0.378358
2019-07-24  263.600006  247.000000  263.250000  430876.0  255.100006 -3.114311
>>> df.graph()
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    df.graph()
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\core\generic.py", line 5067, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'graph'
>>> df.plot(x ='Date', y='daychg', kind = 'scatter')
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    df.plot(x ='Date', y='daychg', kind = 'scatter')
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\plotting\_core.py", line 2942, in __call__
    sort_columns=sort_columns, **kwds)
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\plotting\_core.py", line 1973, in plot_frame
    **kwds)
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\plotting\_core.py", line 1740, in _plot
    kind=kind, **kwds)
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\plotting\_core.py", line 860, in __init__
    super(ScatterPlot, self).__init__(data, x, y, s=s, **kwargs)
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\plotting\_core.py", line 796, in __init__
    MPLPlot.__init__(self, data, **kwargs)
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\plotting\_core.py", line 98, in __init__
    _raise_if_no_mpl()
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\plotting\_core.py", line 48, in _raise_if_no_mpl
    raise ImportError("matplotlib is required for plotting.")
ImportError: matplotlib is required for plotting.
>>> df.plot(x ='Date', y='daychg', kind = 'scatter')
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    df.plot(x ='Date', y='daychg', kind = 'scatter')
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\plotting\_core.py", line 2942, in __call__
    sort_columns=sort_columns, **kwds)
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\plotting\_core.py", line 1973, in plot_frame
    **kwds)
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\plotting\_core.py", line 1740, in _plot
    kind=kind, **kwds)
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\plotting\_core.py", line 860, in __init__
    super(ScatterPlot, self).__init__(data, x, y, s=s, **kwargs)
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\plotting\_core.py", line 796, in __init__
    MPLPlot.__init__(self, data, **kwargs)
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\plotting\_core.py", line 98, in __init__
    _raise_if_no_mpl()
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\plotting\_core.py", line 48, in _raise_if_no_mpl
    raise ImportError("matplotlib is required for plotting.")
ImportError: matplotlib is required for plotting.
>>> import matplotlib as plot
>>> df.plot(x ='Date', y='daychg', kind = 'scatter')
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    df.plot(x ='Date', y='daychg', kind = 'scatter')
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\plotting\_core.py", line 2942, in __call__
    sort_columns=sort_columns, **kwds)
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\plotting\_core.py", line 1973, in plot_frame
    **kwds)
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\plotting\_core.py", line 1740, in _plot
    kind=kind, **kwds)
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\plotting\_core.py", line 860, in __init__
    super(ScatterPlot, self).__init__(data, x, y, s=s, **kwargs)
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\plotting\_core.py", line 796, in __init__
    MPLPlot.__init__(self, data, **kwargs)
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\plotting\_core.py", line 98, in __init__
    _raise_if_no_mpl()
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\plotting\_core.py", line 48, in _raise_if_no_mpl
    raise ImportError("matplotlib is required for plotting.")
ImportError: matplotlib is required for plotting.
>>> import pandas as pd
>>> import matplotlib as plot
>>> df.plot(x ='Date', y='daychg', kind = 'scatter')
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    df.plot(x ='Date', y='daychg', kind = 'scatter')
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\plotting\_core.py", line 2942, in __call__
    sort_columns=sort_columns, **kwds)
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\plotting\_core.py", line 1973, in plot_frame
    **kwds)
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\plotting\_core.py", line 1740, in _plot
    kind=kind, **kwds)
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\plotting\_core.py", line 860, in __init__
    super(ScatterPlot, self).__init__(data, x, y, s=s, **kwargs)
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\plotting\_core.py", line 796, in __init__
    MPLPlot.__init__(self, data, **kwargs)
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\plotting\_core.py", line 98, in __init__
    _raise_if_no_mpl()
  File "C:\Users\Eureka\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\plotting\_core.py", line 48, in _raise_if_no_mpl
    raise ImportError("matplotlib is required for plotting.")
import pandas as tum
 