from password_manager import (
    alphanumeric_pass,
    get_password,
    xkcd_password,
    delete_pass,
)
from user_auth import get_user

if __name__ == "__main__":
    is_ok, auth_user = get_user()
    auth_user = auth_user.upper()
    if is_ok is True:
        MENU_PROMPT = """
        Please choose what you would like to do.

        1 - Generate a alphanumeric password
        2 - Generate a XKCD style password
        3 - View a password
        4 - Delete a password
        E - Exit program

        Your Selection: """

        while True:
            user_input = input(MENU_PROMPT)
            if user_input == "1":
                alphanumeric_pass(auth_user)
            elif user_input == "2":
                xkcd_password(auth_user)
            elif user_input == "3":
                get_password(auth_user)
            elif user_input.upper() == "E":
                break
            elif user_input == "4":
                delete_pass(auth_user)
            else:
                print("\n---Not a valid option---")


else:
    print("Running script from another file")
