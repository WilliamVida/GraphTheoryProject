# Thompsons construction
# William Vida

class State:
    """ A state with one or two edges, all edges labeled by label. """
    # Constrcutor.
    def __init__(self, label=None, edges=[]):
        # Every state has 0, 1, or 2 edges from it.
        self.edges = edges
        # Label for the arrows. None means epsilon.
        self.label = label

class Fragment:
    """ An NFA fragment with a start state and an accept state. """
    # Constructor.
    def __init__(self, start, accept):
        # Start state of NFA fragment.
        self.start = start
        # Accept state of NFA fragment.
        self.accept = accept


def shunt(infix):
    """ Return the infix regular expression in postfix. """
    
    # Convert input to a stack-ish list.
    infix = list(infix)[::-1]

    # Operators stack.
    opers = []

    # Output list.
    postfix = []

    # Operator precedence.
    prec = {'*': 100, '.': 80, '|': 60, ')': 40, '(': 20}

    # Loop through the input one character at a time.
    while infix:
        # Pop a character from the input.
        c = infix.pop()

        # Decide what to do based on the character.
        if c == '(':
            # Push an open bracket to the opers stack.
            opers.append(c)
        elif c == ')':
            # Pop the operators stack until you find a (.
            while opers[-1] != '(':
                postfix.append(opers.pop())
            # Get rid of the '('.
            opers.pop()
        elif c in prec:
            # Push any operators on the opers stack with higher prec to the output.
            while opers and prec[c] < prec[opers[-1]]:
                postfix.append(opers.pop())
            # Push c to the operator stack.
            opers.append(c)
        else:
            # Typically, we just push the character to the output.
            postfix.append(c)

    # Pop all operators to the output.
    while opers:
        postfix.append(opers.pop())

    # Convert output list to string.
    return ''.join(postfix)


def compile(infix):
    """ Return an NFA Fragment representing the infix regular expression. """
    # Convert infix to postfix.
    postfix = shunt(infix)
    # Make postfix a stack of characters.
    postfix = list(postfix)[::-1]

    # A stack for the NFA fragments.
    nfa_stack = []

    while postfix:
        # Pop a character from postfix.
        c = postfix.pop()
        if c == '.':
            # Pop two fragments off the stack
            frag1 = nfa_stack.pop()
            frag2 = nfa_stack.pop()
            # Point frag2's accept state at frag1's start state.
            frag2.accept.edges.append(frag1.start)
            # The new start state is frag2's.
            start=frag2.start
            # The new accept state is frag1's.
            accept=frag1.accept
        elif c == '|':
            # Pop two fragments off the stack.
            frag1 = nfa_stack.pop()
            frag2 = nfa_stack.pop()
            # Create new start and accept states.
            accept = State()
            start = State(edges=[frag2.start, frag1.start])
            # Point the old accept states at the new one.
            frag2.accept.edges.append(accept)
            frag1.accept.edges.append(accept)
        elif c == '*':
            # Pop a single fragment off the stack.
            frag = nfa_stack.pop()
            # Create new start and accept states.
            accept = State()
            start = State(edges=[frag.start, accept])
            # Point the arrows.
            frag.accept.edges = [frag.start, accept]
        else:
            accept = State()
            start = State(label=c, edges=[accept])

        # Create new instance of Fragment to represent the new NFA.
        newfrag=Fragment(start,accept)
        # Push the new NFA to the NFA stack.
        nfa_stack.append(newfrag)

    # The NFA stack should have exactly one NFA in it.
    return nfa_stack.pop()

# Add a state to a set, and follow all of th e(epsilon) arrows.
def follows(state, current):
    # Only do something when we haven't already seen the state.
    if state not in current:
        # Put the state itself into current.
        current.add(state)
        # See whether state is labelled by e(psilon).
        if state.label is None:
            # Loop through the states pointed to by this state.
            for x in state.edges:
                # Follow all of their e(psilon)s too.
                follows(x,current)


def match(regex, s):
    # This function will return Ttrue if and only if the regular expression
    # regex (fully) matches the string s. It returns false otherwise.

    # Compile the regular expression into an NFA.
    nfa = compile(regex)

    # Try to match the regular expression to the string s.

    # The current set of states.
    current={nfa.start}
    # Add the first stat, follow all e(psilon) arrows.
    follows(nfa.start,current)
    # The previous set of states.
    previous=set()
    
    # Loop through characters in s.
    for c in s:
        # Keep track of where we were.
        previous=current
        # Create a new empty set for states we're about to be in.
        current=set()
        # Loop through the previous states.
        for s in previous:
            # Only follow arrows not labeled by e(psilon).
            if s.label is not None:
                # If the label of the state is equal to the characters we've read:
                if s.label==c:
                    # Add the state at the end of the arrow to current.
                    follows(state.edges[0],current)

    # Ask the NFA if it matches the string s.
    return nfa.accept in current

if __name__=="__main__":
    tests= [
        ["a.b|b*", "bbbbbb", True],
        ["a.b|b*", "bbx", False],
        ["a.b", "ab", True],
        ["b**", "b", True],
        ["b*", "", True]
    ]

    for test in tests:
        assert match(test[0],test[1])==test[2], test[0] + \
        (" should match " if test[2] else " should not match ")+test[1]

# print(match("a.b|b*", "bbbbbbbbbbbx"))
