# Notes of [Google python course](https://developers.google.com/edu/python)

## argv

`print sys.argv`, so start count argv[1]

## hello

* Just hello
* `def`
* argv
* Hello + `name`

* if with parentheses or not is Ok
* If not run that line, possibly wrong will not be noticed.
``` python
if True:
    print("haha")
else:
    MethodNotExist()
```

## String

* `+`
* index, `s[0]`
* slice
``` python
# Demo with `Hello`
# H  e  l  l  o
# 0  1  2  3  4
# -5 -4 -3 -2  -1

a[::-1]
a[:]
a[1:]
a[:-1]
```
* reverse index
* Format
``` python2
'%s %d %c' % ('abc',3,'d')
```

## List

* Different types
``` python
li = [1,None,True,'a',"a","abc"]
```

Li is mutable, so change the elements in it won't the `id`

``` vi
>> id(li)
>> li[1] = False
>> id(li)
```

* copy
``` python
li2 = li
id(li) == id(li2)

import copy
...

```

* Loop the list

```
for element in li:
    print element
```

* sorted
``` python
li = ['ac','ccc', 'dc']
sorted(li, key=len)
# ['ac', 'dc', 'ccc']

def last(str):
    return str[-1]

sorted(li, key=last)
# ['ac', 'ccc', 'dc']
```

* join & split
``` python
' '.join(li)
'_'.join(li)
li2 = '?'.join(li)
# 'ac?ccc?dc?12'

li2.split('?')
```

* range(num)

## Tuple

Almost like list, but immutable

``` python
# unpack
tu1 = tuple([1,2,3])
x,_,z = tu1 # we can use `_` to skip un_unpack elements
```