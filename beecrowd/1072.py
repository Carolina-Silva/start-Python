i = 1
dentro = 0
fora = 0
n = int(input())
while i <= n:
    x = int(input())
    if x >= 10 and x <= 20:
        dentro += 1
    else:
        fora += 1
    i+=1
print("%i in" %dentro)
print("%i out" %fora)