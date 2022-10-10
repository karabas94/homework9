def new_list_7(my_str_1: str, my_str_2: str):
    """This function return new list from my str 1 and my str 2, if both string have same ONE symbols."""
    new_li = [i for i in my_str_1 if my_str_1.count(i) == my_str_2.count(i) == 1]
    print("(Exercise 7) List with symbol which cross one time in the both strings: ", new_li)
    return new_li
