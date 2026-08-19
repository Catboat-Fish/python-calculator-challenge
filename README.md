## Core Information
This is a simple calculator app programmed to demonstrate that many functions can be done using only addition and subtraction. Yes, I could have made a calculator that multiplies and divides using built-in Python functions, but this project is meant to show an understanding of both Python and mathematics, as well as the ability to produce working products under a large constraint.


## Guidelines
Just a quick note, these guidelines may change over time
- \+ and - allowed
- == and != allowed
- no * or /
- no range()
- no booleans that are declared to be booleans, i=0 and i!=0 allowed as stated previously
- returns can be used to do math or run functions, but still must only contain code that follows all guidelines


## Notes
### General (not specific to any particular function)
- a and b are used for consistency and ease of reading
- returns are used in definitions instead of prints in case this code is implemented into a non-console system in the future, as returns allow for significantly less rewriting
- you may see the following structure...
```
if i == j:
    return result_1
return result_2
```
- ...which is used because result_1 runs if i == j, and result_2 runs if i != j; this saves space here compared to elif and else, since a return ends the definition early
### Multiply
- originally made using "for i in range(b):", later changed to the current system as using range() in this program violates the spirit of the challenge
- "if a == 0 or b == 0" saves time and power in cases such as (0,99999)
### Divide
- due to my limitation on booleans and wanting to create division that wasn't a clone of multiplication, I decided to create my own boolean using addition and subtraction for determining whether the result is positive or negative, with 0 meaning non-negative (False) and !=0 meaning negative (True)
- since the remainder either is zero or isn't zero, it doesn't need an elif or else, since the code returns before running the final line if non-negative and only uses the final line if negative
- negatives were easy to deal with due to the principle that a/-b == -a/b and -a/b == (-1)(a/b)
### Invert and Absolute
- the format of the final section of division was made here first, since both operate on the basis of "it either is this way or it isn't"
- invert has shown itself to be incredibly usdeful in many other functions, saving a lot of time by skipping me writing out i = (0 - i) repeatedly
### Power
- can currently only do positive powers, but due to the way I wrote the multiplication code, it can do negative numbers to a positive power
- "while b > 1" is used since unlike in multiplication, the result gets returned as "a", meaning it starts at "a" rather than at 0
### Tetration
- still a work-in-progress
- note to self: try using recursion
