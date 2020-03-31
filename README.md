# Graph Theory Project

## Problem Statement
>You must write a program in the Python programming language that can build a non-deterministic finite automaton (NFA) from a regular expression, and can use the NFA to check if the regular expression matches any given string of text.

## Deployment
Clone the repository with:
``` git clone https://github.com/WilliamVida/GraphTheoryProject ```

Enter the project folder and run the regextonfa.py file or enter the following command:
``` python regextonfa.py ```

## Research & Development
### Non-Deterministic Finite Automaton
What is a non-deterministic finite automaton (NFA)?
[Wikipedia](https://en.wikipedia.org/wiki/Nondeterministic_finite_automaton) describes a non-deterministic finite automaton as a
> finite-state machine is called a deterministic finite automaton (DFA), if  
each of its transitions is uniquely determined by its source state and input symbol,  
reading an input symbol is required for each state transition.

### Regular Expression
What is a regular expression?
[Wikipedia](https://en.wikipedia.org/wiki/Regular_expression) describes a regular expression as a
> sequence of characters that define a search pattern. Usually such patterns are used by string searching algorithms for "find" or "find and replace" operations on strings, or for input validation. It is a technique developed in theoretical computer science and formal language theory. 

An example of a regular expression for [validating an email address](https://www.geeksforgeeks.org/write-regular-expressions/
) would be: <br/>
``` ^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$ ``` <br/>
The string "example@email.com" would validate the regular expression above while the strings "example@@email.com" and "'example'@email.com" would not.

### Converting a Regular Expression to a Non-Deterministic Finite Automaton
#### Shunting-yard algorithm
The [shunting-yard algorithm](https://en.wikipedia.org/wiki/Shunting-yard_algorithm) is a 
> method for parsing mathematical expressions specified in infix notation. It can produce either a postfix notation string, also known as Reverse Polish notation (RPN), or an abstract syntax tree (AST). The algorithm was invented by Edsger Dijkstra and named the "shunting yard" algorithm because its operation resembles that of a railroad shunting yard.

The [procedure used](https://brilliant.org/wiki/shunting-yard-algorithm/) is as follows:
-   Expressions are parsed left to right.
-   Each time a number or operand is read, we push it to the stack.
-   Each time an operator comes up, we pop the required operands from the stack, perform the operations, and push the result back to the stack.
-   We are finished when there are no tokens (numbers, operators, or any other mathematical symbol) to read. The final number on the stack is the result.

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


#### Resources Used
https://web.microsoftstream.com/video/f0a890b2-c28a-40d3-8175-adfb005260ed
https://web.microsoftstream.com/video/a29536d4-e975-4172-a470-40b4fe28866e
https://web.microsoftstream.com/video/781325b2-b4b9-461e-88cc-c5bf37e977eb
https://web.microsoftstream.com/video/3be78704-8cc5-43f1-9be5-68b2e92c8d56
https://web.microsoftstream.com/video/77e5ecd7-96c5-43ba-a11e-8399d44c87c9
https://web.microsoftstream.com/video/f4bc3634-b94f-4c15-b2c1-70cccd874c54
https://web.microsoftstream.com/video/dc439334-70cd-45b1-944b-af59c16f7d3a
https://en.wikipedia.org/wiki/Nondeterministic_finite_automaton
https://en.wikipedia.org/wiki/Shunting-yard_algorithm
https://en.wikipedia.org/wiki/Regular_expression
https://en.wikipedia.org/wiki/Thompson%27s_construction
https://www.geeksforgeeks.org/write-regular-expressions/
https://brilliant.org/wiki/shunting-yard-algorithm/
http://www.emerson.emory.edu/services/editors/ne/Regular_Expressions.html
https://swtch.com/~rsc/regexp/fig16.png
