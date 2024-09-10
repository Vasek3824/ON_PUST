my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
setter = 0
while setter < len(my_list):
    if my_list[setter] > 0:
        print(my_list[setter])
        setter += 1
    elif my_list[setter] == 0:
        setter += 1
    else:
        break

