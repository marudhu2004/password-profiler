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
    
    mapping = {}

    # Getting the mapping values
    print('Mapping:')
    for i in symbols:
        vals = input(f"values for \"{i}\":\n>>> ")
        mapping[i] = vals

    outfile = input("Output file name (or path):\n>>> ")

    gen.list_with_masks(base, mapping, outfile)
    print("File generated!")


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