def new_list(my_str_1: str, my_str_2: str):
    """This function return new list from my str 1 and my str 2, if both string have same symbols."""
    new_li = list(set(my_str_1) & set(my_str_2))
    print(new_li)
    return new_li
