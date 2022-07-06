def comp(screen, y, initialAmt, percent):
    # Starting Variables
    decimal = percent / 100
    multiplier = 1 + decimal

    # Answers
    answer = round(initialAmt * multiplier ** y, 2)

    # Give User Their Information
    return f"Total amount after {y} year(s): ${answer}!"