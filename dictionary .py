monthConversions = {
    'Jan': 'january',
    'Feb': 'Febuary',
    'Mar': 'March',
    'Apr': 'April',
    'Nov': 'November',
                # this is a set of words that will be used to help store different types of data.
                # you can also store numbers to specify different types of information.
                # dictionary is a list words or numbers that have been assigned variable.

#print(monthConversions['Feb'])
print(monthConversions.get('Apr')) # this command allows you to access the dictionary, it grabs the information that -
                                # and then runs the code through the terminal
print(monthConversions.get('Dec', 'the key not found')) # any variable that is incorrect or doesn't show up in the dictionary will ~
                                                # give an alert that the key cannot be found.
                                                # This feature is useful if you're trying to declare a certain variable