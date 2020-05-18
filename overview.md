# Overview

## Introduction
This purpose of this repository is to build a non-deterministic finite automaton (NFA) from a regular expression and can use the NFA to check if the regular expression matches any given string of text. The repository contains "shunting.py" which is the shunting-yard algorithm. "thompsons.py" is Thompson's construction. "regextonfa.py" is where the user can compare a regular expression to a string.

## Run
To download Python, go to https://www.python.org/downloads/ and download Python for your respective operating system and after you through the installation setup, download the repository and use the following command:
``` python regextonfa.py ```

For help enter ``` python commands.py --help ``` in the command line. To compare a regular expression to a string using one line in the command line use:
``` python commands.py -r "[regular expression]" -s "[string]" ``` <br/>
or <br/>
``` python commands.py -s "[string]" -r "[regular expression]" ```
This is done using the "argparse" package.

## Test
The tests are done in the "tests.py" using "unittest", which a unit testing framework. The tests are done importing the "unittest" library. The tests call "assertEqual", "assertTrue" or "assertFalse" which all call "thompsons.match" from the "thompsons.py" to compare an inputted regular expression to the string and whether they match or not. The tests consist of three methods, one to test whether the test equals true or false, one to test if it equals true and one to test if it equals false. The tests are run by entering the following command:
``` python tests.py ```

If all the tests were successful then "OK" should be printed in the command line along with how many methods were declared.

## Algorithm
(For a more in-depth explanation look in the "README.MD" file.)
The shunting-yard algorithm is used to convert an infix to postfix notation. Infix notation is where an operator is between operands, for example, 2 + 2. Postfix is where an operator is after the operands, for example, 2 2 +. The "shunting.py" file is used to do this a newer function is declared in "thompsons.py".

The "compile" function takes an infix parameter. The infix is then entered in the "shunt" function to return a postfix. A stack is declared for the NFAs. A while loop then goes through the postfix expression checking, using "if" and "elif" statements, if an operator (".", "|", "*", "+", "?") is found. For example, if "." or concatenation is found, two fragments will be popped off the stack, the first fragments' accept state will be pointed at the others start state, then the new start state is the second fragment while the new accept state is the first fragment. The "followes" function adds a state to a set and follows all the epsilon arrows. The match function is used to check if the regular expression and the string match. It will return True if and only if the regular expression fully matches the string s. It returns false otherwise.

## References
See "Resources Used" in "README.MD".
