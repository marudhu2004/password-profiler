# Set of valid characters for a password
alpha = "abcdefghijklmnopqrstuvwxyz"
numeric = "1234567890"
symbols = "!@#$%^&*()_ "


# The fuction to create the password list based on give coditions
def create_word_list(out_file, num = False, special = False, min_len = 3, max_len = 3, upper = False, lower = True, char_set=""):
    
    # Getting the character set setup
    charset = ""
    if lower:
        charset += alpha
    if upper:
        charset += alpha.upper()
    if num:
        charset += numeric
    if special:
        charset += symbols

    # Checking if charset is not empty
    if char_set == "":
        print("there must be atleast some characters to create password")
        return

    # If a specific charset is specified
    if char_set:
        charset = char_set
    
    # Creating the inital string to iterate upon
    password_string = char_set[0] * min_len
    char_pass_index = min_len - 1

    # Opening the output file    
    with open(out_file, 'w') as file:
        while True:
            
            # Getting the new password strings
            password_string = next_pass(len(password_string) - 1, charset, password_string)
            
            # Leaving if the last pass reached
            if len(password_string) > max_len: break
            
            # Writing the password to the file
            file.write(password_string+"\n")


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


if __name__ == '__main__':
    create_word_list('out.txt', char_set='1234')