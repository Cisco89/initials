def get_initials(fullname):
    """ Given a person's name, returns the person's initials (uppercase) """
    # TODO your code here
    my_initials = ''.join([s[:1] for s in fullname.split(' ')])
    my_initials= my_initials.upper()
    return my_initials

initials = get_initials("francisco garcia")
print("The initials to your full name are", initials)
