def new_list_2(my_list: list):
    """This function return new list from my list, if string im my list first symbol - "a"."""
    my_list = [i for i in my_list if i.find("a") == 0]
    print("(Exercise 2) String of list with first symbol - 'a': ", my_list)
    return my_list
