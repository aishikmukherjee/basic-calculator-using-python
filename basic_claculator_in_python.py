
def add(operator1, operator2):
    """This function adds operator1 and operator2 and returns the result"""
    return operator1+operator2


def sub(operator1, operator2):
    """This function subtracts operator1 and operator2 and returns the result"""
    return operator1-operator2


def mul(operator1, operator2):
    """This function multiplies operator1 with operator2 and returns the result"""
    return operator1*operator2


def div(operator1, operator2):
    """This function divides operator1 by operator2 and returns the result"""
    return operator1/operator2

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


credit_of_project = '''
 _____                                                                   _____ 
( ___ )                                                                 ( ___ )
 |   |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|   | 
 |   |                                                                   |   | 
 | S |    _   _   _   _   _   _   _   _                                  | P | 
 |   |   / \ / \ / \ / \ / \ / \ / \ / \                                 | R | 
 | O |  ( C | R | E | A | T | O | R | : )                                | O | 
 |   |   \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/                                 | J | 
 | L |    _   _   _   _   _   _     _   _   _   _   _   _   _   _   _    | E | 
 |   |   / \ / \ / \ / \ / \ / \   / \ / \ / \ / \ / \ / \ / \ / \ / \   | C | 
 | O |  ( A | i | s | h | i | k ) ( M | u | k | h | e | r | j | e | e )  | T | 
 |   |   \_/ \_/ \_/ \_/ \_/ \_/   \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/   |   | 
 |   |                                                                   |   | 
 |___|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|___| 
(_____)                                                                 (_____)

                        CREATED ON: 03-10-2024
───────────────────────────────────────────────────────────────────────────────

'''
print(logo)

power_on = True
while power_on:
    num1 = float(input("\nWhat is the first number?: "))
    print("+\n-\n*\n/")
    operation = input("Pick an operation: ")
    num2 = float(input("What is the second number?: "))
    match operation:
        case '+':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        case '-':
            print(f"{num1} - {num2} = {sub(num1, num2)}")
        case '*':
            print(f"{num1} * {num2} = {mul(num1, num2)}")
        case '/':
            if num2 == 0:
                print("Division by 0 is not allowed")
            else:
                print(f"{num1} / {num2} = {div(num1, num2)}")
        case _ :
            print('Wrong Operation Input........!!!')
    choice = input('\nEnter \'yes\' to calculate again\nEnter anything else to exit\nEnter choice: ').lower()
    if choice != 'yes':
        power_on = False
        print("\nGoodBye...!!!")
        print(credit_of_project)
