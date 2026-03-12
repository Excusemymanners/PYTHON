

def main():
    print("=" * 60)
    print("PYTHON CONCEPTS - EXEMPLELE DIN POZE")
    print("=" * 60)
    
    print("\n1. NUMERIC TYPES")
    print("-" * 30)
    
    print(f"type(1) = {type(1)}")
    print(f"type(-10) = {type(-10)}")
    print(f"type(0) = {type(0)}")
    print(f"type(0.0) = {type(0.0)}")
    print(f"type(2.2) = {type(2.2)}")
    print(f"type(4E2) = {type(4E2)}")
    
    # Arithmetic operations
    print(f"10 + 3 = {10 + 3}")           # 13
    print(f"10 - 3 = {10 - 3}")           # 7
    print(f"10 * 3 = {10 * 3}")           # 30
    print(f"10 ** 3 = {10 ** 3}")         # 1000
    print(f"10 / 3 = {10 / 3}")           # 3.333...
    print(f"10 // 3 = {10 // 3}")         # 3 --> floor division - no decimals and returns an int
    print(f"10 % 3 = {10 % 3}")           # 1 --> modulo operator - return the reminder. Good for deciding if number is even or odd
    
    # Basic functions
    print(f"pow(5, 2) = {pow(5, 2)}")     # 25 --> like doing 5**2
    print(f"abs(-50) = {abs(-50)}")       # 50
    print(f"round(5.46) = {round(5.46)}")   # 5
    print(f"round(5.468, 2) = {round(5.468, 2)}")  # 5.47 --> round to nth digit
    print(f"bin(512) = {bin(512)}")       # '0b1000000000' --> binary format
    print(f"hex(512) = {hex(512)}")       # '0x200' --> hexadecimal format
    
    age = input("How old are you?")
    age = int(age)
    
    pi = input("What is the value of pi?")
    pi = float(pi)
    
    print("\n2. STRINGS")
    print("-" * 30)
    
    print(f"type('Helloooooo') = {type('Helloooooo')}")
    
    print("'I\\'m thirsty'")
    print("\"I'm thirsty\"")
    print("\"\\n\"")
    print("\"\\t\"")  
    
    name = 'John Doe'
    print(f"'Hey you!'[4] = {'Hey you!'[4]}")
    print(f"name = '{name}'")
    print(f"name[2] = {name[2]}")
    print(f"name[:] = {name[:]}")
    print(f"name[1:] = {name[1:]}")
    print(f"name[:1] = {name[:1]}")
    print(f"name[-1] = {name[-1]}")
    print(f"name[::1] = {name[::1]}")
    print(f"name[::-1] = {name[::-1]}")
    print(f"name[0:7:2] = {name[0:7:2]}")
    
    # String operations
    print(f"'Hi there ' + 'Timmy' = {'Hi there ' + 'Timmy'}")  # Hi there Timmy --> This is called string concatenation
    print(f"'*' * 10 = {'*' * 10}")               # **********
    
    # String methods
    print(f"len('turtle') = {len('turtle')}")      # 6
    
    print("' I am alone '.strip() = 'I am alone'")
    print("'On an island'.strip('d') = 'On an islan'")
    print("'but life is good!'.split() = ['but', 'life', 'is', 'good!']")
    print("'Help me'.replace('me', 'you') = 'Help you'")
    print("'Need to make fire'.startswith('Need') = True")
    print("'and cook rice'.endswith('rice') = True")
    print("'bye bye'.index('e') = 2")
    print("'still there?'.upper() = 'STILL THERE?'")
    print("'HELLO!'.lower() = 'hello?!'")
    print("'ok, I am done.'.capitalize() = 'Ok, I am done.'")
    print("'oh hi there'.find('i') = 4")
    print("'oh hi there'.count('e') = 2")
    
    name1 = 'Andrei'
    name2 = 'Sunny'
    print(f"f'Hello there {{name1}} and {{name2}}' = \"Hello there {name1} and {name2}\"")
    print(f"'Hello there {{}} and {{}}'.format(name1, name2) = \"Hello there {name1} and {name2}\"")
    print(f"'Hello there %s and %s' % (name1, name2) = \"Hello there {name1} and {name2}\"")
    
    word = 'reviver'
    p = bool(word.find(word[::-1]) + 1)
    print(f"p = {p}")
    
    print("\n3. BOOLEAN")
    print("-" * 30)
    
    print(f"bool(True) = {bool(True)}")
    print(f"bool(False) = {bool(False)}")
    
    print(f"bool(None) = {bool(None)}")
    print(f"bool(False) = {bool(False)}")
    print(f"bool(0) = {bool(0)}")
    print(f"bool(0.0) = {bool(0.0)}")
    print(f"bool([]) = {bool([])}")
    print(f"bool({{}}) = {bool({})}")
    print(f"bool(()) = {bool(())}")
    print(f"bool('') = {bool('')}")
    print(f"bool(range(0)) = {bool(range(0))}")
    print(f"bool(set()) = {bool(set())}")
    
    print("\n4. LISTS")
    print("-" * 30)
    
    my_list = [1, 2, '3', True]
    print(f"my_list = {my_list}")
    print(f"len(my_list) = {len(my_list)}")
    print(f"my_list.index('3') = {my_list.index('3')}")
    print(f"my_list.count(2) = {my_list.count(2)}")
    
    print(f"my_list[3] = {my_list[3]}")
    print(f"my_list[1:] = {my_list[1:]}")
    print(f"my_list[:1] = {my_list[:1]}")
    print(f"my_list[-1] = {my_list[-1]}")
    print(f"my_list[::1] = {my_list[::1]}")
    print(f"my_list[::-1] = {my_list[::-1]}")
    print(f"my_list[0:3:2] = {my_list[0:3:2]}")
    
    # Add to list
    my_list_copy = my_list.copy()
    my_list_copy + 2                               # [1, 2, '3', True, 1, 2, '3', True] - doesn't mutate original
    print(f"my_list + [100] = {my_list + [100]}")  # [1, 2, '3', True, 100] --> doesn't mutate original list, creates new one
    
    my_list_test = my_list.copy()
    my_list_test.append(100)
    print(f"my_list.append(100) result: {my_list_test}")  # None --> Mutates original list to [1, 2, '3', True, 100]
    # Or: <list> += [<el>]
    
    my_list_extend = my_list.copy()
    my_list_extend.extend([100, 200])
    print(f"my_list.extend([100, 200]) result: {my_list_extend}")  # None --> Mutates original list to [1, 2, '3', True, 100, 200]
    
    my_list_insert = my_list.copy()
    my_list_insert.insert(2, '!!!')
    print(f"my_list.insert(2, '!!!') result: {my_list_insert}")  # None --> [1, 2, '!!!', '3', True] - Inserts item at index and moves the rest to the right.
    
    print(f"' '.join(['Hello', 'There']) = {' '.join(['Hello', 'There'])}")  # 'Hello There' --> Joins elements using string as separator.
    
    # Copy a list
    basket = ['apples', 'pears', 'oranges']
    new_basket = basket.copy()
    new_basket2 = basket[:]
    print(f"new_basket = {new_basket}")
    print(f"new_basket2 = {new_basket2}")
    
    remove_list = [1, 2, 3]
    popped = remove_list.pop()
    print(f"[1,2,3].pop() = {popped}")
    
    remove_list2 = [1, 2, 3]
    popped2 = remove_list2.pop(1)
    print(f"[1,2,3].pop(1) = {popped2}")
    
    remove_list3 = [1, 2, 3]
    remove_list3.remove(2)
    print(f"[1,2,3].remove(2) result: {remove_list3}")
    
    clear_list = [1, 2, 3]
    clear_list.clear()
    print(f"[1,2,3].clear() result: {clear_list}")
    
    del_list = [1, 2, 3]
    del del_list[0]
    print(f"del [1,2,3][0] result: {del_list}")
    
    order_list1 = [1, 2, 5, 3]
    order_list1.sort()
    print(f"[1,2,5,3].sort() result: {order_list1}")
    
    order_list2 = [1, 2, 5, 3]
    order_list2.sort(reverse=True)
    print(f"[1,2,5,3].sort(reverse=True) result: {order_list2}")
    
    order_list3 = [1, 2, 5, 3]
    order_list3.reverse()
    print(f"[1,2,5,3].reverse() result: {order_list3}")
    
    print(f"sorted([1,2,5,3]) = {sorted([1,2,5,3])}")
    print(f"list(reversed([1,2,5,3])) = {list(reversed([1,2,5,3]))}")
    
    numbers = [1, 2, 5, 3]
    print(f"1 in [1,2,5,3] = {1 in numbers}")
    print(f"min([1,2,3,4,5]) = {min([1,2,3,4,5])}")
    print(f"max([1,2,3,4,5]) = {max([1,2,3,4,5])}")
    print(f"sum([1,2,3,4,5]) = {sum([1,2,3,4,5])}")
    
    mList = [63, 21, 30, 14, 35, 26, 77, 18, 49, 10]
    first, *x, last = mList
    print(f"first = {first}")
    print(f"last = {last}")
    
    print("\n5. DICTIONARIES")
    print("-" * 30)
    
    my_dict = {'name': 'John Doe', 'age': 25, 'magic_power': False}
    print(f"my_dict = {my_dict}")
    
    print(f"my_dict['name'] = {my_dict['name']}")
    print(f"len(my_dict) = {len(my_dict)}")
    print(f"list(my_dict.keys()) = {list(my_dict.keys())}")
    print(f"list(my_dict.values()) = {list(my_dict.values())}")
    print(f"list(my_dict.items()) = {list(my_dict.items())}")
    
    my_dict['favourite_snack'] = 'Grapes'
    print(f"After adding favourite_snack: {my_dict}")
    
    print(f"my_dict.get('age') = {my_dict.get('age')}")
    print(f"my_dict.get('ages', 0) = {my_dict.get('ages', 0)}")
    
    dict_copy = my_dict.copy()
    del dict_copy['name']
    print(f"After del my_dict['name']: {dict_copy}")
    
    dict_copy2 = my_dict.copy()
    popped_value = dict_copy2.pop('name', None)
    print(f"my_dict.pop('name', None) = {popped_value}")
    print(f"Dict after pop: {dict_copy2}")
    
    print("\n6. TUPLES")
    print("-" * 30)
    
    my_tuple = ('apple', 'grapes', 'mango', 'grapes')
    apple, grapes, mango, grapes = my_tuple
    print(f"my_tuple = {my_tuple}")
    print(f"len(my_tuple) = {len(my_tuple)}")
    print(f"my_tuple[2] = {my_tuple[2]}")
    print(f"my_tuple[-1] = {my_tuple[-1]}")
    
    try:
        my_tuple[1] = 'donuts'
    except TypeError as e:
        print(f"Error trying to modify tuple: {e}")
        
    try:
        my_tuple.append('candy')
    except AttributeError as e:
        print(f"Error trying to append to tuple: {e}")
    
    print(f"my_tuple.index('grapes') = {my_tuple.index('grapes')}")
    print(f"my_tuple.count('grapes') = {my_tuple.count('grapes')}")
    
    print("\n7. SETS")
    print("-" * 30)
    
    my_set = {1, 100}
    print(f"my_set = {my_set}")
    my_set.add(100)
    print(f"After adding 100 again: {my_set}")
    
    new_list = [1, 2, 3, 3, 3, 4, 4, 5, 6, 1]
    print(f"set(new_list) = {set(new_list)}")
    
    my_set.remove(100)
    print(f"After removing 100: {my_set}")
    
    my_set.add(100)
    my_set.discard(100)
    print(f"After discarding 100: {my_set}")
    
    my_set.clear()
    print(f"After clear: {my_set}")
    
    new_set = {1, 2, 3}.copy()
    print(f"new_set = {new_set}")
    
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    set3 = set1.union(set2)
    set4 = set1.intersection(set2)
    set5 = set1.difference(set2)
    set6 = set1.symmetric_difference(set2)
    
    print(f"set1.union(set2) = {set3}")
    print(f"set1.intersection(set2) = {set4}")
    print(f"set1.difference(set2) = {set5}")
    print(f"set1.symmetric_difference(set2) = {set6}")
    
    print(f"set1.issubset(set2) = {set1.issubset(set2)}")
    print(f"set1.issuperset(set2) = {set1.issuperset(set2)}")
    print(f"set1.isdisjoint(set2) = {set1.isdisjoint(set2)}")
    
    # Frozenset
    # hashable --> it can be used as a key in a dictionary or as an element in a set.
    frozenset_example = frozenset([1, 2, 3])
    print(f"frozenset([1, 2, 3]) = {frozenset_example}")
    
    # ============================================
    # 8. NONE
    # ============================================
    print("\n8. NONE")
    print("-" * 30)
    
    # None este folosit pentru absenta unei valori si poate fi folosit pentru a arata ca nu a fost asignata nicio valoare unui obiect.
    print(f"type(None) = {type(None)}")  # NoneType
    a = None
    print(f"a = {a}")
    
    print("\n" + "=" * 60)
    print("TOATE EXEMPLELE AU FOST IMPLEMENTATE!")
    print("=" * 60)


if __name__ == "__main__":
    main()
