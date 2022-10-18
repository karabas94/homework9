def new_list_3(my_list: list):
    """This function return new list from my list, if string im my list have symbol - "a"."""
    new_li = [i for i in my_list if i.find("a") >= 0]
    print("(Exercise 3) String of list with symbol - 'a': ", new_li)
    return new_li
