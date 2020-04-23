import FundamentalAnalysis as fa
import pandas as pd
import logging

def get_methods(object, spacing=20): 
  methodList = [] 
  for method_name in dir(object): 
    try: 
        if callable(getattr(object, method_name)): 
            methodList.append(str(method_name)) 
    except: 
        methodList.append(str(method_name)) 
  processFunc = (lambda s: ' '.join(s.split())) or (lambda s: s) 
  for method in methodList: 
    try: 
        print(str(method.ljust(spacing)) + ' ' + 
              processFunc(str(getattr(object, method).__doc__)[0:90])) 
    except: 
        print(method.ljust(spacing) + ' ' + ' getattr() failed') 

def format(x):
  #Cast as a float for now, this will need error checking later
  try:
  	x = float(x)
  	x = "${:.1f}K".format(x/1000)
  except ValueError:
  	#Do nothing
  	logging.info("Value " + x + " doesn't need to be converted")
  return x

df = pd.DataFrame({'A':['A','B','C','D'],'B':[12355.00,12555.67,640.00,7000],'C':[155.00,145.67,600.0,990]})



#df['C'] = df['C'].apply(format)
i = 0
while i < len(df.columns):
	df[df.columns[i]] = df[df.columns[i]].apply(format)
	i = i + 1
#for col in df.columns:
	#get_methods(df[col])
	#df[col] = df[col].apply(format)


#drugInfo.rename(columns = {drugInfo.columns[1]: 'col_1_new_name'}, inplace = True)

#df = pd.DataFrame({'a':randn(5), 'b':randn(5), 'c':randn(5)})
#df.rename(columns={list(df)[1]:'col1_new_name'}, inplace=True)


print(df)