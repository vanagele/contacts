contacts = []

while(True):
    response = input('(1)add contact (2)print contacts (3)exit: ')
    if response =='1':
        person_name = input('Name: ')
        person_surname = input('Surname: ')
        person_phone = input('Phone: ')
        person_emai = input('Email: ')

        person_contact = {
            'name': person_name,
            'surname': person_surname,
            'phone': person_phone,
            'email': person_emai
        }
        contacts.append(person_contact)
    elif response == '2':
        print(contacts)
    elif response == '3':
        print('Bye bye!')
        exit()
