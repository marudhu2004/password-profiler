import generator

# Main function
def main():
    
    # Giving the starting banner
    banner()

    # Asking the user to choose what to do
    option = input("what do you want to do? (i for interactive mode, l for password list generation, h for help, e for exit, k for mask based generation)\n>>> ")
    if option == 'i':
        interactive()

    # Creating the basic wordlist
    elif option == 'l':
        create_word_list()

    # Mask based list generation call
    elif option == 'k':
        mask_based()
    
    # Printing the help
    elif option == 'h':
        print_help()
    
    # Existing the program
    elif option == 'e':
        print("bye")

    # Exiting if invalid val called
    else:
        print("invalid option!, exiting")


# The help page
def print_help():
    pass


# Mask terminal prompt
def mask_based():
    
    # Setting up the generator
    gen = generator.PasswordGenerator()

    # Getting the input necessary to generate list
    base = input("the base pass (the known parts and symbols):\n>>> ")
    symbols = input("the symbols in the password:\n>>> ")
    
    # Checking if the symbols are valid
    for i in symbols:
        if i not in base:
            print('key not in base')
            exit()
    
    # Keeping the symbols clean
    unique = ''
    for i in symbols:
        if i not in unique:
            unique += i
    
    symbols = unique
    mapping = {}

    # Getting the mapping values
    print('\nMapping:')
    for i in symbols:
        vals = input(f"values for \"{i}\":\n>>> ")
        mapping[i] = vals

        # Adding a new line
        print()

    outfile = input("Output file name (or path):\n>>> ")

    gen.list_with_masks(base, mapping, outfile)
    print("File generated!")


def create_word_list():

    # Charset validator
    def charset_validator(txt):
        
        val = input(txt)
        val = val.upper()
        
        while True:
        
            # Giving true or false
            if val == 'Y':
                return True
            elif val == 'N':
                return False
            else:
                print("invalid option!")
                val = input('>>>').upper()

    # Length values
    min_len = int(input("minimum length:"))
    max_len = int(input("maximum length:"))

    # Getting if charset already known
    charset = input("have a specific set of character in mind (empty if none)?\n>>> ")
    
    # Setting up the generator
    gen = generator.PasswordGenerator(min_len=min_len, max_len=max_len)

    # Setting up charset
    if not charset:
        upper = charset_validator("Has upper case characters [Y or N]:\n>>> ")
        lower = charset_validator("Has lower case characters [Y or N]:\n>>> ")
        numeric = charset_validator("Has numerical characters [Y or N]:\n>>> ")
        specials = charset_validator("Has special characters [Y or N]:\n>>> ")

        # Updating the generator
        gen.set_charset(numeric, specials, upper, lower)
    
    # Updating the generator if a charset is already given
    else:
        gen.charset = charset
    
    # Getting the output file name and running the generator
    outfile = input("\nOutput file name (or path):\n>>> ")
    gen.create_word_list(outfile)
    print("done!")


# The Start up banner
def banner():
    print(r"""
==================================================================================================================
|| +----------------------------------------------------------------------------------------------------------+ ||
|| *      ____  ___   ___________       ______  ____  ____     ____  ____  ____  ____________    __________   * ||
|| *     / __ \/   | / ___/ ___/ |     / / __ \/ __ \/ __ \   / __ \/ __ \/ __ \/ ____/  _/ /   / ____/ __ \  * ||
|| *    / /_/ / /| | \__ \\__ \| | /| / / / / / /_/ / / / /  / /_/ / /_/ / / / / /_   / // /   / __/ / /_/ /  * ||
|| *   / ____/ ___ |___/ /__/ /| |/ |/ / /_/ / _, _/ /_/ /  / ____/ _, _/ /_/ / __/ _/ // /___/ /___/ _, _/   * ||
|| *  /_/   /_/  |_/____/____/ |__/|__/\____/_/ |_/_____/  /_/   /_/ |_|\____/_/   /___/_____/_____/_/ |_|    * ||
|| *                                                                                                          * ||
|| +----------------------------------------------------------------------------------------------------------+ ||
==================================================================================================================                                                                                                      
""", end="")


if __name__ == "__main__":
    main()