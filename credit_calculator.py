import sys
import argparse
import math

# python credit_calc.py --type=diff --principal=1000000 --periods=10 --interest=10
parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
parser.add_argument("--type")
parser.add_argument("--payment", type=int)
parser.add_argument("--principal", type=int)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)

args = parser.parse_args()
# print(args)
tokens = [args.type, args.payment, args.principal, args.periods, args.interest]
# print(tokens)
if args.type != "diff" and args.type != "annuity":
    print("Incorrect parameters")
    sys.exit()
if args.type == "diff" and args.payment:
    print("Incorrect parameters")
    sys.exit()
if args.interest is None:
    print("Incorrect parameters")
    sys.exit()
if len(tokens) < 4:
    print("Incorrect parameters")
    sys.exit()

if args.interest:
    i = args.interest / 12 / 100
if args.type == "annuity":
    if args.periods is None:
        months = math.ceil(math.log(args.payment / (args.payment - i * args.principal), (1 + i)))
        if months == 1:
            print("You need 1 month to repay this credit!")
        else:
            years = math.floor(months / 12)
            left_months = months - years * 12
            if years == 0:
                print(f"You need {left_months} months to repay this credit!")
            elif years == 1:
                if months == 0:
                    print(f"You need 1 year to repay this credit!")
                elif months == 1:
                    print(f"You need 1 year and 1 month to repay this credit!")
                else:
                    print(f"You need 1 year and {left_months} months to repay this credit!")
            else:
                if months == 0:
                    print(f"You need {years} years to repay this credit!")
                elif months == 1:
                    print(f"You need {years} years and 1 month to repay this credit!")
                else:
                    print(f"You need {years} years and {left_months} months to repay this credit!")
        overpayment = months * args.payment - args.principal
        print(f"Overpayment = {overpayment}")
    elif args.payment is None:
        a = math.ceil(args.principal * (i * math.pow(i + 1, args.periods)) / (math.pow(i + 1, args.periods) - 1))
        print(f"Your annuity payment = {a}!")
        overpayment = args.periods * a - args.principal
        print(f"Overpayment = {overpayment}")
    elif args.principal is None:
        credit_principal = args.payment / (
                (i * math.pow(i + 1, args.periods)) / (math.pow(i + 1, args.periods) - 1))
        print(f"Your credit principal = {round(credit_principal)}!")
        overpayment = args.periods * args.payment - round(credit_principal)
        print(f"Overpayment = {overpayment}")
elif args.type == "diff":
    total = 0
    for m in range(1, args.periods + 1):
        d = math.ceil(args.principal / args.periods + i * (args.principal - args.principal * (m - 1) / args.periods))
        total += d
        print(f"Month {m}: paid out {d}")
    overpayment = total - args.principal
    print(f"Overpayment = {overpayment}")
