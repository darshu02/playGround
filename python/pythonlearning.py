Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a=10
>>> b=20
>>> 
======== RESTART: C:/Users/darsh/Documents/darshika/home/condition.py ========
Traceback (most recent call last):
  File "C:/Users/darsh/Documents/darshika/home/condition.py", line 6, in <module>
    printf("b is greater",b)
NameError: name 'printf' is not defined
>>> 
======== RESTART: C:/Users/darsh/Documents/darshika/home/condition.py ========
b is greater 20
>>> 2+5
7
>>> 18/7
2.5714285714285716
>>> 9%4
1
>>> 8.75%.5
0.25
>>> 6^3
5
>>> 6**3
216
>>> -5**4
-625
>>> darshika
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    darshika
NameError: name 'darshika' is not defined
>>> x = 18
>>> x
18
>>> x+15
33
>>> x**3
5832
>>> pow(2,3)
8
>>> abs(-897)
897
>>> import math
>>> math.floor(234.789)
234
>>> math.sqrt(25)
5.0
>>> a=math.sqrt()
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    a=math.sqrt()
TypeError: sqrt() takes exactly one argument (0 given)
>>> a=math.sqrt
>>> a(100)
10.0
>>> b=math.floor
>>> b(34567.1234567)
34567
>>> 
======= RESTART: C:/Users/darsh/Documents/darshika/home/saveprogram.py =======
Traceback (most recent call last):
  File "C:/Users/darsh/Documents/darshika/home/saveprogram.py", line 1, in <module>
    a=raw_input("Enter name")
NameError: name 'raw_input' is not defined
>>> 
======= RESTART: C:/Users/darsh/Documents/darshika/home/saveprogram.py =======
Enter namedarshika
Good Evening darshika
>>> 
======= RESTART: C:/Users/darsh/Documents/darshika/home/saveprogram.py =======
Enter name
======= RESTART: C:/Users/darsh/Documents/darshika/home/saveprogram.py =======
Enter nameDarshika
Good Evening Darshika
press<Enter>
>>> "Darshika said,\ "How now\" to me"
SyntaxError: invalid syntax
>>> "Darshika said'\"hey now\" to me"
'Darshika said\'"hey now" to me'
>>> "Darshika said,\"hey now\" to me"
'Darshika said,"hey now" to me'
>>> a='Darshika'
>>> b='Digant'
>>> a+b
'DarshikaDigant'
>>> a + b
'DarshikaDigant'
>>> a ,b
('Darshika', 'Digant')
>>> a='Darshika '
>>> a+b
'Darshika Digant'
>>> "Good Evening"
'Good Evening'
>>> print("Good Evening")
Good Evening
>>> a=26
>>> print("Darshika is "+a)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    print("Darshika is "+a)
TypeError: can only concatenate str (not "int") to str
>>> a=str(26)
>>> print("Darshika is "+a)
Darshika is 26
>>> b=27
>>> print('Digant is '+ ~b~)
SyntaxError: invalid syntax
>>> print('Digant is '+ `b`)
SyntaxError: invalid syntax
>>> print ("Diagnt is " + `b`)
SyntaxError: invalid syntax
>>> print "Digant is " + `b`
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("Digant is " + `b`)?
>>> 
========== RESTART: C:/Users/darsh/Documents/darshika/home/input.py ==========
Enter Name: Darshika
Darshika
>>> 
========== RESTART: C:/Users/darsh/Documents/darshika/home/input.py ==========
Traceback (most recent call last):
  File "C:/Users/darsh/Documents/darshika/home/input.py", line 1, in <module>
    a=raw_input("Enter Name: ")
