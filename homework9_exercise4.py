def new_list(my_list: list):
    """This function return new list from my list, if string im my list."""
    my_list = [i for i in my_list if type(i) == str]
    print(my_list)
    return my_list
