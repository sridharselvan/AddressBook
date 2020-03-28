"""
This is used to add, update, retrieve and delete details of contacts in files.
"""
from read_write_file import ReadWriteFile


class AddressBook(object):
    """Used to maintain details of contacts"""
    read_write = ReadWriteFile()
    def __init__(self, file_name):
        """Init method to store contact information"""
        self.file_name = file_name

    def add_contact(self, **kwargs):
        """."""
        my_contacts = {
            'Name': kwargs['name'],
            'Email': kwargs['email'],
            'Phone': kwargs['phone'],
            'Address': kwargs['address']
        }
        is_name_exists = self.check_name_exists(kwargs['name'])
        if not is_name_exists:
            AddressBook.read_write.append_to_file(self.file_name, my_contacts)
            return 'Contact added successfully.'

        return '{} already exists in the contact list.'.format(name)

    def check_name_exists(self, name, position=None):
        """."""
        address_list = AddressBook.read_write.read_from_file(self.file_name)
        for idx, row in enumerate(address_list):
            if row.get('Name') == name:
                return (True, idx) if position else True
        return (False, 0) if position else False

    def update_contact(self, **kwargs):
        """."""
        is_name_exists, idx = my_book.check_name_exists(kwargs['contact_to_modify'], position=True)
        if not is_name_exists:
            return "{} not found in the list.".format(kwargs['contact_to_modify'])

        is_book_altered = False
        address_list = AddressBook.read_write.read_from_file(self.file_name)
        if kwargs.get('name', ''):
            address_list[idx]['Name'] = kwargs['name']
            is_book_altered = True
        elif kwargs.get('address', ''):
            address_list[idx]['Address'] = kwargs['address']
            is_book_altered = True
        elif kwargs.get('email', ''):
            address_list[idx]['Email'] = kwrgs['email']
            is_book_altered = True
        elif kwargs.get('phone', ''):
            address_list[idx]['Phone'] = kwargs['phone']
            is_book_altered = True

        if is_book_altered:
            AddressBook.read_write.write_to_file(self.file_name, address_list)
            return "Contact book updated successfully."

    def search_contacts(self, contact_to_search):
        """."""
        address_list = AddressBook.read_write.read_from_file(self.file_name)
        is_name_exists, position = self.check_name_exists(
            contact_to_search, position=True)
        if is_name_exists:
            return address_list[position]
        
        return "{} not found in the contact list".format(contact_to_search)

    def display_contacts(self):
        """."""
        address_list = AddressBook.read_write.read_from_file(self.file_name)
        result = []
        if not address_list:
            return "No records Found."
        
        return address_list


if __name__ == '__main__':
    my_book = AddressBook('my_address_book.csv')
