fibonacci = [0,1]
for i in range(1,20-1):
    serie = fibonacci[i] + fibonacci[i-1]
    fibonacci.append(serie)
print(fibonacci)