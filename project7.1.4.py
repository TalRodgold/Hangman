def squared_numbers(start, stop):
    end = stop +1
    list =[start**2]
    while start <= stop:
        start += 1
        if start == end:
            break
        list.append(start**2)

    return list

print(squared_numbers(4,8))


