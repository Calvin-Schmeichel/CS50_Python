def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d_formatted = d.replace("$", "")
    d_float = float(d_formatted)
    return d_float


def percent_to_float(p):
    p_formatted = p.replace("%", "")
    p_float = float(p_formatted) / 100
    return p_float


main()