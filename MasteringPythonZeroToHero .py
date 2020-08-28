#!/usr/bin/env python
# coding: utf-8

# # Some Useful Functions

# In[2]:


x = input("Please Enter a Number: ")
type(x)
x= int(x)
type(x)

b = float(input("Enter a Real Number :"))

get_ipython().run_line_magic('pinfo2', 'isinstance')

isinstance(x,int)
help(pow)


a = int(input("Enter First Number :"))
b = int(input("Enter Second Number :"))
if(a > b):
    print(a)
elif(b > a):
    print(b)
else:
    print("Both numbers are equal")


a = int(input("Enter Marks : "))
if a >= 85:
    print("Grade: A")
elif (a < 85) and (a >= 80):
    print("Grade: A-")
elif (a < 80) and (a >= 75):
    print("Grade: B")
elif (a < 75) and (a >= 70):
    print("Grade: B-")
else:
    print("Below Average Grades")

a = int(input("Enter a number : "))
if a > 10:
    print("Number is greater than 10")
    if a > 20:
        print("and also greater than 20")
    else:
        print("but not greater than 20")
print("Number is less than 10")


#Example Program
"""
User will enter floating point number say 238.793. Your task is to find integer portion before the point
and check that integer portion is even or not.
"""
a = float(input("Enter a floating point number"))
b = round(a)
if a >= 0:
    if b > a:
        integerportion = b-1
    else:
        integerportion = b
elif a < 0:
    if b < a:
        integerportion = b+1
    else:
        integerportion = b
if ((integerportion % 2) == 0):
    print("Number is even")
else:
    print("Number is odd")
print(integerportion)


# In[14]:


b = -343.65   # a way to find out integer portion of floating point number
c = int(b)
print(c)
type(c)


# # Loops
#  -While Loop

# In[2]:


# Print Even numbers
n = int(input("Enter Max Number : "))
i = 1
while (i <= n):
    if (i % 2 == 0):
        print("Even Numbers :",i)
    i += 1  
print ("Loop Done!")


# In[3]:


# Print Square
n = int(input("Enter Iterations : "))
i = 1
while(i <= n):
    print(i**2)
    print("This is iteration number : ", i)
    i += 1   # i = i+1
print("done")


# In[2]:


i = 1
while True:
    if i % 2 == 0:
        print("Break")
        break
    else:
        i += 1
        print(i)
        continue
    print("I am inside the loop")
print("Done!")


# In[3]:


i = 1
while True:
    if i != 10:
        x{} = int(input("Enter"))
        i += 1
        continue


# In[16]:


i = 1
while (i < 5):
    print("*"*i)
    i += 1
while (i > 0):
    print("*"*i)
    i -= 1 


# In[18]:


i = 1
while (i < 5):
    if(i % 2 != 0):
        print("*"*i)
    i += 1
while (i > 0):
    if(i % 2 != 0):
        print("*"*i)
    i -= 1 


# In[28]:


i = 7
while (i > 0):
    if(i % 2 != 0):
        print("1"*i)
    i -= 1 


# In[34]:


i = 1
j = 2
while (i >= 1):
    print(" "*j+"*"*i+" "*j)
    i = i+2
    j = j-1
    if (i>5):
        break
i = 3
j = 1
while (i >= 1):
    print(" "*j+"*"*i+" "*j)
    i = i-2
    j = j+1


# In[58]:


n = int(input("Please enter a number :"))
i = 1
j = int(n/2)
while (i >= 1):
    print(" "*j+"*"*i+" "*j)
    i = i+2
    j = j-1
    if (i>n):
        break
i = n-2
j = 1
while (i >= 1):
    print(" "*j+"*"*i+" "*j)
    i = i-2
    j = j+1


# In[68]:


n = int(input("Please enter a number :"))
i = 1
j = n
while (i >= 1):
    print(" "*j+"*"*i)
    i = i+1
    j = j-1
    if (i>n):
        break


# In[81]:


n = int(input("Enter number :"))
i = n
j = 1
while (i >= 1):
    print("1"*j+"0"*i+"1"*j)
    i = i-2
    j = j+1


# In[8]:


i = 5
j = 1
while (i >= 1):
    print(" "*j+"1"*i+" "*j)
    i = i-2
    j = j+1


