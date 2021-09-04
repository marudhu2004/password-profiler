# Set of valid characters for a password
alpha = "abcdefghijklmnopqrstuvwxyz"
numeric = "1234567890"
symbols = "!@#$%^&*()_ "

# The fuction to create the password list based on give coditions
def create_word_list():
    
    # Getting the basic settings 
    settings = {'num': False, 'special': False, "length": (3, 3)}

    # Getting the character set setup
    char_set = alpha + alpha.upper()
    if settings['num']:
        char_set += numeric
    if settings['special']:
        char_set += symbols
    
    # Setting up length variables
    max_len = settings['length'][1]
    min_len = settings['length'][0]

    # Creating the inital string to iterate upon
    password_string = char_set[0] * min_len
    char_pass_index = min_len - 1

    while True:
        password_string = next_pass(len(password_string) - 1, char_set, password_string)
        if len(password_string) > max_len: break
        print(password_string)


# Rcursive function for next char update
def next_pass(char_pass_index, char_set, current_pass):
    
    # In case a new character is needed to be added
    if char_pass_index < 0:
        return char_set[0] + current_pass

    # Getting current char index in char_set
    char_index = char_set.index(current_pass[char_pass_index])
    pass_len = len(current_pass)
    char_set_len = len(char_set)
    
    # Creating new password
    new_char = char_set[(char_index + 1) % char_set_len]
    new_pass = current_pass[0 : char_pass_index] + new_char + current_pass[char_pass_index + 1 : pass_len]
    
    # Checking if the current char needs to be carried again
    if char_index >= char_set_len - 1:
        return next_pass(char_pass_index - 1, char_set, new_pass)
    
    # Returning the new password string
    return new_pass
