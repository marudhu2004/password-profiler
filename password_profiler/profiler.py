# The function to run in interactive mode and make a customized password list
def interactive():

    # The basic info dict
    target_info = {}

    # Getting basic info
    target_info["name"] = input("Name of the target:\n>>> ")
    target_info["nick_name"] = input("Nick name of the target:\n>>> ")
    target_info["DOB"] = input("Date Of Birth(dd-mm-yyyy):\n>>> ")
    target_info["lucky_num"] = input("Lucky Number of the target:\n>>> ")

    # Printing the collected info
    for key, value in target_info.items():
        print(f"{key}: {value}")


# Execution part
if __name__ == "__main__":

    create_word_list()
    # main()