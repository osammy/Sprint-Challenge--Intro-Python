def inputParser(enteredInput):
    splittedInput = enteredInput.strip(" ").split(",")
    return [float(splittedInput[0]), float(splittedInput[1])]
