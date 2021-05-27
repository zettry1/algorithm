
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
