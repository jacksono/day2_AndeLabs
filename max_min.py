
def find_max_min(arg):
    '''Finds the mininum and maximum value in a list an returns then in a new list
    Args:
        arg: A list of numbers
    Returns:
        A list containing the min and max number, respectively or a list containing the 
        number of elements in arg if the mininum amd maximum numbers are equal
    '''
    max_value = max(arg)
    min_value = min(arg)
    if max_value == min_value:
        return [len(arg)]
    else:
        return [min_value, max_value]