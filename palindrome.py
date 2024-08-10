def is_palindrome(string):
    if string == string[::-1]:
        print('The string is a Palindrome')
    else:
        print('The string is not a Palindrome')

string = 'MADAM'
is_palindrome(string)