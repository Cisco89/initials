def get_initials(fullname):
    """ Given a person's name, returns the person's initials (uppercase) """
    # TODO your code here
    my_initials = ''
    for index in fullname.split(' '):
        my_initials += index[0]
    return my_initials.upper()
    
def main():
    initials = get_initials(input("What is your name?"))
    print("The initials to your full name are", initials)

if __name__ == '__main__':
    main()
