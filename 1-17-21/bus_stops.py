def number(bus_stops):
    count = 0
    for i in bus_stops:
        count += i[0]
        count -= i[1]
    return count