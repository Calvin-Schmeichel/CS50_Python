def convert(user_string):
    user_string_modified = user_string.replace(':)', '🙂').replace(':(', '🙁')

    return user_string_modified

def main():
    user_string = input()
    print(convert(user_string))

if __name__ == "__main__":
    main()