# Graph Theory Project

## Problem Statement
To must write a program in the Python programming language that can
build a non-deterministic finite automaton (NFA) from a regular expression,
and can use the NFA to check if the regular expression matches any given
string of text.

## Deployment
Clone the repository with:
``` git clone https://github.com/WilliamVida/GraphTheoryProject ```

Enter the project folder then enter the following command:
``` python regextonfa.py ```

## Research & Development
#### Non-Deterministic Finite Automaton
What is a non-deterministic finite automaton (NFA)?
[Wikipedia](https://en.wikipedia.org/wiki/Nondeterministic_finite_automaton) desribes a non-deterministic finite automaton as a
> In automata theory, a finite-state machine is called a deterministic finite automaton (DFA), if 
each of its transitions is uniquely determined by its source state and input symbol,
reading an input symbol is required for each state transition.

### Regular Expression
What is a regular expression?
[Wikipedia](https://en.wikipedia.org/wiki/Regular_expression) describes a regular expression as a 
> sequence of characters that define a search pattern. Usually such patterns are used by string searching algorithms for "find" or "find and replace" operations on strings, or for input validation. It is a technique developed in theoretical computer science and formal language theory. 

An example of regular expression for [validating an email address](https://www.geeksforgeeks.org/write-regular-expressions/
) would be:
``` ^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$ ```
The string example@email.com would validate the regular expression above while example@@email.com and "example"@email.com would not.

### Converting a Regular Expression to a Non-Deterministic Finite Automaton
#### Thompson's construction
[Thompson's construction](https://en.wikipedia.org/wiki/Thompson%27s_construction) is a
> method of transforming a regular expression into an equivalent nondeterministic finite automaton (NFA). This NFA can be used to match strings against the regular expression. This algorithm is credited to Ken Thompson.
