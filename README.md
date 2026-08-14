## Core Information

This is a simple calculator app programmed to demonstrate that many functions can be done using only addition and subtraction. Yes, I could have made a calculator that multiplies and divides using built-in Python functions, but this project is meant to show an understanding of both Python and mathematics, as well as the ability to produce working products under a large constraint.


## Notes
### Multiply
- originally made using "for i in range(b):", later changed to the current system as using range() in this program violates the spirit of the challenge
- "if a == 0 or b == 0" saves time and power in cases such as (0,99999)
### Divide
- still a work-in-progress
### Absolute and Invert
- both are very similar, but the difference shows that the limitations
- since absolute only has two possibilities, it doesn't need an elif or else, since the code returns before running the final line if non-negative and only uses the final line if negative