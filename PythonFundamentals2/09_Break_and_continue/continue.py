#contniue keyword is used in lopps for skiping a current iterator

i  = 1
while i <= 10 :
    if (i % 3 == 0):
        i += 1
        continue

    print(i)
    i += 1