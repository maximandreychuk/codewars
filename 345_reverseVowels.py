def reverseVowels(s):
    vowels = ['a', 'e', 'i', 'o','u']
    s=list(s)
    start, end = 0, len(s)-1
    while start < end:
        if s[start].lower() in vowels and s[end].lower() in vowels:
            s[start], s[end] = s[end], s[start]
            start+=1
            end-=1
        elif s[start].lower() not in vowels:
            start+=1
        else:
            end-=1
    return "".join(s)








print(reverseVowels("IceCreAm")) # "AceCreIm"
print(reverseVowels("leetcode")) # "leotcede"