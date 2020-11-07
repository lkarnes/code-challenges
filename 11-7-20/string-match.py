def string_match(a,b):
    pos = 0
    if '*' not in a and a != b:
        return False
    for i in a.split('*'):
        
        if i not in b:
            return False
        if pos == 1 and i != b[len(b)-len(i)::]:
            return False
        pos = pos + 1
    return True