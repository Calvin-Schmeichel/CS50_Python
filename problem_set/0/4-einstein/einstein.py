def calculate_joules(mass):
    c = 300000000
    E = mass * (pow(c, 2))
    return E

def main():
    mass = int(input())
    print(calculate_joules(mass))

if __name__ == "__main__":
    main()