Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
no =123
type(no)
<class 'int'>
id(no)
1794217021488
value = 0b1111
print(value)
15
value = 0b1011
print(value)
11
value = 0o12345
print (value)
5349
value
5349
vaalue = 0xabc
value
5349
value = 0xabc
value
2748
value = 0xdcg
SyntaxError: invalid hexadecimal literal
value = 0xface
value
64206
value = 0xcea
value
3306
value = 0xeac
value
3756
value = 0xdca
value
3530
print(hex(10))
0xa
print ( bin(10))
0b1010
print (oct(10))
0o12
no =1.234
no = 1.2e3
no = 4.5e2
no
450.0
no = 1.2e3
value = 5
value = 5
5+6j
(5+6j)
value = 5+6j
print (value.imag)
6.0
print(value.real)
5.0
bool
<class 'bool'>
mark 1= 98
SyntaxError: invalid syntax
mark1 =98
mark2 =100
print(mark1>mark2)
False
print (mark2=mark1)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    print (mark2=mark1)
TypeError: 'mark2' is an invalid keyword argument for print()
print (mark1=mark2)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    print (mark1=mark2)
TypeError: 'mark1' is an invalid keyword argument for print()
print(mark1 = mark2)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    print(mark1 = mark2)
TypeError: 'mark1' is an invalid keyword argument for print()
print(mark1)
98
print (mark1=mark2)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    print (mark1=mark2)
TypeError: 'mark1' is an invalid keyword argument for print()
print (mark2>mark1)
True
print(True+ False)
1
print (True+True)
2
print (False+False)
0
name= 'shanmuga'

name
'shanmuga'
name= "shanmuga
SyntaxError: unterminated string literal (detected at line 1)
name= "shanmuga"
name= '''shanmuga priyan'''
name
'shanmuga priyan'
name2 = "shanmuga priyan"
name2
'shanmuga priyan'
name3= """shanmuga priyan"""
name3
'shanmuga priyan'
name4 =""" shanmuga
puppy
sun
moon"""
name4
' shanmuga\npuppy\nsun\nmoon'
print(name4)
 shanmuga
puppy
sun
moon
value =150
sent =" 'pandi' 'god'"
print (sent)
 'pandi' 'god'
-value
-150
_value
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    _value
NameError: name '_value' is not defined. Did you mean: 'value'?
sent = ''' "sun" 'vanna' '''
sent
' "sun" \'vanna\' '
