# Crunch
## Description
Crunch word generator that use itertools to generate wordlist, also can
receive a function as input to process that word in the running time

# Usage
```python
from crunch import Crunch
# Crunch object
c = Crunch(letters="(default = ascii_letters + digits + punctuation + whitespace)",
           remove="The chars to be removed from letters (default None)")

# Input of the function always is a tuple for example ('1','1','1','1')
# Crunch has as default lambda x: None
# The user function is help full when for example you want to crack a specific
# user in a SSH connection you can do it with this and you don't need to save
# a huge file of passwords
def my_func(word:tuple):
  print(''.join(word))

# Generate all possible word with range 4, 5, 6 using the letters reference
c.generate(4, 6, my_func)

```
## Example
```python
from crunch import Crunch

# Chars to be removed
remove = 'abc'

# Create a Crunch object removing from it's default abc
c = Crunch(remove=remove)

# print the len of each word
def my_func(word:tuple):
  print(len(word))

# run
c.generate(3, 5, my_func)

```
