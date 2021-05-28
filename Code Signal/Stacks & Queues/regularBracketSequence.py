def regularBracketSequence2(sequence) -> bool:
    brackets = {'[': 0, ']': 0, '(': 0, ')': 0}  # constant space O(1)
    for bracket in sequence:    # linear time O(N)
        brackets[bracket] += 1

    # if no of left brackets does not equal the right ones
    if brackets['['] != brackets[']'] or brackets['('] != brackets[')']:
        return False

    stack = []    # push left brackets into stack, if incounter the right similar one then pop
    for bracket in sequence:  # time O(N)
        if bracket in ['[', '(']:
            stack.append(bracket)

        else:
            if len(stack) == 0:  # if first element is right side and left side is not in correct order
                return False

            else:
                brack = stack.pop()
                if brack == '[' and bracket != ']':
                    return False

                elif brack == '(' and bracket != ')':
                    return False

    return True


regularBracketSequence2("[()()]")
