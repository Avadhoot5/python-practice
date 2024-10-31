# Walrus operator

if (n := len([1,2,3,4,5])) > 3:
    print(f'List is too long ({n} elments, expected <= 3)')

n : int = 5

name : str = 'hello world'

def sum(a: int, b: int) -> int:
    return a + b

print(sum(5, 9))

# walrus, types in python
# types in dict, tuple, union.
# match case 
# try except -> raise custom error.
# try except else. tr except finally.