# In[101]:


number = 5
spaces = 0
    
while (number > 0) :    
    string = ""
    k = 0
    while(k < spaces):
        string += " "
        k += 1
    i = 0
    while (i < number):
        if (i % 2 == 0):
            string += "1"
        else:
            string += "0"
        i += 1
    print(string)
    number -= 2
    spaces += 1


# In[27]:


number = 10
i = 1
while (number > 0):
    i = i*number
    number -= 1
print (i)


# In[30]:


def factorial (number):
    if(number == 0):
        return 1
    else:
        return number * factorial(number-1)


# In[31]:


print(factorial(5))


# In[100]:


number = 5
spaces = 0
while(number > 0):
    i = 1
    k = 0
    string = ''
    while(k < spaces):
        string += " "
        k += 1
    while (i <= number):
        if (i % 2 == 0):
            string += "0"
        else:
            string += "1"
        i += 1
    print (string)
    number -= 2
    spaces += 1


# In[86]:


# Table of a number
number = int(input("Enter Number: "))
rang = int(input("Enter range 1-: "))
i = 1
while(i <= rang):
    print(number,"*",i,"=",i*number)
    i += 1


# In[82]:


# HCF of two numbers
number = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))
i = 1
small = 1
if (number < number2):
    small = number
else:
    small = number2
while(i < small):
    if((number % i == 0) and (number2 % i == 0)):
            j = i
    i += 1
print (j)


# In[85]:


i = 1
j = 0
while (i <= 10):
    j = j+i
    i += 1
print ("Sum of first 10 natural integers:",j)
    


# In[84]:


i = 1
while (i <= 10):
    print ("Cube of",i,":", i**3)
    i += 1


# In[89]:


# Table of a number Vertically
number = int(input("Enter Number: "))
rang = int(input("Enter range 1-: "))
i = 1
while(i <= rang):
    print(number,"*",i,"=",i*number)
    i += 1


# In[4]:


number = 5
i = 1
j = ''
while (i <= number):
    j = str(i)
    print (j*i)
    i += 1


# In[20]:


i = 1
j = 1
k = 0
num = 4
while (j <= num):
    k = k+j
    while(i <= k): 
        print (i, end='')
        i += 1
    print('')
    j += 1


# In[53]:


def diagonalDifference(arr):
    i = 0
    j = 0
    sum1D, sum2D = 0, 0
    while (i < len(arr)):
        j = 0
        while(j < len(arr[i])):
            if i == j:
                sum1D = sum1D + arr[i][j]
            if len(arr[i]) - j - 1 == i:
                sum2D = sum2D + arr[i][j]
                print(arr[i][j])
            j = j + 1
        i = i + 1
    if(sum1D > sum2D):
        return sum1D - sum2D
    else:
        return sum2D - sum1D
    


# In[54]:


arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
print(arr)


# In[55]:


print(diagonalDifference(arr))


# In[72]:


i = 1
string = ""
n = 6
k =
while (i <= n):
    string += "#"
    print(string)
    i += 1
    
    


# In[79]:


i = 1
n = 10
j = n-1
while (i <= n):
    print(" "*j+"#"*i)
    i = i+1
    j = j-1


# In[93]:


number = 6
spaces = number - 1
j = 1
    
while (j <= number) :    
    string = ""
    k = 0
    while(k < spaces):
        string += " "
        k += 1
    i = 0
    while (i < j):
        string += "#"
        i += 1
    print(string)
    j += 1
    spaces -= 1


# In[109]:


arr1 = [1,5,3,4,2]
arr = sorted(arr1 , reverse=False)
x = len(arr)
minSum = 0
maxSum = 0
i = 0
j = 1
while (i < x-1):
    minSum += arr[i]
    i += 1
while (j < x):
    maxSum += arr[j]
    j += 1
print(minSum,"  " , maxSum)


# In[126]:


ar = [3,2,3,1,3]
x = len(ar)
count = 0
maximum = 0
for i in range(0, x): 
    if ar[i] > maximum:
        maximum = ar[i]
for j in range(0, x):
    if (ar[j] == maximum):
        count += 1
print (count)


# In[119]:


