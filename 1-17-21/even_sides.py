def find_even_index(arr):
    index = 0;
    running = True
    if arr[0] == sum(arr[index:len(arr)]):
        return 0
    for i in arr:
        if running: 
            if sum(arr[0:index-1]) == sum(arr[index:len(arr)]):
                running = False
            else:index += 1
    if index == len(arr) and sum(arr[0:index-1]) != sum(arr[index:len(arr)]):
        return -1
    return index -1
    