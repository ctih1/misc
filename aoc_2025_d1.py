"""
This worked at some point but I couldnt be bothered to solve thwe extra challenge
"""

from typing import Tuple, Literal, List

lines: List[str] = []

with open("1/input.txt") as f:
    lines = f.readlines()

def parse_line(line: str) -> Tuple[Literal["left", "right"], int]:
    direction: Literal["left", "right"] = "left" if line.startswith("L") else "right"
    amount = int(line[1:])

    return direction, amount

zeroes: int = 0

def get_next_dial(current_dial: int, line: str) -> int:
    global zeroes
    starts_at_0 = current_dial == 0
    direction, amount = parse_line(line)

    if direction == "left":
        current_dial -= amount
    elif direction == "right":
        current_dial += amount
    
    while current_dial > 99:
        current_dial = 0 + (current_dial-100)
        if not starts_at_0 and current_dial != 0:
            print("Y")
            zeroes += 1
        starts_at_0 = False
    
    while current_dial < 0:
        current_dial = 100 - abs(current_dial)
        if not starts_at_0 and current_dial != 0:
            zeroes += 1
            print("Z")
        starts_at_0 = False

    if current_dial == 0:
        print("X")
        zeroes += 1

    return current_dial

# assert get_next_dial(11, "R8") == 19
# assert get_next_dial(19, "L19") == 0
# assert get_next_dial(5, "L10") == 95
# assert get_next_dial(95, "R5") == 0
# assert get_next_dial(0, "L1") == 99
# assert get_next_dial(99, "R1") == 0

dial: int = 50
print(f"The dial starts by pointing at {dial}")
for line in lines:
    print()
    dial = get_next_dial(dial, line)

    print(f"The dial is rotated {line.strip()} to point at {dial}")

print(f"Answer: {zeroes}")