ar = [1,5,3,4,2]
x = len(ar)
i = 0
j = 0
count = 0
maximum = 0
for i in range(1, x): 
        if ar[i] > maximum: 
            maximum = ar[i] 
print(maximum)


# In[2]:


s = "12:09:05PM"
i = 0
l = len(s)
hh = 0
for i in range (0, l):
    hours = int(s[0]+s[1])
    minutes = int(s[3]+s[4])
    if (hours < 12 and s[8] == 'P'):
        hh = hours + 12
    if (hours == 12 and s[-2] == 'A'):
        hh = 0
print (hh)


# In[23]:


s = "12:09:05AM"
s1 = ''
if (s[:2] == '12' and s[-2:] == 'AM'):
    s1 = "00" + s[2:-2]
if (s[-2:] == 'AM'):
    s1 = s[:-2]   
if (s[-2:] == 'PM'and s[:2] == '12'):
    s1 = s[:-2]   
else:
    s1 = str(int(s[:2]) + 12) + s[2:8]
print (s1)


# In[24]:


def timeConversion(s):
    
    if (s[:2] == '12' and s[-2:] == 'AM'):
        return"00" + s[2:-2]
    if (s[-2:] == 'AM'):
        return s[:-2]   
    if (s[-2:] == 'PM'and s[:2] == '12'):
        return s[:-2]   
    else:
        return str(int(s[:2]) + 12) + s[2:8]


# In[25]:


print (timeConversion(s))


# In[60]:


h = 1
m = 1
s = ''
numbers = ("zero","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty","twenty one","twenty two","twenty three","twenty four","twenty five","twenty six","twenty seven","twenty eight", "twenty nine", "thirty")
if (m == 0):
    s = numbers[h] +" "+ "o'"+" "+"clock"
if (m == 1):
    s = numbers[m]+" "+ "minute past" +" "+ numbers[h]
if (m == 15):
    s = "quarter past" +" "+ numbers[h]
if (m == 30):
    s = "half past" +" "+ numbers[h]
if (m >= 2 and m <= 14):
    s = numbers[m]+" " + "minutes past" +" " +numbers[h]
if (m >= 16 and m <= 29):
    s = numbers[m]+" " + "minutes past" +" " +numbers[h]
if (m >= 31 and m <= 44) or (m >= 46 and m <= 59):
    m1 = 60 - m
    if (h == 12):
        h = h%12
    s = numbers[m1]+" " + "minutes to" +" " +numbers[h+1]
if (m == 45):
    if (h == 12):
        h = h%12
    s = "quarter to" +" " +numbers[h+1]

print (s)
    


# In[76]:


"""Little Bobby loves chocolate. He frequently goes to his favorite  store, Penny Auntie, to buy them.
They are having a promotion at Penny Auntie. If Bobby saves enough wrappers, he can turn them in for a free chocolate.
For example, Bobby has  to spend on bars of chocolate that cost  each. He can turn in  wrappers to receive another bar.
Initially, he buys  bars and has  wrappers after eating them. He turns in  of them, leaving him with , for  more bars.
After eating those two, he has  wrappers, turns in  leaving him with  wrapper and his new bar. Once he eats that one,
he has  wrappers and turns them in for another bar. After eating that one, he only has  wrapper, and his feast ends.
Overall, he has eaten  bars."""
n = 15          # an integer representing Bobby's initial amount of money
c = 3           # an integer representing the cost of a chocolate bar
m = 2           # an integer representing the number of wrappers he can turn in for a free bar
wrapers = 0
while (n >= c):
    bars = int(n/c)
    n = int(n%c)
    wrapers += bars
    while (wrapers >= m):
        bars += int(wrapers/m)
        wrapers = int(wrapers%m) + int(wrapers/m)
print(bars)


# In[154]:


"""Service Lane: You will be given an array of widths at points along the road (indices),
then a list of the indices of entry and exit points. Considering each entry and exit point pair,
calculate the maximum size vehicle that can travel that segment of the service lane safely."""
cases = [[2, 3], [1, 4], [2, 4], [2, 4], [2, 3]]
ar = []
width = [1, 2, 2, 2, 1]
n1 = len(cases)
n3 = len(cases[0])
for i in range (n1):
    ar2 = []
    small = 100000
    for j in range (n3):
        ar2.append(cases[i][j])
    a = ar2[0]
    b = ar2[1]
    for m in range (a, b+1):
        if (width[m] < small):
            small = width[m]
    ar.append(small)
