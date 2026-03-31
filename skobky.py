def is_valid_bracket_sequence(s):
    stack = []
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
        else:
            # Неожиданный символ — считаем неправильным
            return False

    return len(stack) == 0

# Примеры использования:
print(is_valid_bracket_sequence("()"))
print(is_valid_bracket_sequence("()[]{}"))
print(is_valid_bracket_sequence("(]"))
print(is_valid_bracket_sequence("([)]"))
print(is_valid_bracket_sequence("{[]}"))
