# CGS Calculator designed to implement functions based on program example writted by Dr. Bruce Scharlau
# University of Aberdeen

def welcome():
    """ a welcome message for users """
    print('Welcome to the CGS Calculator')
    print('Please enter all your grades, one per line')
    print('Enter a blank line to designate the end')

def calculate():
    """ Map from letter to common grade scale value"""
    points = {'A1':22.0, 'A2':21.0, 'A3':20.0, 'A4':19.0, 'A5':18.0,
    'B1':17.0, 'B2':16.0, 'B3':15.0, 'C1':14.0, 'C2':13.0, 'C3':12.0,
    'D1':11.0 ,'D2':10.0, 'D3':9.0, 'E1':8.0, 'E2':7.0, 'E3':6.0,
    'F1':5.0, 'F2':4.0, 'F3':3.0, 'G1':2.0, 'G2':1.0, 'G3':0.0}
    num_courses = 0
    total_points = 0
    done = False
    while not done:
        grade = input()
        if grade == '':
            done = True
        elif grade not in points:
            print("Unknown grade '{0}' being ignored".format(grade))
        else:
            num_courses += 1
            total_points += points[grade]
    if num_courses > 0: # avoids division by zero
        print('Your CGS score is {0:.3}'.format(total_points / num_courses))
        menu()

def menu():
    """ Either end or enter more grades for conversion """
    print('Enter 1 to exit or 2 to convert more grades')
    choice = input()
    if choice == 1:
        exit()
    else:
        calculate()

""" Run the program """
welcome()
calculate()

