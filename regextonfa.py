import thompsons


def menu():
    choice = ''

    while choice != "-1":
        print("Enter 1 to compare a regular expresion to a string")
        print("Enter -1 to exit")
        choice = input()

        if choice == "1":
            print("Enter regular expression")
            inputRegex = input()

            print("Enter string to compare")
            inputString = input()

            if thompsons.match(inputRegex, inputString) == True:
                print("MATCH, the regular expression,", inputRegex, ", and the string,", inputString, ", entered are a match.")
            else:
                print("NO MATCH, the regular expression,", inputRegex, ", and the string,", inputString, ", entered do not match.")

menu()
