def is_valid(parenthesises):
    stack=[]
    mapping = {")":"(","}":"{","]":"["}

    for char in parenthesises:
        if char in mapping:
            toplement= stack.pop() if stack else "#"
            if toplement !=mapping[char]:
                return False
        else:
            stack.append(char)


    return not stack