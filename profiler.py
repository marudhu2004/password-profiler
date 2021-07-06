# Set of valid characters for a password
alpha = "abcdefghijklmnopqrstuvwxyz"
numeric = "1234567890"
symbols = "!@#$%^&*()_ "


# Main function
def main():
    
    # Giving the starting banner
    banner()

    # Asking the user to choose what to do
    option = input("what do you want to do? (i for interactive mode, l for password list generation, h for help, e for exit)\n>")
    if option == 'i':
        interactive()
    elif option == 'l':
        creat_word_list()
    elif option == 'h':
        print_help()
    elif option == 'e':
        print("bye")
        exit()
    else:
        print("invalid option!")


# The function to run in interactive mode and make a customized password list
def interactive():

    # The basic info dict
    target_info = {}

    # Getting basic info
    target_info["name"] = input("Name of the target:\n> ")
    target_info["nick_name"] = input("Nick name of the target:\n> ")
    target_info["DOB"] = input("Date Of Birth(dd-mm-yyyy):\n> ")
    target_info["lucky_num"] = input("Lucky Number of the target:\n> ")

    # Printing the collected info
    for key, value in target_info.items():
        print(f"{key}: {value}")


# The fuction to create the password list based on give coditions
def creat_word_list():
    pass


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


# Execution part
if __name__ == "__main__":
    main()