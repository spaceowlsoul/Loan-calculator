import argparse
import math
months_in_year = 12

parser = argparse.ArgumentParser(description="This is a loan calculator!")
parser.add_argument("-t", "--type", type=str, help="Choose the type of calculation: diff (differentiated) or annuity")
parser.add_argument("-pr", "--principal", type=int, help="Input your loan principal")
parser.add_argument("-pe", "--periods", type=int, help="Input the number of months")
parser.add_argument("-in", "--interest", type=float, help="Input the value of interest rate")
parser.add_argument("-p", "--payment", type=int, help="Input your monthly payment")
args = parser.parse_args()


if args.type == "annuity":
    if args.principal and args.payment and args.interest:
        nominal_interest_rate = args.interest / (months_in_year * 100)
        number_of_periods = math.ceil((math.log((args.payment / (args.payment - nominal_interest_rate * args.principal)),
                                                (nominal_interest_rate + 1))))
        months = round(number_of_periods % months_in_year)
        years = number_of_periods // months_in_year
        overpayment = (number_of_periods * args.payment) - args.principal
        if years > 1:
            if months > 1:
                print(f'It will take {years} years {months} months to repay this loan!')
                print(f'Overpayment = {overpayment}!')
            elif months == one:
                print(f'It will take {years} years {months} month to repay this loan!')
                print(f'Overpayment = {overpayment}!')
            else:
                print(f'It will take {years} years to repay this loan!')
                print(f'Overpayment = {overpayment}!')
        elif years < 1:
            if months > 1:
                print(f'It will take {months} months to repay this loan!')
                print(f'Overpayment = {overpayment}!')
            else:
                print(f'It will take {months} month to repay this loan!')
                print(f'Overpayment = {overpayment}!')
    elif args.principal and args.periods and args.interest:
        nominal_interest_rate = args.interest / (months_in_year * 100)
        monthly_payment = math.ceil(args.principal * (nominal_interest_rate
                                                      * pow((1 + nominal_interest_rate), args.periods))
                                    / (pow((1 + nominal_interest_rate), args.periods) - 1))
        overpayment = (args.periods * monthly_payment) - args.principal
        print(f'Your monthly payment = {monthly_payment}!')
        print(f'Overpayment = {overpayment}!')
    elif args.payment and args.periods and args.interest:
        nominal_interest_rate = args.interest / (months_in_year * 100)
        loan_principal = math.floor(args.payment / ((nominal_interest_rate * pow((1 + nominal_interest_rate), args.periods))
                                                    / (pow((1 + nominal_interest_rate), args.periods) - 1)))
        overpayment = (args.periods * args.payment) - loan_principal
        print(f'Your loan principal = {loan_principal}!')
        print(f'Overpayment = {overpayment}!')
    else:
        print('Incorrect parameters')
elif args.type == "diff":
    if args.principal and args.periods and args.interest:
        nominal_interest_rate = args.interest / (months_in_year * 100)
        total_payment = 0
        for current_month in range(1, (args.periods + 1)):
            differentiated_payment = math.ceil((args.principal / args.periods) + nominal_interest_rate * (args.principal -
                                                                                                          ((args.principal
                                                                                                           * (current_month - 1))
                                                                                                           / args.periods)))

            total_payment += differentiated_payment
            print(f'Month {current_month}: payment is {differentiated_payment}')
        overpayment = total_payment - args.principal
        print(f'Overpayment = {overpayment}')
    else:
        print('Incorrect parameters')
