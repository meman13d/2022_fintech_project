def login():
    global username
    global password
    logged_in = False
    while logged_in is False:
        login_u = input('Enter your username: ')
        login_p = input('Enter your password: ')
        if login_u == username and login_p == password:
            print('logged in!\n\n')
            logged_in = True
            os.system('clear')
            menu()
        else:
            print('incorrect username or password. please try again.')


def menu():
    done_action = False
    while done_action is False:
        action = input(
            'Enter what you want to do (sell, buy, balance, log off): ')
        if action.lower().find('sell') // 1 == 0 or action.lower().find(
                'buy') // 1 == 0:
            os.system('clear')
            sell()
            done_action = True
        elif action.lower().find('view') // 1 == 0 or action.lower().find(
                'balance') // 1 == 0:
            os.system('clear')
            view_balance()
            done_action = True
        elif action.lower() == 'log off':
            done_action = True
            os.system('clear')
            login()
        else:
            print('Please choose one of the options')


def sell():
    risk_appetite = float(input('Please enter your risk appetite (0-100): '))
    max_investment = float(
        input('Enter the maximum amount of money that you want to risk: '))
    recommendations = {
        5.0: "government bonds or corporate debt",
        10.0: "blue chip stock funds or hedge funds",
        15.0: "more risky stock or private equity",
        20.0: "general cryptocurrency investments",
        20.1: "venture capital"
    }
    for r_value in recommendations.keys():
        if risk_appetite - r_value <= 0:
            print(f"We recommend investing in {recommendations[r_value]}")
            break
    '''
  if risk_appetite <= 5.0:
    print('We recommend investin in government bonds or corporate debt')
  elif risk_appetite <=10.0:
    print('we recommend investing in blue chip stock funds or hedge funds')
  elif risk_appetite <= 15.0:
    print('We recommend investing in more risky stock or private equity')
  elif risk_appetite <= 20:
    print('We recommend investing in general cryptocurrency investments')
  elif risk_appetite >20:
    print('We recommend investing in venture capital')
  '''

    print('Your potential profit for this year is: ',
          max_investment * risk_appetite)

    go_home()


def view_balance():
    print('Your balance is: \n $420 (+6.9%) \n' +
          tabulate(data, headers=col_names))
    go_home()


def go_home():
    go_home = False
    while go_home is False:
        home = input('\n type ok to return to home: ')
        if home.lower() == 'ok':
            go_home = True
            os.system('clear')
            menu()


from tabulate import tabulate
import os
import sys

username = 'admin'
password = 'admin'

data = [['Bitcoin', 1], ['Ethereum', 5]]

col_names = ['Investments', 'Percentage fluctuation']

login()
