def new_list_4(my_list: list):
    """This function return new list from my list, if string im my list."""
    my_list = [i for i in my_list if type(i) == str]
    print("(Exercise 4) List with type of elements string: ", my_list)
    return my_list
