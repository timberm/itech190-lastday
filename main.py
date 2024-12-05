
def print_list_reverse(lyst):
    print(lyst[-1::-1])

def print_list(lyst): 
    print(lyst)

def print_list_index(lyst, index):
    print(lyst[index])

def print_list_slice(lyst, start, stop):
    print(lyst[start:stop])

def main():
    my_list = [
        'Case', 'Shandell', 'Timber', 'Justin'
    ]
    
    print_list(my_list)
    print_list_reverse(my_list)
    print_list_index(my_list, 0)
    print_list_slice(my_list, 0, 2)


if __name__ == "__main__":
    main()