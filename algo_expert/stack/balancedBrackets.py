
#O(n)|O(1)
def balancedBrackets(strings):
    openingBrackets="([{"
    closingBrackets=")]}"
    matchingBracket = {")":"(","]":"[","}":"{"}
    stack =[]
    for char in strings:
        if char in openingBrackets:
            stack.append(char)
        elif char in closingBrackets:
            if len(stack)==0:
                return False
            if stack[-1] == matchingBracket[char]:
                stack.pop()
            else:
                return False
    return len(stack)==0


def isValid(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    # For every bracket in the expression.
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '.'
            print('top_element',top_element)
            if mapping[char] != top_element:
                return False
        else:
            print('new',char)
            stack.append(char)
    return not stack

isValid("()[]{}}")