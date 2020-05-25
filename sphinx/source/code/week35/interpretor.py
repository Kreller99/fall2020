Python 3.7.7 (default, Mar 10 2020, 15:43:33) 
n 3.7.7 (default, Mar 10 2020, 15:43:33) 
[Clang 11.0.0 (clang-1100.0.33.17)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> s = 'Hello world'
>>> s
'Hello world'
>>> type(s)
<class 'str'>
>>> s2 = 'i am hungry'
>>> s+s2
'Hello worldi am hungry'
>>> s[1:3]
'el'
>>> s[-1:-4]
''
>>> s[-4:-1]
'orl'
>>> s[-4:-]
  File "<stdin>", line 1
      s[-4:-]
                ^
                SyntaxError: invalid syntax
                >>> s[-4:]
                'orld'
                >>> s[-4:-0]
                ''
                >>> s[-4:]
                'orld'
                >>> 
[Clang 11.0.0 (clang-1100.0.33.17)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> s = 'Hello world'
>>> s
'Hello world'
>>> type(s)
<class 'str'>
>>> s2 = 'i am hungry'
>>> s+s2
'Hello worldi am hungry'
>>> s[1:3]
'el'
>>> s[-1:-4]
''
>>> s[-4:-1]
'orl'
>>> s[-4:-]
  File "<stdin>", line 1
    s[-4:-]
          ^
SyntaxError: invalid syntax
>>> s[-4:]
'orld'
>>> s[-4:-0]
''
>>> s[-4:]
'orld'
>>> 
