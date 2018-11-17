def average(string):
    lst = string.split()
    a = 0

    for str in lst:
        a += len(str.strip())
    return a/len(lst)

def vowel_count(string):
    a = string.count('a') + string.count('e') + string.count('i') + string.count('o')+ string.count('u')
    return a

def rotate(string):
    vowelCounts = [0]*26
    newStrings = [None]*26

    for i in range(0,26):
        for chr in string:
            intermediate = ord(chr) +1
            intermediate2 = chr(intermediate)
            vowelCounts[i] += vowel_count(string)
    print(vowelCounts)