import FundamentalAnalysis as fa
import pandas as pd

students = [ ('jack', 34, 'Sydeny') ,
('Riti', 30, 'Delhi' ) ,
('Aadi', 16, 'New York') ]
# Create a DataFrame object
dfObj = pd.DataFrame(students, columns = ['Name' , 'Age', 'City'], index=['a', 'b', 'c'])

students = [ ('jack', 34, 'Sydeny') ,
             ('Riti', 30, 'Delhi' ) ,
             ('Aadi', 16, 'New York') ]
 
# Create a DataFrame object
dfObj = pd.DataFrame(students, columns = ['Name' , 'Age', 'City'], index=['a', 'b', 'c'])

print(dfObj.head())

print(dfObj.describe())

print(list(dfObj.index))

print(list(dfObj.loc[ 'b' , : ]))

arr = [ 1, 2, 3, 4 ];

def isIncreasing(values):
    last = 0
    increasing = 0
    decreasing = 0
    analysis = ""
    for val in values:
        if val >= last:
            increasing += 1
        else:
            if val == 0:
                continue
            decreasing += 1
        last = val
    print(increasing)
    print(len(values))    
    if increasing > len(values)/2:
        analysis = "mostly increasing"
    if increasing == len(values):
        analysis = "strictly increasing"
    if decreasing > len(values)/2:
        analysis = "mostly decreasing"
    if decreasing == len(values):
        analysis = "strictly decreasing"
    return analysis
    
print("The test array is " + isIncreasing(arr))