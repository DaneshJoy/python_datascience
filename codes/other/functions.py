
''' No input / No output '''

def my_print():
    print('-'*15)
    print('='*15)
    
print('Hello')
my_print()


''' Input parameter / no output '''
def power2(n):
    print(n**2)

power2(4)


''' Input param / Output param '''
def power2_pro(n, m):
    p = n**m
    return p, m

x, y = power2_pro(5, 3)
print(y)





