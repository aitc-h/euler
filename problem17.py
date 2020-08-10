"""
    Problem 17
    Number letter counts
"""

from utility.decorators import timeit, printit

words = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred",
    1000: "thousand"
}


def get_string(n):
    # String for all to be appended to
    s = ""

    if n >= 1000:
        s += words[int(n / 1000)] + " "     # Add the number of thousands
        s += words[1000]                    # Add the word for thousand
        n %= 1000                           # Remove the thousands and above
    if n >= 100:
        s += words[int(n / 100)] + " "      # Add the number of hundreds
        s += words[100]                     # Add the word for hundred
        n %= 100                            # Remove the hundreds
    if s != "" and n != 0:                  # If there is text in the string and more to be added, add a conjunction
        s += " and "
    if n >= 20:
        # For numbers greater than 20, add their multiple of 10
        s += words[(int(n/10) % 10)*10] + " "
        n %= 10                             # Remove the tens
    if n != 0:
        s += words[n]                       # If the final digit is not 0
    return s


def count(s):
    return len(s.strip().replace(" ", ""))


@ printit
@ timeit
def run():
    total = 0
    for i in range(1, 1001):
        total += count(get_string(i))
    #print(x := get_string(13), count(x))
    return total


if __name__ == "__main__":
    run()
