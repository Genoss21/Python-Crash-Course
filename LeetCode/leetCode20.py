def isValid(s):
    stack = []  # To use append and pop
    pairs = {
        '(': ')',
        '{': '}',
        '[': ']'
    }

    for bracket in s:
        if bracket in pairs:
            stack.append(bracket)
        elif len(stack) == 0 or bracket != pairs[stack.pop()]:
            return False
    return len(stack) == 0  # Moved outside the loop


# Loop with user input
while True:
    userInput = input("Enter a string of brackets (or 'q' to quit): ")

    if userInput.lower() == 'q':
        print("Ending")
        break

    result = isValid(userInput)
    print(f"The string '{userInput}' is valid: {result}")
