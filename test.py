a = ['a', 'b', 'c', 'd', 'e', 'f']
b = [1, 2, 3, 4, 5, 6]
for i in range(5):
    a, b = a[0:i] + b[i:], b[0:i] + a[i:]
    print(a + b)
