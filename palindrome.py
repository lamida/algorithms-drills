input = "alula"

for i in range(len(input)):
    j = len(input) - i - 1
    if i > j: 
        break
    #print(f"i: {i} j: {j}")
    print(f"left: {input[i]} right: {input[j]}")
    if input[i] != input[j]:
        print("no")
        break
print("yes")

