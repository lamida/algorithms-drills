def palindrome(inn):
    left = 0  
    right = len(inn) - 1
    while left < right:
        if inn[left] == inn[right]:
            left += 1
            right -= 1
            continue
        else: 
            return False
    return True

print(palindrome("alxula"))

