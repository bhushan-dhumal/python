List is Iterable and it generates iterator when passed in Iter method.

Generator gives Iterator(Generator Object)

Generator experssion is similar to list comprehension but generates sequence on runtime.

Generator means
- Generator method
- Generator object
- Generator expression

e.g. of generator expression is

``` python
gen = (n*n for n in range(10))
for a in gen:
  print(gen)
```
