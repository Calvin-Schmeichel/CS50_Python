def is_valid(vanity_plate):
    if not 2 <= len(vanity_plate) <=6:
        return False
    if vanity_plate[0].isalpha() != True or vanity_plate[1].isalpha() != True:
         return False
    
    numbers = []
    for char in vanity_plate:
       if char in ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", 
                   "+", "?", "_", "=", ",", "<", ">", "/", ".", " "]:
           return False
       if len(numbers) != 0 and char.isalpha():
           return False
       if char.isnumeric() and (len(numbers) == 0 and char == '0'):
           return False
       elif char.isnumeric():
           numbers.append(char)
    return True

def main():
    if (is_valid(input("Enter Plate: ").upper())) == False:
        print("Invalid")
    else:
        print("Valid")

if __name__ == "__main__":
    main()