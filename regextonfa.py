import thompsons


def menu():
    print("Enter regular expression")
    inputRegex = input()

    print("Enter string to compare")
    inputString = input()

    if thompsons.match(inputRegex, inputString) == True:
        print("MATCH, the regular expression,", inputRegex,", and the string,", inputString,", entered are a match.")

    else:
        print("NO MATCH, the regular expression,", inputRegex,", and the string,", inputString,", entered do not match.")


menu()
