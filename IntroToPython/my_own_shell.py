import sys

sys.stdout.write(">>> ")
sys.stdout.flush()


def my_own_shell():
    while True:
        try:
            user_input = input()
            if user_input == "exit":
                break
            else:
                print(user_input)

        except EOFError:
            break

        # I don't know why this is not working
        # add emoji to the prompt
