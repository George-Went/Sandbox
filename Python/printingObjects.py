## Formatting Operations in python
## ref: https://www.datacamp.com/community/tutorials/f-string-formatting-in-python#intro

## Soloution 1 ecapsulates the operation in brackets, meaning it is calcualted
def Soloution1(a, b):
    return "1: The answer is: " + str(a * b)


def Soloution2(a, b):
    answer = str(a * b)
    return "2: The answer is: " + answer


## f-strings are evaluated at runtime - meaning that the program does not
def Soloution3(a, b):
    return f"3: The answer is: {a * b}"


print(Soloution1(5, 5))
print(Soloution2(5, 5))
print(Soloution3(5, 5))
