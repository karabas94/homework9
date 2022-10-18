def new_list_1(my_list: list):
    """This function return new list from my list, if string im my list uneven will be reversed"""
    new_li = []
    for i in range(len(my_list)):
        if i % 2 != 0:
            new_li.append(my_list[i][::-1])
        else:
            new_li.append(my_list[i])
    print("(Exercise 1) List with reverse uneven string: ", new_li)
    return new_li
