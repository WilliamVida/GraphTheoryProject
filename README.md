
# Graph Theory Project

## Problem Statement
>You must write a program in the Python programming language that can build a non-deterministic finite automaton (NFA) from a regular expression, and can use the NFA to check if the regular expression matches any given string of text.

## Deployment
Clone the repository with:
``` git clone https://github.com/WilliamVida/GraphTheoryProject ```

Enter the project folder then enter the following command:
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
) would be:<br/>
``` ^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$ ```<br/>
The string "example@email.com" would validate the regular expression above while the strings "example@@email.com" and "'example'@email.com" would not.

### Converting a Regular Expression to a Non-Deterministic Finite Automaton
#### Thompson's construction
[Thompson's construction](https://en.wikipedia.org/wiki/Thompson%27s_construction) is a
> method of transforming a regular expression into an equivalent nondeterministic finite automaton (NFA). This NFA can be used to match strings against the regular expression. This algorithm is credited to Ken Thompson.

##### Operators
#####  "."
The [full stop](http://www.emerson.emory.edu/services/editors/ne/Regular_Expressions.html) is a special character that matches anything except a newline. Using concatenation, we can make regular expressions like `a.b` which matches any three-character string which begins with "a" and ends with "b".

#####  "|"
The [vertical bar](http://www.emerson.emory.edu/services/editors/ne/Regular_Expressions.html) specifies an alternative. Two regular expressions a and b with "|" in between (`a|b`) form an expression that matches anything that either a or b will match. Thus, `foo|bar` matches either "foo" or "bar" but no other string. "|" applies to the largest possible surrounding expressions. Only a surrounding "( ... )" grouping can limit the grouping power of "|".

##### "*"
The [asterisk](https://en.wikipedia.org/wiki/Regular_expression) indicates  _zero or more_  occurrences of the preceding element. For example,  `ab*c`  matches "ac", "abc", "abbc", "abbbc", and so on.

##### "+"
The [plus sign](https://en.wikipedia.org/wiki/Regular_expression) indicates  _one or more_  occurrences of the preceding element. For example,  `ab+c`  matches "abc", "abbc", "abbbc", and so on, but not "ac".

##### "?"
The [question mark](https://en.wikipedia.org/wiki/Regular_expression) indicates _zero or one_ occurrences of the preceding element. For example, `colou?r` matches both "color" and "colour".

#### Shunting-yard algorithm
The [shunting-yard algorithm](https://en.wikipedia.org/wiki/Shunting-yard_algorithm) is a 
> method for parsing mathematical expressions specified in infix notation. It can produce either a postfix notation string, also known as Reverse Polish notation (RPN), or an abstract syntax tree (AST). The algorithm was invented by Edsger Dijkstra and named the "shunting yard" algorithm because its operation resembles that of a railroad shunting yard.