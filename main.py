# python3
#LABD
#datustrukturas
from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text: str):
    opening_brackets_stack = []
    text = text.split("\\n")[1]

    for position, symbol in enumerate(text):
        
        if symbol in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(symbol, position + 1))
        elif symbol in ")]}":
            # Process closing bracket, write your code here
            if opening_brackets_stack == [] or not are_matching(opening_brackets_stack[-1].char, symbol):
                return position + 1
            opening_brackets_stack.pop()
            
    if opening_brackets_stack:
        return opening_brackets_stack[-1].position
    else:
        return 0


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    if not mismatch:
        print("Success")
    else:
        print(mismatch)

if __name__ == "__main__":
    main()
