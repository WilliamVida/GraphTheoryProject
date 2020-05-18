# Graph Theory Project
By William Vida <br/>
Student ID: G00356773

## Problem Statement
>You must write a program in the Python programming language that can build a non-deterministic finite automaton (NFA) from a regular expression, and can use the NFA to check if the regular expression matches any given string of text.

## Deployment
Clone the repository with:
``` git clone https://github.com/WilliamVida/GraphTheoryProject ```

Assuming Python is downloaded, enter the project folder and run the "regextonfa.py" file or enter the following command:
``` python regextonfa.py ```

## Research & Development
### Non-Deterministic Finite Automaton
What is a non-deterministic finite automaton (NFA)?
[Wikipedia](https://en.wikipedia.org/wiki/Nondeterministic_finite_automaton) describes a non-deterministic finite automaton as a
> finite-state machine is called a deterministic finite automaton (DFA), if each of its transitions is uniquely determined by its source state and input symbol, reading an input symbol is required for each state transition.

### Regular Expression
What is a regular expression?
[Wikipedia](https://en.wikipedia.org/wiki/Regular_expression) describes a regular expression as a
> sequence of characters that define a search pattern. Usually such patterns are used by string searching algorithms for "find" or "find and replace" operations on strings, or for input validation. It is a technique developed in theoretical computer science and formal language theory. 

An example of a regular expression for [validating an email address](https://www.geeksforgeeks.org/write-regular-expressions/) would be: <br/>
``` ^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$ ``` <br/>
The string "example@email.com" would validate the regular expression above while the strings "example@@email.com" and "'example'@email.com" would not.

### Converting a Regular Expression to a Non-Deterministic Finite Automaton
#### Shunting-yard algorithm
The [shunting-yard algorithm](https://en.wikipedia.org/wiki/Shunting-yard_algorithm) is a 
> method for parsing mathematical expressions specified in infix notation. It can produce either a postfix notation string, also known as Reverse Polish notation (RPN), or an abstract syntax tree (AST). The algorithm was invented by Edsger Dijkstra and named the "shunting yard" algorithm because its operation resembles that of a railroad shunting yard.

[Infix](https://en.wikipedia.org/wiki/Infix_notation) is 
> the notation commonly used in arithmetical and logical formulae and statements. It is characterized by the placement of operators between operands—"infixed operators"—such as the plus sign in 2 + 2.

[Postfix](https://en.wikipedia.org/wiki/Reverse_Polish_notation) is a
> mathematical notation in which operators follow their operands, in contrast to Polish notation (PN), in which operators precede their operands. It does not need any parentheses as long as each operator has a fixed number of operands.

The [procedure used](https://brilliant.org/wiki/shunting-yard-algorithm/) is as follows:
-   Expressions are parsed left to right.
-   Each time a number or operand is read, we push it to the stack.
-   Each time an operator comes up, we pop the required operands from the stack, perform the operations, and push the result back to the stack.
-   We are finished when there are no tokens (numbers, operators, or any other mathematical symbol) to read. The final number on the stack is the result.


[Consider the following infix notations:](https://brilliant.org/wiki/shunting-yard-algorithm/)
> 4+18/(9-3).

Now we know that the answer to this from the rule or order of operations is 77.

We have not seen it yet, given the above infix notation, that the shunting yard algorithm will output the reverse polish notation as
> 4,18,9,3,−,/,+.

Note that the commas are not part of the reverse polish, but used to separate each token.

Using the procedure for reverse polish,
![procedure for reverse Polish](https://ds055uzetaobb.cloudfront.net/brioche/uploads/owlqbSo3hD-c1f3db0cf4738e82ea1535ccc835bb7f747e7abb.jpg?width=1200)

In steps aa to dd, we push the numbers in reverse polish expression into the stack. In step ee, where we have reached the operator sign (-)(−), we pop the two numbers involved, perform the operation 9-3=69−3=6, and push it back to the stack. Next is the operator sign (/)(/), where we pop the 66 and 1818 and perform the operation 18/6=318/6=3 and push it to the stack. We continue with the procedure until we are left with a single number that is 77.


To [build the algorithm](https://brilliant.org/wiki/shunting-yard-algorithm/), we will need

- 1 stack for operations
- 1 queue of the output
- 1 array (or other list) of tokens.

A pseudocode of the algorithm is as follows:
```
While there are tokens to be read:
	Read a token
	If it's a number add it to queue
	If it's an operator
		While there's an operator on the top of the stack with greater precedence:
			Pop operators from the stack onto the output queue
		Push the current operator onto the stack
	If it's a left bracket push it onto the stack
	If it's a right bracket 
		While there's not a left bracket at the top of the stack:
			Pop operators from the stack onto the output queue.
		Pop the left bracket from the stack and discard it
While there are operators on the stack, pop them to the queue
```

#### Thompson's construction
[Thompson's construction](https://en.wikipedia.org/wiki/Thompson%27s_construction) is a
> method of transforming a regular expression into an equivalent nondeterministic finite automaton (NFA). This NFA can be used to match strings against the regular expression. This algorithm is credited to Ken Thompson.

##### Operators
#####  "."
The [full stop](http://www.emerson.emory.edu/services/editors/ne/Regular_Expressions.html) is a special character that matches anything except a newline. Using concatenation, we can make regular expressions like `a.b` which matches any three-character string which begins with "a" and ends with "b". <br/>
![full stop](https://swtch.com/~rsc/regexp/fig15.png)

#####  "|"
The [vertical bar](http://www.emerson.emory.edu/services/editors/ne/Regular_Expressions.html) specifies an alternative. Two regular expressions a and b with "|" in between (`a|b`) form an expression that matches anything that either a or b will match. Thus, `foo|bar` matches either "foo" or "bar" but no other string. "|" applies to the largest possible surrounding expressions. Only a surrounding "( ... )" grouping can limit the grouping power of "|". <br/>
![vertical bar](https://swtch.com/~rsc/regexp/fig16.png)

##### "*"
The [asterisk](https://en.wikipedia.org/wiki/Regular_expression) indicates  _zero or more_  occurrences of the preceding element. For example,  `ab*c`  matches "ac", "abc", "abbc", "abbbc", and so on. <br/>
![asterisk](https://swtch.com/~rsc/regexp/fig18.png)

##### "+"
The [plus sign](https://en.wikipedia.org/wiki/Regular_expression) indicates  _one or more_  occurrences of the preceding element. For example,  `ab+c`  matches "abc", "abbc", "abbbc", and so on, but not "ac". <br/>
![plus sign](https://swtch.com/~rsc/regexp/fig19.png)

##### "?"
The [question mark](https://en.wikipedia.org/wiki/Regular_expression) indicates _zero or one_ occurrences of the preceding element. For example, `colou?r` matches both "color" and "colour". <br/>
![question mark](https://swtch.com/~rsc/regexp/fig17.png)

#### How the Code Works
#### The State Class
Every state has 0, 1, or 2 edges from it. Every edge has a label and none means epsilon.

#### The Fragment Class
NFA fragments have a start state and an accept state. The class has a constructor where the variables, start and accept, are associated with the current instance.

#### The shunt Function
The "shunt" function is based on the shunting-yard algorithm. The function takes an infix regular expression parameter and will return it in postfix. A dictionary of operators based on their precedence is declared. The infix is looped through a while loop checking if any operators are found, if an operator is found, then it is added to the stack. For example, if the infix "A * B + C" is entered then the postfix should be "A B * C +".

#### The compile Function
The "compile" function takes an infix parameter. The infix is then entered in the "shunt" function to return a postfix. A stack is declared for the NFAs. A while loop then goes through the postfix expression checking, using "if" and "elif" statements, if an operator (".", "|", "*", "+", "?") is found. For example, if "." or concatenation is found, two fragments will be popped off the stack, the first fragments' accept state will be pointed at the others start state, then the new start state is the second fragment while the new accept state is the first fragment.

#### The followes Function
The "followes" function adds a state to a set and follows all the epsilon arrows.

#### The match Function
The match function is used to check if the regular expression and the string match. It will return True if and only if the regular expression fully matches the string s. It returns false otherwise.

#### Resources Used
https://web.microsoftstream.com/video/f0a890b2-c28a-40d3-8175-adfb005260ed - A video explaining Thompson's construction. <br/>
https://web.microsoftstream.com/video/a29536d4-e975-4172-a470-40b4fe28866e - A video explaining the shunting-yard algorithm by hand. <br/>
https://web.microsoftstream.com/video/781325b2-b4b9-461e-88cc-c5bf37e977eb - A video coding the shunting-yard algorithm in Python. <br/>
https://web.microsoftstream.com/video/3be78704-8cc5-43f1-9be5-68b2e92c8d56 - A video coding classes for states, edges, and NFA fragments in Python for "thompsons.py". <br/>
https://web.microsoftstream.com/video/77e5ecd7-96c5-43ba-a11e-8399d44c87c9 - A video building fragments of automata using the construction. <br/>
https://web.microsoftstream.com/video/f4bc3634-b94f-4c15-b2c1-70cccd874c54 - A video using the automaton to match strings. <br/>
https://web.microsoftstream.com/video/dc439334-70cd-45b1-944b-af59c16f7d3a - A video on how to test and cleaning up Python code. <br/>
All the videos above were recorded by Dr Ian McLoughlin. Much of the code is based on the videos above. His lectures also helped me in understanding the concepts of this project. <br/>
https://en.wikipedia.org/wiki/Nondeterministic_finite_automaton - This page is about NFAs. <br/>
https://en.wikipedia.org/wiki/Shunting-yard_algorithm - This page is about the shunting yard algorithm. <br/>
https://en.wikipedia.org/wiki/Regular_expression - This page is about regular expressions and its history, syntax and implementations. <br/>
https://en.wikipedia.org/wiki/Thompson%27s_construction - The page discusses Thompson's construction. <br/>
https://www.geeksforgeeks.org/write-regular-expressions/ - This page gives a quick rundown of regular expressions. <br/>
https://brilliant.org/wiki/shunting-yard-algorithm/ - This page goes through the shunting-yard algorithm. It explains it using pseudocode and diagrams.<br/>
http://www.emerson.emory.edu/services/editors/ne/Regular_Expressions.html - A very informative page explaining the different signs used in regular expressions. <br/>
https://swtch.com/~rsc/regexp/regexp1.html - This page uses diagrams to show how the different signs are used in regular expressions and NFAs. It also explains how they are done using pseudocode. This helped me understand them a lot more. <br/>
https://en.wikipedia.org/wiki/Infix_notation - This is a short Wikipedia page about infix notation. <br/>
https://en.wikipedia.org/wiki/Reverse_Polish_notation - This is a Wikipedia page about postfix notation. It is a good place to start for research about postfix notation. It talks about its history, implementations and explains what postfix is. <br/>
https://docs.python.org/3/library/unittest.html - This is the official documentation for the "unittest" framework which is always a good start for getting to know about a certain library, language, framework, etc. It was very useful for getting to know about the framework.<br/>
https://www.youtube.com/watch?v=_0soBPejyu4 - This is a video introduction about the use of tests in Python using "unittest". <br/>
https://docs.python.org/3/library/argparse.html - Again this is the official documentation for the "argparse" library and it was very informative. <br/>
https://www.youtube.com/watch?v=cdblJqEUDNo - This a video going through an example using the "argparse" library. <br/>
