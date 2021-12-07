from password_manager import alphanumeric_pass, get_password, xkcd_password

if __name__ == '__main__':
    MENU_PROMPT = """
    Please choose what you would like to do.

    1 - Generate a alphanumeric password
    2 - Generate a XKCD style password
    3 - View a password
    E - Exit program

    Your Selection: """

    while True:
        user_input = input(MENU_PROMPT)
        if user_input == '1':
            alphanumeric_pass()
        elif user_input == '2':
            xkcd_password()
        elif user_input == '3':
            get_password()
        elif user_input.upper() == 'E':
            break
        else:
            print('\n---Not a valid option---')


else:
    print('Running script from another file')
