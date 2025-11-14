import sys
import pathlib
import collections

#Create starting items
a0 = []
a1 = []
a2 = []
a3 = []
a4 = []
a5 = []
ra1 = 0
ra2 = 0

pointer = 0

file_pointer_list = []
prepared_instructions = []

test = 0

# function M
def m_function(type):

    global file_pointer_list

    # Addition with reg/imm and reg/imm
    if type == "madd":
        if type(file_pointer_list[2]) == list:
            val_1 = file_pointer_list[2][0]
        else:
            val_1 = file_pointer_list[2]
        if type(file_pointer_list[3]) == list:
            val_1 = file_pointer_list[3][0]
        else:
            val_1 = file_pointer_list[3]
        val_1 = file_pointer_list[2]
        val_2 = file_pointer_list[3]
        file_pointer_list[1].clear()
        file_pointer_list[1].append(val_1 + val_2)

    #Subtraction with reg and reg/imm
    elif type == "msub":
        if type(file_pointer_list[2]) == list:
            val_1 = file_pointer_list[2][0]
        else:
            val_1 = file_pointer_list[2]
        if type(file_pointer_list[3]) == list:
            val_1 = file_pointer_list[3][0]
        else:
            val_1 = file_pointer_list[3]
        val_1 = file_pointer_list[2]
        val_2 = file_pointer_list[3]
        file_pointer_list[1].clear()
        file_pointer_list[1].append(val_1 - val_2)

    reader()

# function J
def j_function(type):

    global pointer

    #CHoose ra and jump to index
    if type == "jjt1":
        pointer = ra1
    
    elif type == "jjt2":
        pointer = ra2

    reader()

# function s
def s_function(type):

    global file_pointer_list

    #Print
    if type == "sprt":
        my_print = file_pointer_list[1][0].str()
        print(my_print)

    #Exit file
    elif type == "sbrk":
        quit()

    #Empty register
    elif type == "semp":
        file_pointer_list[1].clear

    #Copy register
    elif type == "scpy":
        file_pointer_list[1] = file_pointer_list[2]

    reader()

# function L
def l_function(type):

    global file_pointer_list

    #Greater then
    if type == "lgrt":
        val_1 = file_pointer_list[2][0]
        val_2 = file_pointer_list[3][0]
        if val_1 > val_2:
            file_pointer_list[1]()

    #Less then
    elif type == "llst":
        val_1 = file_pointer_list[2][0]
        val_2 = file_pointer_list[3][0]
        if val_1 < val_2:
            file_pointer_list[1]()
    #Equal
    elif type == "leql":
        val_1 = file_pointer_list[2][0]
        val_2 = file_pointer_list[3][0]
        if val_1 == val_2:
            file_pointer_list[1]()

    reader()

#Execute the fileinstructions
def reader():

    global test 
    global pointer
    global file_pointer_list
    global prepared_instructions

    print ("reads pointer", pointer)
    test += 1
    print (test, " times reader run")

    file_pointer_list = prepared_instructions[pointer]
    decide_function = file_pointer_list.split()
    pointer += 1
    print(type(decide_function))
    match decide_function[0]:

        case "madd" | "msub":
            m_function(decide_function)

        case "jjt1" | "jjt2":
            j_function(decide_function[0])
        
        case "sprt" | "sbrk" | "semp" | "scpy":
            s_function(decide_function[0])

        case "lgrt" | "llst" | "leql":
            s_function(decide_function[0])



#Parts taken from bbvv
def main():

    global pointer
    global ra1
    global ra2
    
    counter = 0

    # Check that the proper amount of Command Line Arguments (CLA) are given
    if len(sys.argv) != 2:
        print(
            "\tIncorrect arguemts, command should be\n\t'python3 interpreter.py <filename>'"
        )
    else:
        file = pathlib.Path(str(sys.argv[1]))
        # Make sure the the given file path is a file that exists
        if file.is_file():
            # Make sure the file has the proper prefix.
            if file.suffix != ".ffes":
                print(f"\tGiven file is not of type .ffes")
            else:
                full_instructions = open(sys.argv[1], "r")
                row_split_instruction = full_instructions.readlines()
                for row in row_split_instruction:
                        temp_row = row_split_instruction[counter].rstrip()
                        if temp_row == "ra1":
                            ra1 = pointer
                            pointer += 1
                        elif temp_row == "ra2":
                            ra2 = pointer
                            pointer += 1
                        elif temp_row != "":
                            prepared_instructions.append(temp_row)
                            pointer += 1
                        counter += 1
                full_instructions.close()
                print (prepared_instructions[0])
                pointer = 0
                reader()
        else:   
            print(f"\tFile: {file} does not exist")


# Python stuff.
if __name__ == "__main__":
    main()
