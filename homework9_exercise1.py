def new_list_1(my_list: list):
    """This function return new list from my list, if string im my list uneven will be reversed"""
    for i in range(len(my_list)):
        if i % 2 != 0:
            my_list[i] = (my_list[i])[::-1]
    print("(Exercise 1) List with reverse uneven string: ", my_list)
    return my_list
