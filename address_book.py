"""
Addressbook.py
An address book program to store details of people i know.
Stuff I'm storing is:
first name
family name
email address
date of birth
[other stuff]

Isaiah Santillan
7/26/18

"""

#### Classes Section
class AddressBook(object):
    """
    AddressBook instances hold and manage a list of people
    """
    def __init__ (self):
        """ Set people attribute to an empty list"""
        self.people = []

    def add_entry(self, new_entry):
        """ Add a new entry to the list of people in the
        address book the new_entry should be an instance
        of the AddressEntry class"""
        self.people.append(new_entry)

class AddressEntry(object):
    """
    AddressEntry instances hold and manage details of a person
    """
    def __init__(self, first_name=None, family_name=None,
                 email_address=None, date_of_birth=None):
        """Initialize attributes first_name,
        family_name abd date_of_birth.
        Each argument should be a string.
        date_of_birth should be of the form "MM, DD, YYYY"
        """
        self.first_name = first_name
        self.family_name = family_name
        self.email_address = email_address
        self.date_of_birth = date_of_birth

    def __repr__(self):
        """
        Given and AddressEntry object self return
        a readable string representation
        """
        template = "AddressEntry(first)_name='%s', "+\
                   "family_name='%s',"+\
                   " email_address='%s',"+\
                   "date_of_birth='%s')"
        return template%(self.first_name, self.family_name,
                         self.email_address, self.date_of_birth)
       

####Functions
        
#### Main Section

if __name__ == "__main__":
    address_book = AddressBook()
    #person1 = AddressEntry() #creates the entry
    #person1.first_name = "Isaiah" # Attribute
    #person1.family_name = "Santillan"
    #person1.date_of_birth = "November 12, 1998"
    #person1.email_address = "Isaiahsantillan297@gmail.com"
    person1 = AddressEntry("Isaiah", "Santillan",
                           "isaiahsantillan297@gmail.com",
                           "November 12, 1998")
    print(person1)
    address_book.add_entry(person1)
    print(address_book.people)
   
    
                           
