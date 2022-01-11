Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
alphabets ="abcdefghijklmnopqrstuvwxy"
print (alphabets)
abcdefghijklmnopqrstuvwxy
print (alphabets {0})
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print ( alphabets[0])
a
print (alphabets [-1])
y
print (alphabets [True])
b
print (alphates [false])
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print (alphates [false])
NameError: name 'alphates' is not defined. Did you mean: 'alphabets'?
print (alphates [False])
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print (alphates [False])
NameError: name 'alphates' is not defined. Did you mean: 'alphabets'?
print (alphabets [false])
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print (alphabets [false])
NameError: name 'false' is not defined. Did you mean: 'False'?
print (alphabets [False])
a
print (alphabets[:5])
abcde
print( alphabets[3:6])
def
print ( alphabets[-3:8])
name ="henna"
print(name[0].upper())
H
print (name[-1].upper())
A
print (name[0].upper()+name[:5]+name[-1].upper())
HhennaA
print (name[0].upper()+name[:4]+name[-1].upper())
HhennA
print (name[0].upper()+name[1:4]+name[-1].upper())
HennA
length (name)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    length (name)
NameError: name 'length' is not defined
len .name
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    len .name
AttributeError: 'builtin_function_or_method' object has no attribute 'name'
len (name)
5
name ="fiweojpgkepeka0vpdfm0ipejm'
SyntaxError: unterminated string literal (detected at line 1)
name ="vudomiozj0vuje9bojmj0gpkpgk bolo"
print (name[0].upper()+name[1:len(name)4]+name[-1].upper())
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print (name[0].upper()+name[1:len(name)-1]+name[-1].upper())

print ( alphabets[-3:8])

alphabets[:]
'abcdefghijklmnopqrstuvwxy'
alphabets[-1:]
'y'
alphabets[-3:10]
''
alphabets[10: -3]
'klmnopqrstuv'
alphabets[::3]
'adgjmpsvy'
alphabets[2::3]
'cfilorux'
name="san"
name.title
<built-in method title of str object at 0x000002385475C1F0>
name.upper
<built-in method upper of str object at 0x000002385475C1F0>
name.upper()
'SAN'
name.lower()
'san'
name.title()
'San'
name[0].upper(1)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    name[0].upper(1)
TypeError: str.upper() takes no arguments (1 given)
name[1].upper()
'A'
name
'san'
name[0].upper()
'S'
name[1:]
'an'
print(name[0].upper()+name[1:])
San
print 
