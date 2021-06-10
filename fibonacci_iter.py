n = 20
prev = 0
prev_prev =1
fibn = 0
print ('iteration 0: 0')
for i in range(n-1):
    fibn = prev + prev_prev
    prev_prev = prev
    prev = fibn
    
    print('iteration ', i, 'value :', fibn)
    
def fib(n):
    return fib(n-1)+fib(n-2)

print(fib(5))