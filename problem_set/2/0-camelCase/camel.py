user_string = input("camelCase: ")
user_string_list = list(user_string)

for letter in user_string_list:
    if letter.isupper():
        user_string_list.insert((user_string_list.index(letter)), '_')
        user_string_list[user_string_list.index(letter)] = letter.lower()

user_snake_case_string = "".join(user_string_list)
print(f"snake_case: {user_snake_case_string}")
