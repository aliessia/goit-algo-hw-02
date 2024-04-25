from collections import deque

def check_palindrome(input_string):
    formatted_string = ''.join(input_string.split()).lower()
    character_deque = deque(formatted_string)
    while len(character_deque) > 1:
        first = character_deque.popleft()
        last = character_deque.pop()
        if first != last:
            return False
    return True
result = check_palindrome("deed")
print(result)    