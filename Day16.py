#switch case statement

a=int(input("Enter number between 1-5:"))

match a:
    case 1:
        print('You entered number "1".')
    case 2:
        print('You entered number "2".')
    case 3:
        print('You entered number "3".')
    case 4:
        print('You entered number "4".')
    case 5:
        print('You entered number "5".')
    case _:
        print('Please enter number between 1-5.')
#'case _' is the default case if none of the above cases match.
        
        
