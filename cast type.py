Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
name ="shan"
print(name(-1).upper())
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    print(name(-1).upper())
TypeError: 'str' object is not callable
print(name[-1].upper())
N
print(name[0].upper())
S
print(name[0].upper()+name+name[-1].upper())
SshanN
print(name[0].upper()+name[1:4]+name[-1].upper())
ShanN
len
<built-in function len>
leng(name)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    leng(name)
NameError: name 'leng' is not defined. Did you mean: 'len'?
len (name)
4
print(name[0].upper()+name[1:len(name)-1]+name[-1].upper())
ShaN
name ="vbsdoasijkliop"
print(name[0].upper()+name[1:len(name)-1]+name[-1].upper())
VbsdoasijklioP
print(name[:len(name)-1])+name[-1].upper()
vbsdoasijklio
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print(name[:len(name)-1])+name[-1].upper()
TypeError: unsupported operand type(s) for +: 'NoneType' and 'str'
print(name[:len(name)-1]+name[-1].upper())
vbsdoasijklioP
name ='henna'+'5'
name
'henna5'
word ='hahaha lmo'*10
print(word)
hahaha lmohahaha lmohahaha lmohahaha lmohahaha lmohahaha lmohahaha lmohahaha lmohahaha lmohahaha lmo
pay ="shanmuga priyan'
SyntaxError: unterminated string literal (detected at line 1)
pay ='shanmuga priyan'
'a' in pay
True
'k' in pay
False
mark1 =78
mark2=80.5
total = mark1+ mark2
print(total)
158.5
type(data)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    type(data)
NameError: name 'data' is not defined
data (type)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    data (type)
NameError: name 'data' is not defined
type(total)
<class 'float'>
ava = total/2
print (ava)
79.25
print(int(ava))
79
print('yor bill is '+str(total))
yor bill is 158.5
shirt= 500
pant= 600
total ='shirt'+'pant'
print (total)
shirtpant
total= 500+ 600
print(total)
1100
print( 'your bill is + str(total) )
       
SyntaxError: unterminated string literal (detected at line 1)
print( 'your bill is' + str(total) )
       
your bill is1100
print ("your bill is" , total)
       
your bill is 1100
a =2
       
bool(a)
       
True
a=13057
       
bool (a)
       
True
a=0
       
bool(a)
       
False
int(a)
       
0
name =1.4
       
bool (name)
       
True
name =''
       
bool (name)
       
False
name = 'dsihjioe'
       
bool(name)
       
True
value =70
       
complex(value)
       
(70+0j)
complex (4,6)
       
(4+6j)
a = 5j
       
complex(a)
       
5j
complex(True+ True)
       
(2+0j)
complex (True , True)
       
(1+1j)
a = 5
       
a = 5B
       
SyntaxError: invalid decimal literal
complex('5')
       
(5+0j)
mark = 90
       
if mark > 80:
       print('excellent')
elif mark > 60:
      print ('very good')
else mark > 50:
    
SyntaxError: expected ':'

==================================================================== RESTART: F:/small prog.py ====================================================================
Traceback (most recent call last):
  File "F:/small prog.py", line 1, in <module>
    if mark > 80:
NameError: name 'mark' is not defined

==================================================================== RESTART: F:/small prog.py ====================================================================
excellent
