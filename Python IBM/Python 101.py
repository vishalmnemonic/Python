print("Hello World")

# Comment

type(11)	Represents different types of data: int, float, str
type(11.2)
type("Hi")

int(1.2):1
float(1):1.0
int(True):1
bool(1):True

25/5:5.0
26//5:5

my_variable = 1
my_variable

x = 1 + 2 + 3
y = x + 5
y = y + 6

my = "Vishal"
my[0]:V
my[-1]:l
my[0:2]:Vi
my[::2]:"Vsa"
my[start:stop-1:gap]

len("Vishal")
concatenate using + symbol
my + "is my name"
3 * my
Strings are immutable, but can create a new string
\n represents a new line
\t represents a tab
\\ represents a \

Method:
A="I am the best"
B=A.replace('I am', 'She is')

A.find('am'):3
A.index('am'):3
A.find('z'):-1

# Python will try to run the code line-by-line, and it will stop if it runs into an error.

// for integer division

A="Thriller is the sixth studio album"
print("before upper:",A)
B=A.upper()
print("After upper:",B)

A="1"
B="2"
A+B="12"

Mod 2
Tuples are ordered sequence
Ratings=(10,9,8,7,6,5,4,3,2,1)
string, integer, float, tuple
Ratings[0]:10
They can be added to create bigger tupple
len(Ratings):10
Tupples are Immutable, must create a new tupple
RatingsSorted=sorted(Ratings)
Tuples can be nested
NT[1][2]
NT[4][2][1]

Lists, data structure, [], mutable
nesting
Can concatenate
Add 2 element L.extend([88,34])
Add 1 element L.append([88, 34])
del(L[0): Remove first element

String to List: "A,B,C,D".split(",")
Changing list will change its reference too, So do A=b[:]
help(python object)

Sets: type of collection, unordered, unique elements, {}, 
List to a set by set():Type casting
A.add("action"), A is a set
A.remove("action")
Action in A: False
Union of 2 sets: &
A.union(B)
A.issubset(B)

Dictionaries: Contains keys(label) and values
Keys are immutable and unique 
Values can be immutable, mutable and duplicates
{Key1:1, Key2:[2,3,3]}
DICT["Key1"]:1
DICT["Grad"]=1987
del(DICT[Key1])
Key1 in DICT:TRUE
DICT.keys()
DICT.values()

Mod3
Comparision operator
a=7
a==7
not equal: !=
if(age>18)
print("You can enter")
else: print("move on")

elif: alternate expression is checked

Logic Operators:
not(True):False
OR AND 

Range(1:5):1, 2, 3, 4

for i in range(0,5)
	square[i]="white"

newsquares=[]
i=0
while(squares[i]=='orange'):
newsquares.append(squares[i])
i=i+1

for year in dates:  
    print(year)  

functions: Len, sum, sorted, sort()

def add1(a):
"""add 1"""
b=a+1
return b
add(5):6

def nowork():
pass
return none

for index(i), variable(s) in enumerate(variable):
print(i, s)

squares=['red','yellow','green','purple','blue ']

for i,square in enumerate(squares):
    print(i,square)
	
dates = [1982,1980,1973,2000]

i=0;
year=0
while(year!=1973):
    year=dates[i]
    i=i+1
    print(year)
    
    
print("it took ", i ,"repetitions to get out of loop")

Global and Local variables

Data Types: int, float, string, list, dictionary, bool
Each is an object

x.reverse()

class circle(object):
def _init_(self, radius, color):
self.radius=radius;
self.color=color;

RedCircle=circle(5, "red")

def add_rad(self, r):
self.radius=self.radius + r

Redcircle.add_rad(2)

sort(): change the list, no new list is created

-----------------

file=open("dir/x.txt", "w")
file.name or file.mode

file.close()

with open("dir/x.txt", "r") as file1:
	filestuff=file1.read()
	filestuff2= file1.readlines()
	filestuff2= file1.readlines(5) #print first 5 characters
	print(filestuff)

with open("dir/x.txt", "w") as file1:
	file1.write("this is it")
	
Lines=["This is line A\n","This is line B\n","This is line C\n"]
Lines

with open('Example2.txt','w') as writefile:
    for line in Lines:
        print(line)
        writefile.write(line)

with open('Example2.txt','r') as testwritefile:
    print(testwritefile.read())

with open('Example2.txt','a') as testwritefile:
    testwritefile.write("This is line D\n")
with open('Example2.txt','r') as testwritefile:
    print(testwritefile.read())

with open('Example2.txt','r') as readfile:
    with open('Example3.txt','w') as writefile:
          for line in readfile:
                writefile.write(line)

Pandas: Numerical dictional
import pandas as pd
df=pd.read_csv(csv_path)

x=df[['Lenght']] #portion from another data frame
df.ix[0,0] #to access that cell
df.ix[1,'column name']
df.ix[0:2,0:2]

df["released"].unique()

df1=df[df["released"]>=1980]
df1. to_csv('new song.csv')

------------------
Numpy: Libraries for scientific computation
Array: Fixed length and of single type

import numpy as np
a=np.array([0,1,2,3,4])
type(a):numpy.ndarray
a.dtype:dtype('int64')
a.size:# of elements
a.ndim: dimention
a.shape:(5,):size of each dimention

c=np.array([20,1,2,3,4])
c[0]=100
d=c[0:2]

add, sub and multi are carried out element wise
mean_a=a.mean() avergae of all the elements in array
max_a=a.max()
np.pi ni.sin(x)
np.linespace(-2, 2, num=5)

x=np.linespace(0, 2*np.pi, 100)
y=np.sin(x)
import matplotlib.pyplot as plt
%matplotlib inline
plt.plot(x, y)

