
try:
    with open('problem/1.txt') as f:
        print(f.read())
except Exception as e:
    print(e)

try:
    with open('problem/2.txt') as f:
        print(f.read())
except Exception as e:
    print(e)

try:
    with open('problem/3.txt') as f:
        print(f.read())
except Exception as e:
    print(e)
    
print('thank you!')
