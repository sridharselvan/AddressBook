from address_book import AddressBook

def main():
    my_book = AddressBook('my_address_book.csv')
    while True:
        print('1. To Add Contacts \n2. For Searching a Contact\n3. For Modifying a Contact\n4. To Display Contacts\n5. To Exit')
        choice = int(input('Enter your choice: '))
        if choice == 1:
            user_input = get_user_input()
            result = my_book.add_contact(**user_input)
            print(result)
        elif choice == 2:
            contact_name = input("Enter the name to search:")
            print(my_book.search_contacts(contact_name))
        elif choice == 3:
            user_input = {}
            option_dict = {'1': 'name', '2': 'address', '3': 'email', '4': 'phone'}
            user_input['contact_to_modify'] = str(input('Enter the name of the contact to modify (Only enter full name): '))
            print('1. To modify name\n2. To modify address\n3. To modify email,\n4. To modify phone: ')
            option = input('Enter your choice: ')
            if option_dict.get(option, ''):
                user_input[option_dict[option]] = input("Enter the values to modify:  ")
                print(my_book.update_contact(**user_input))                
            else:
                 print('Invalid Option. Try Again!')
        elif choice == 4:
            res = my_book.display_contacts()
            for each in res:
                print('Name: {0} | Email: {1} | Phone: {2} | Address: {3}'.format(each['Name'],
                                                                              each['Email'],
                                                                              each['Phone'],
                                                                              each['Address']))
        elif choice == 5:
            exit()
        else:
            print('Invalid Option. Try Again!')

def get_user_input():
    """."""
    user_input = {}
    user_input['name'] = input('Enter Name: ')
    user_input['email'] = input('Enter Email: ')
    user_input['phone'] = input('Enter Phone: ')
    user_input['address'] = input('Enter Address: ')
    return user_input

if __name__ == '__main__':
    main()