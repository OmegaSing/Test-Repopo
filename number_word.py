#!/usr/bin/env python3
"""Number to Word Script
For each number entered, returns a word beginning with the same letter as the number.
"""

NUMBER_WORDS = {
    0: "Zebra",
    1: "Onion",
    2: "Turtle",
    3: "Thimble",
    4: "Falcon",
    5: "Flamingo",
    6: "Silver",
    7: "Sapphire",
    8: "Eclipse",
    9: "Nautilus"
}

def number_to_word(n):
    if n in NUMBER_WORDS:
        return NUMBER_WORDS[n]
    digits = [int(d) for d in str(abs(n))]
    return ' '.join(NUMBER_WORDS[d] for d in digits)

def main():
    print("Number to Word Generator")
    print("Enter numbers (one per line, 'q' to quit):")
    while True:
        try:
            user_input = input("> ").strip()
            if user_input.lower() == 'q':
                print("Goodbye!")
                break
            num = int(user_input)
            result = number_to_word(num)
            print(f"{num} -> {result}")
        except ValueError:
            print("Please enter a valid integer.")
        except EOFError:
            break

if __name__ == "__main__":
    main()
