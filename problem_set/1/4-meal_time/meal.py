def main():
    user_string = input("What time is it? ")
    time = convert(user_string)

    o_seven_hundred = 7 * 60
    o_eight_hundred = 8 * 60

    twelve_hundred = 12 * 60
    thirteen_hundred = 13 * 60

    eighteen_hundred = 18 * 60
    nineteen_hundred = 19 * 60

    if o_seven_hundred <= time <= o_eight_hundred:
        print("breakfast time")
    elif twelve_hundred <= time <= thirteen_hundred:
        print("lunch time")
    elif eighteen_hundred <= time <= nineteen_hundred:
        print("dinner time")
    else:
        ...

def convert(time):
    hours, minutes = time.split(":")
    minutes = int(minutes) + (int(hours) * 60)

    return minutes

if __name__ == "__main__":
    main()