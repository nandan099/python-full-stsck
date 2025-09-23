# Implement a function to merge two dictionaries.
def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()  
    merged_dict.update(dict2)    
    return merged_dict

# Ex 2

dict_a = {'a': 1, 'b': 2}
dict_b = {'b': 3, 'c': 4}
result = merge_dicts(dict_a, dict_b)
print(result)  # Output: {'a': 1, 'b': 3,