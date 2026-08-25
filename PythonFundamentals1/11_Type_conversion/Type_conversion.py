#two types k hote h jisme ek data type sae dosre mae convert krte h
#first hota h implicit type conversion kehte h automatic by interpreter
#second explicit hota h type casting khete h isme by devloper compatible type mae convert kr deta H

#implicit conversion (automatic by interpreter)
sum = 5 + 10.0
divide = 20/5
print(sum , type(sum))
print(divide , type(divide))

#explicit type casting using functions

sum1 = (int(5+10.0))
sum2 = (float(5+5))
val = (bool(10)) #return true always for non zero value , else false

print(sum1 , type(sum1))
print(sum2 , type(sum2))
print(val , type(val))