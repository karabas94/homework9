def new_list_5(my_str: str):
    """This function return new list from my str, if symbol im my string one."""
    new_li = [i for i in my_str if my_str.count(i) == 1]
    print("(Exercise 5) List with symbol which cross one time : ", new_li)
    return new_li
