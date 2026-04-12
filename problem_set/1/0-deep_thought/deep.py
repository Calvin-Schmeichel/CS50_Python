user_string = input("What is the Answer to the Great Question of Life, The Universe, and Everything? ")

if user_string.lower() in ("42", "forty-two", "forty two"):
    print("Yes")
else:
    print("No")