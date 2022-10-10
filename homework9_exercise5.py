def new_list(my_str: str):
    """This function return new list from my str, if symbol im my string one."""
    new_li = [i for i in my_str if my_str.count(i) == 1]
    print(new_li)
    return new_li
