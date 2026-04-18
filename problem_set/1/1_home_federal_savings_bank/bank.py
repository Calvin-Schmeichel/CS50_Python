user_string = input("Greeting: ")

if (str.find(user_string.lower(), "hello")) == 0:
    print("$0")
elif(str.find(user_string.lower(), "h")) == 0:
    print("$20")
else:
    print("$100")