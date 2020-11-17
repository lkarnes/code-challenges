def int_to_roman(self, num):
response = []
while num > 0:
    if num >= 1000:
        num -= 1000
        response.append('M')
    elif num >= 500:
        if num >= 900:
            num -= 900
            response.append('CM')
        else:
            num -= 500
            response.append('D')
    elif num >= 100:
        if num >= 400:
            num -= 400
            response.append('CD')
        else:
            num -= 100
            response.append('C')
    elif num >= 50:
        if num >= 90:
            num -= 90
            response.append('XC')
        else:
            num -= 50
            response.append('L')
    elif num >= 10:
        if num >= 40:
            num -= 40
            response.append('XL')
        else:
            num -= 10
            response.append('X')
    elif num >= 5:
        if num >= 9:
            num -= 9
            response.append('IX')
        else:
            num -= 5
            response.append('V')
    elif num == 4:
        num -= 4
        response.append('IV')
    else:
            num -= 1
            response.append('I')
return ''.join(response)