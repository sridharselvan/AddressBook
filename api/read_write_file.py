"""
Utility class to read and write from file
"""
import csv

class ReadWriteFile(object):

    def append_to_file(self, file_name, my_contacts):
        """."""
        headers = my_contacts.keys()
        with open(file_name, 'a') as csvfile: 
            csvwriter = csv.writer(csvfile)
            writer = csv.DictWriter(csvfile, delimiter=',', lineterminator='\n', fieldnames=headers)
            if not csvfile.tell():
                writer.writeheader() 
            writer.writerow(my_contacts)

    def read_from_file(self, file_name):
        """"."""
        contacts = []
        try:
            with open(file_name, 'r') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=',')
                for each in reader:
                    contacts.append(each)
            return contacts
        except OSError as e:
            return contacts

    def write_to_file(self, file_name, my_contacts):
        """."""
        headers = my_contacts[0].keys()
        with open(file_name, 'w') as csvfile: 
            csvwriter = csv.writer(csvfile)
            writer = csv.DictWriter(csvfile, delimiter=',', lineterminator='\n', fieldnames=headers)
            if not csvfile.tell():
                writer.writeheader()
            writer.writerows(my_contacts)
