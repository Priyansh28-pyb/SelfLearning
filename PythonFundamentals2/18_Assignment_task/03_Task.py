num = int(input("Enter a number :"))

def p_num(num):
    while num > 0 :
        n = num % 10
        print(n)
        num = num // 10

p_num(num)