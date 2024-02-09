import random

def random_numbers():
    """
    Returns a list of random numbers between 1 and 49 in ascending order.

    :rtype: list
    :return: list with 6 random numbers
    """
    list_of_random_numbers = []
    for num in range(6):
        draw = random.randint(1, 49)
        list_of_random_numbers.append(draw)
    return sorted(list_of_random_numbers)

def get_user_numbers():
    """
    Get number from user.
    Try untill user gives proper number.

    :rtype: int
    :return: given number as int
    """
    while True:
        try:
            user_input = int(input("Input a number in range 1-49: "))
            break
        except ValueError:
            print("This is not a number!")

    return user_input

def user_numbers():
    """
    Returns a list of given user numbers between 1 and 49 in ascending order.

    :rtype: list
    :return: list with 6 user numbers
    """
    list_of_user_numbers = []
    while len(list_of_user_numbers) < 6:
        number = get_user_numbers()
        if number not in list_of_user_numbers and 0 < number <= 49:
            list_of_user_numbers.append(number)

    return sorted(list_of_user_numbers)

def lotto():
    """
    Main function of the lotto game.
    """
    usr_numbers = user_numbers()
    print(f"Your numbers: {usr_numbers}")

    lotto_numbers = random_numbers()
    print(f"Lotto numbers: {lotto_numbers}")

    hits = 0

    for number in usr_numbers:
        if number in lotto_numbers:
            hits += 1

    print(f"You have hit {hits} {'number!' if hits == 1 else 'numbers!'}")


if __name__ == "__main__":
    lotto()
