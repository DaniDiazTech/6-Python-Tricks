def eliminate_duplicates(lst):
    """
    Returns a sorted list, without duplicates
    """ 
    new_list = list(set(lst)) 
    
    new_list.sort()    
    
    return new_list

list1 = [25, 12, 11, 4, 12, 12, 25]

print(eliminate_duplicates(list1))