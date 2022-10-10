def new_list(my_str_1: str, my_str_2: str):
    """This function return new list from my str 1 and my str 2, if both string have same ONE symbols."""
    new_li = [i for i in my_str_1 if my_str_1.count(i) == my_str_2.count(i) == 1]
    print(new_li)
    return new_li
