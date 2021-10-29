# Set of valid characters for a password
alpha = "abcdefghijklmnopqrstuvwxyz"
numeric = "1234567890"
symbols = "!@#$%^&*()_ "


# The fuction to create the password list based on give coditions
def create_word_list(out_file, num = False, special = False, min_len = 3, max_len = 3, upper = False, lower = True, char_set=""):

    # Creating the generator object
    password_list = password_list_generator(num, special, min_len, max_len, upper, lower, char_set)

    # Opening the output file    
    with open(out_file, 'w') as file:

        # Writing the passwords to the output file
        try:
            for password in password_list:
                file.write(password + '\n')
        
        except ValueError:
            print('the charset must not be empty plz try with different settings')
            return

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

# Generator version of getting passwords
def password_list_generator(num = False, special = False, min_len = 3, max_len = 3, upper = False, lower = True, char_set=""):
    
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
    if charset == "":
        raise ValueError("there must be atleast 1 character in char set! (check the function settings)")

    # If a specific charset is specified
    if char_set:
        charset = char_set
    
    # Creating the inital string to iterate upon
    password_string = charset[0] * min_len
    char_pass_index = min_len - 1

    # Looping to get the possible combinations
    while True:
            
        # Leaving if the last pass reached
        if len(password_string) > max_len: break

        # Writing the password to the file
        yield password_string
        
        # Getting the new password strings
        password_string = next_pass(len(password_string) - 1, charset, password_string)



# To deal with knowing specific part chars
def with_known_chars(known_chars, symbol, outfile, num = False, special = False, upper = False, lower = True, char_set=""):

    # Getting the mask and length needed to fill
    lenght = len(known_chars)
    mask = [1 if i == symbol else 0 for i in known_chars]
    gen_len = sum(mask)

    # Creating the charset to check if the call is valid
    charset=""
    if lower:
        charset += alpha
    if upper:
        charset += alpha.upper()
    if num:
        charset += numeric
    if special:
        charset += symbols

    # raising an error if there is nothing to substitute with
    if gen_len == 0:
        raise ValueError("there should atleast be one character to be substitute in the password") 
    
    # Raising an error if the symbol is in the charset
    if symbol in charset:
        raise ValueError("The symbol must not be a part of the charset")

    # Creating paswords with the given conditions
    fill_vals = password_list_generator(num , special, gen_len, gen_len, upper, lower, char_set)
    
    # Opening the output file to write to
    with open(outfile, 'w') as file:

        # Going through the list of generated passwords
        for value in fill_vals:
            password = ""
            count = 0
            
            # Assigining the generated characters requires positions
            for i, v in enumerate(mask):
                # If generated value needed
                if v:
                    password += value[count]
                    count += 1

                # If value alreaady known
                else:
                    password += known_chars[i]

            # Saving the generated password
            file.write(password+"\n")


if __name__ == '__main__':
    with_known_chars("max", '~', 'test.txt')