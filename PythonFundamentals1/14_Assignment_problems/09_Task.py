#computing the simple interest
principal = input("Enter Principal :")
rate = input("Enter Rate :")
time = input("Enter Time :")

p = float(principal)
r= float(rate)
t = float(time)
SI = p * r * t / 100

print("Simple interest is :" , SI)