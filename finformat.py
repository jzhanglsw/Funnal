import pandas as pd
import logging

def format(x):
    #Cast as a float for now, this will need error checking later
    try:
        x = float(x)
        x = "${:.1f}K".format(x/1000)
    except ValueError:
        #Do nothing
        logging.info("Value " + x + " doesn't need to be converted")
    return x

    
def currency_format(df):
    i = 0
    while i < len(df.columns):
        df[df.columns[i]] = df[df.columns[i]].apply(format)
        i = i + 1
    return df