NameError: name 'raw_input' is not defined
>>> 
========== RESTART: C:/Users/darsh/Documents/darshika/home/input.py ==========
Enter Name: Digant
Digant
>>> family=['mom','dad','brother','sister','wife','husband']
>>> family(4)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    family(4)
TypeError: 'list' object is not callable
>>> family[4]
'wife'
>>> family[-0]
'mom'
>>> family[-1]
'husband'
>>> 'Darshika'[5]
'i'
>>> "Digant"[6]
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    "Digant"[6]
IndexError: string index out of range
>>> "Darshika"[5]
'i'
>>> "Darshika"[-1]
'a'
>>> li=[0,1,2,3,4,5,6,7,8,9]
>>> li[0:5]
[0, 1, 2, 3, 4]
>>> li[:]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> li[4:]
[4, 5, 6, 7, 8, 9]
>>> li[:8]
[0, 1, 2, 3, 4, 5, 6, 7]
>>> li[-1:-6]
[]
>>> li[-6:-1]
[4, 5, 6, 7, 8]
>>> li[-5:]
[5, 6, 7, 8, 9]
>>> li[:-6]
[0, 1, 2, 3]
>>> li[1:6:2]
[1, 3, 5]
>>> li[1:6:-2]
[]
>>> li[6:1:-2]
[6, 4, 2]
>>> li[::-2]
[9, 7, 5, 3, 1]
>>> li[10:0:-2]
[9, 7, 5, 3, 1]
>>> [1,2,3]+[4,5,6]
[1, 2, 3, 4, 5, 6]
>>> [1,2,3]+'Darshika'
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    [1,2,3]+'Darshika'
TypeError: can only concatenate list (not "str") to list
>>> 'Darshika'*5
'DarshikaDarshikaDarshikaDarshikaDarshika'
>>> Darshika*5
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    Darshika*5
NameError: name 'Darshika' is not defined
>>> 2***5
SyntaxError: invalid syntax
>>> 2**3
8
>>> [2]*10
[2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
>>> name='Darshika'
>>> z in name
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    z in name
NameError: name 'z' is not defined
>>> name='Darshika'
>>> 'z' in name
False
>>> 'a' in name
True
>>> 'husband' in family
True
>>> 'dog' in family
False
>>> len('Darshika')
8
>>> no=[1,72,34,20,567]
>>> len(no)
5
>>> a=[darshika,digant]
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    a=[darshika,digant]
NameError: name 'darshika' is not defined
>>> a=['darshika','digant']
>>> len(a)
2
>>> max(no)
567
>>> min(no)
1
>>> max(a)
'digant'
>>> min(b)
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    min(b)
NameError: name 'b' is not defined
>>> min(a)
'darshika'
>>> list(a)
['darshika', 'digant']
>>> list(no)
[1, 72, 34, 20, 567]
>>> list('Darshika')
['D', 'a', 'r', 's', 'h', 'i', 'k', 'a']
>>> list(12345678934567892345)
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    list(12345678934567892345)
TypeError: 'int' object is not iterable
>>> number()
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    number()
NameError: name 'number' is not defined
>>> numbers
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    numbers
NameError: name 'numbers' is not defined
>>> no
[1, 72, 34, 20, 567]
>>> no[2]=108
>>> no
[1, 72, 108, 20, 567]
>>> del no[0]
>>> no
[72, 108, 20, 567]
>>> list['darshika']
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    list['darshika']
TypeError: 'type' object is not subscriptable
>>> list('Darshika')
['D', 'a', 'r', 's', 'h', 'i', 'k', 'a']
>>> a=list('Darshika')
>>> a
['D', 'a', 'r', 's', 'h', 'i', 'k', 'a']
>>> list
<class 'list'>
>>> 'Darshika'
'Darshika'
>>> a[9:]=list('Digant')
>>> a
['D', 'a', 'r', 's', 'h', 'i', 'k', 'a', 'D', 'i', 'g', 'a', 'n', 't']
>>> a[6:]=list('Digant')
>>> a
['D', 'a', 'r', 's', 'h', 'i', 'D', 'i', 'g', 'a', 'n', 't']
>>> z=[0,1,2,3,4]
>>> z
[0, 1, 2, 3, 4]
>>> z[1:1]
[]
>>> z[1:1]=list(2,2,2)
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    z[1:1]=list(2,2,2)
TypeError: list expected at most 1 arguments, got 3
>>> z[1:1]=list[2,2,2]
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    z[1:1]=list[2,2,2]
TypeError: 'type' object is not subscriptable
>>> z[1:1]=[2,2,2]
>>> z
[0, 2, 2, 2, 1, 2, 3, 4]
>>> z[1:3]=[2,2,2]
>>> z
[0, 2, 2, 2, 2, 1, 2, 3, 4]
>>> z[1:2]=[2,2,2]
>>> z
[0, 2, 2, 2, 2, 2, 2, 1, 2, 3, 4]
>>> z[1:1]=[5,5,5]
>>> z
[0, 5, 5, 5, 2, 2, 2, 2, 2, 2, 1, 2, 3, 4]
>>> z[0:1]=[5]
>>> z
[5, 5, 5, 5, 2, 2, 2, 2, 2, 2, 1, 2, 3, 4]
>>> z[0:1]=[5,5]
>>> TypeError: 'type' object is not subscriptable
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> 
>>> digant = list('digant')
>>> digant
['d', 'i', 'g', 'a', 'n', 't']
>>> digant[:3] = list('Darshika')
>>> digant
['D', 'a', 'r', 's', 'h', 'i', 'k', 'a', 'a', 'n', 't']
>>> digant[6:] = list('12345')
>>> digant
['D', 'a', 'r', 's', 'h', 'i', '1', '2', '3', '4', '5']
>>> digant[2:2] = list('zzzz')
>>> digant
['D', 'a', 'z', 'z', 'z', 'z', 'r', 's', 'h', 'i', '1', '2', '3', '4', '5']
>>> digant[2:10] = list('QQQQ')
>>> digant
['D', 'a', 'Q', 'Q', 'Q', 'Q', '1', '2', '3', '4', '5']
>>> digant[1:5]=[]
>>> di
Traceback (most recent call last):
  File "<pyshell#146>", line 1, in <module>
    di
NameError: name 'di' is not defined
>>> digant
['D', 'Q', '1', '2', '3', '4', '5']
>>> list=[1,2,3,4]
>>> list[1:1]=[]
>>> list
[1, 2, 3, 4]
>>> list[1:2]=[]
>>> list
[1, 3, 4]
>>> del list[1]
>>> list
[1, 4]
>>> face=[20,34,40]
