def new_list_4(my_list: list):
    """This function return new list from my list, if string im my list."""
    new_li = [i for i in my_list if type(i) == str]
    print("(Exercise 4) List with type of elements string: ", new_li)
    return new_li
