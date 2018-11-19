>>> # Single quotes
>>> print('P"casso')
P"casso

>>> # Double quotes
>>> print("P'casso")
P'casso

>>> # Tripple quotes
>>> print('''...Picasso...''')
...Picasso...

>>> # Escape sequences
>>> print("P\ti\nca\Osso")
P	i
ca\Osso

>>> #Raw strings
>>> print(r"C:\myscript.py")
C:\myscript.py

>>> # Byte strings
>>> print(b'Picas\x01so')
b'Picas\x01so'
>>> type(b'Picas\x01so')
<class 'bytes'>
>>> type('normal_string')
<class 'str'>

>>> # Unicode strings
>>> S = 'A\u00c4B\U000000e8C'
>>> S
'A-B-C'
>>> len(S)
5
>>> 