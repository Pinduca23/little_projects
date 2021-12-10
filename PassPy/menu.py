from password_manager import alphanumeric_pass, get_password, xkcd_password
from user_auth import get_user


if __name__ == '__main__':
    accept, auth_user = get_user()
    if accept == False:
        print(f'Invalid login.')
    while accept == True:
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
                alphanumeric_pass(auth_user)
            elif user_input == '2':
                xkcd_password(auth_user)
            elif user_input == '3':
                get_password(auth_user)
            elif user_input.upper() == 'E':
                accept = False
                break
            else:
                print('\n---Not a valid option---')


else:
    print('Running script from another file')
