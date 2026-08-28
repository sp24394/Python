script = ""

# TODO make . function with chr(x) [gets the ascii char from number]

style = {
    "reset": "\033[0m",
    "cell": "\033[1;47m"
}

valid_chars = "+-<>[],."

loop_stack = []
index = 0

def validate_script(script):
    v_stack = []
    for index, char in enumerate(script):
        if char in valid_chars:
            if char == "[":
                v_stack.append(index)

            elif char == "]":
                if v_stack:
                    v_stack.pop()
                else:
                    return False, f"Unmatched ']' at index {index}"

    if v_stack:
        return False, f"'[' at index {v_stack[-1]} was not closed"
    
    return True, None

valid, error = validate_script(script)

if not valid:
    print(f"Invalid script; {error}")
else:
    pass

print(style["cell"] + "hi")