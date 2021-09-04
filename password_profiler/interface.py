# Main function
def main():
    
    # Giving the starting banner
    banner()

    # Asking the user to choose what to do
    option = input("what do you want to do? (i for interactive mode, l for password list generation, h for help, e for exit)\n>")
    if option == 'i':
        interactive()
    elif option == 'l':
        create_word_list()
    elif option == 'h':
        print_help()
    elif option == 'e':
        print("bye")
        exit()
    else:
        print("invalid option!, exiting")


# The help page
def print_help():
    pass


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