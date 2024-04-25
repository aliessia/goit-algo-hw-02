def check_brackets(expression):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    for char in expression:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs:
            if stack and stack[-1] == pairs[char]:
                stack.pop()
            else:
                return "Несиметрично"
    if stack:
        return "Несиметрично"
    else:
        return "Симетрично"

print(check_brackets("( ){[ ]( 1 + 3 )( ){ }}")) 