print (ar)


# In[226]:


""" Lisa's Workbook
Function Description
Complete the workbook function in the editor below.
It should return an integer that represents the number of special problems in the workbook.
workbook has the following parameter(s):
n: an integer that denotes the number of chapters
k: an integer that denotes the maximum number of problems per page
arr: an array of integers that denote the number of problems in each chapter"""
n = 5
k = 3
arr = [4,2,6,1,10]
pgNo = 1
specialPage = 0
for j in range (0, len(arr)):
    count = 1
    count2 = 0
    for m in range (1, arr[j]+1):
        if (m == pgNo):
            specialPage += 1
        if (count == k):
            count = 0
            count2 = 0
            pgNo += 1
        else:
            count2 += 1
        count += 1
    if (count2 > 0):
        pgNo += 1
print ("Special pages are: ", specialPage)


# In[2]:


from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
import pandas as pd
from bokeh.palettes import Spectral5
output_file('simple_timeseries_plot.html')

df = pd.read_csv('C:/Users/Owner/Desktop/student.csv')
df['average'] = df[['Math','Physics','Chemistry', 'English']].mean(axis = 1)

p = figure()

p.line(x='Roll No', y='Math', line_width=2, source=df, legend_label='Mat')
p.line(x='Roll No', y='Physics', line_width=2, source=df, color=Spectral5[1], legend_label='Phy')
p.line(x='Roll No', y='Chemistry', line_width=2, source=df, color=Spectral5[2], legend_label='Che')
p.line(x='Roll No', y='English', line_width=2, source=df, color=Spectral5[3], legend_label='Eng')

p.yaxis.axis_label = 'Roll Numbers'

show(p)


# In[15]:


from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
import pandas as pd
from bokeh.palettes import Spectral5
output_file('simple_timeseries_plot.html')

df = pd.read_csv('C:/Users/Owner/Desktop/job.csv')

numlines=len(df.columns)
mypalette=Spectral5[0:numlines]

p = figure(width=500, height=300) 

p.multi_line(xs=[df.index.values]*numlines,
                ys=[df[name].values for name in df],
                line_color=mypalette,
                line_width=5)

p.yaxis.axis_label = 'Roll Numbers'

show(p)


# In[11]:


print(df.Direction)
print(len(df))


# In[36]:


import holoviews as hv
hv.extension('bokeh')

df = pd.read_csv('C:/Users/Owner/Desktop/job.csv')
ds = hv.Dataset(df)
ds.to(hv.Curve, 'Hour' ,'AproachCount', 'Direction')


# In[120]:


df = pd.read_csv('C:/Users/Owner/Desktop/job.csv')
df2= df.groupby('Direction') 
colors =  {"Left": "blue", "Right": "red", "Straight" : "green"}
curves = []
for x in df.Direction:
    ds = df2.get_group(x)
    cur = hv.Curve( data = (ds.Hour, ds.AproachCount), label = x).opts(color = colors[x])
    curves.append(cur)

from functools import reduce
reduce(lambda x, y: x*y, curves)



df = pd.read_csv('C:/Users/Owner/Desktop/job.csv')
df2= df.groupby('Direction') 



df = pd.read_csv('C:/Users/Owner/Desktop/job.csv')
df2= df.groupby('Direction')
ds = df2.get_group('Left')
ds1= df2.get_group('Right')
ds2 = df2.get_group('Straight')
Curve_left = hv.Curve( data = (ds.Hour, ds.AproachCount), group = 'Left', label= 'L')
Curve_right = hv.Curve( data = (ds1.Hour, ds1.AproachCount), group = 'Right', label= 'R').opts(color = 'red')
Curve_straight = hv.Curve( data = (ds2.Hour, ds2.AproachCount), group = 'Straight', label= 'S').opts(color = 'green')
Curves = Curve_left * Curve_right * Curve_straight
Curves



df = pd.read_csv('C:/Users/Owner/Desktop/job.csv')
colors =  {"Left": "blue", "Right": "red", "Straight" : "green"}
curves = []
for name, group in df.groupby('Direction'):
    print(group)
