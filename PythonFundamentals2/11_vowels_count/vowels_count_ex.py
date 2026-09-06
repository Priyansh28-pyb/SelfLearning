word = "artificial"

ans = 0

for i in word:
    if(i == "a" or i == "e" or i == "i" or i == "o" or i == "u"):
        ans += 1

print("vowels count in this :" , ans)