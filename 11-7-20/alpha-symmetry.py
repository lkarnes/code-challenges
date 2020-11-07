import string
def aplpha_symmetry(arr):
    li = []
    x = list(string.ascii_lowercase)
    for i in arr:
        if len(i) > len(x):
            i = i[0:len(x)]
        i = i.lower()
        pos = 0
        count = 0
        for j in i:     
            if j == x[pos]:
                count = count + 1 
            pos = pos + 1
        li.append(count)   
    return li