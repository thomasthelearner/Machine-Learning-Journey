import random
import functools

prefixes = ['Mystic', 'Golden', 'Dark', 'Shadow', 'Silver']
suffixes = ['storm', 'song', 'fire', 'blade', 'whisper']

def capitalize_suffix(name):
    return name.capitalize()

capitalize_suffix_list = list(map(capitalize_suffix, suffixes))

def create_fantasy_name(prefixes, suffixes):
    return random.choice(prefixes) + ' ' + random.choice(suffixes)

random_names = [create_fantasy_name(prefixes, capitalize_suffix_list) for _ in range(10)]

def fire_in_name(name):
    if 'fire' in name.lower():
        return True
    else:
        return False

def concatenate_names(name1, name2):
    return name1 + ' ' + name2 + '\n'

def filter_names_with_fire(random_names):
    return list(filter(fire_in_name, random_names))

def combine_names(acc, names):
    return functools.reduce(concatenate_names, names, acc)

def display_name_info():
    print("Generated Fantasy Names: ")
    for name in random_names:
        print(name)
    if filter_names_with_fire(random_names):
        print("\nNames containing 'fire':")
        for name in filter_names_with_fire(random_names):
            print(name)
    print("\nConcatenated Names: ")
    print(combine_names("", random_names))

display_name_info()
