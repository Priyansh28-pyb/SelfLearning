n = int(input("Enter a number : "))

def n_count(n):
    count = 0
    while n > 0:
        count += 1
        n = n // 10
    return count

print(n_count(n))

