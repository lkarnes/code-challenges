def open_or_senior(data):
    li = []
    for i in data:
        if i[0] > 54 and i[1] > 7:
            li.append("Senior")
        else:
            li.append("Open")
    return li