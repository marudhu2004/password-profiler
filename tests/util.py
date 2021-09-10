
# Function to check if the files are identical
def check_file(self, out_file, test_file):

    # Opening the output and test case files
    with open(out_file, 'r') as created_file:
        with open(test_file, 'r') as case_file:

            # Reading the password lists
            gen_pass_list = created_file.readline()
            test_pass_list = case_file.readline()

            # Checking if files are of equal length
            self.assertEquals(len(gen_pass_list), len(test_pass_list))

            # Going over all the passwords on the password list
            for i in range(len(test_pass_list)):
                
                # Reading the passwords from the list
                gen_pass = gen_pass_list[i]
                test_pass = test_pass_list[i]
            
                # Checking if the passwords match
                self.assertEquals(gen_pass, test_pass)