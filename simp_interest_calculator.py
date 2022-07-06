def simple(screen, years, initialAmt, percent):
    decimal = percent / 100 * years + 1
    a = initialAmt * decimal

    # Give User Their Answer
    return f"Total amount after {years} year(s): ${round(a, 2)}!"