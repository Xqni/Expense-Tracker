import os
import argparse
import json
from datetime import datetime
import calendar


expense = {
    "id": None,
    "date": None,
    "description": None,
    "amount": 0
}


def add(args):
    if args.amount > 0:
        expenses = check_file()
        try:
            expense['id'] = expenses[-1]['id'] + 1

        except IndexError:
            expense['id'] = 1

        expense['description'] = args.description
        expense['amount'] = args.amount
        expense['date'] = datetime.today().strftime("%d-%m-%Y")
        expenses.append(expense)

        write_file(expenses)
        print(f"Expense added successfully (ID {expense['id']})")
    else:
        print(f"amount cannot be equal or less than zero.")


def update(args):
    expenses = check_file()
    for expense in expenses:
        if expense['id'] == args.id:
            if args.description is not None:
                expense['description'] = args.description
            elif args.amount is not None:
                expense['amount'] = args.amount
            else:
                continue
            expense['date'] = datetime.today().strftime("%d-%m-%Y")
            write_file(expenses)
            return
    print(f"Invalid expense id {args.id}")


# accepts no args but got error without it
# by design of argparse
def list(args):
    expenses = check_file()

    # '-' (left align)
    # '12' (how much space to be given to this part of the output)
    # 's' (we are printing an integer)
    print('\n%-5s%-12s%-20s%-12s' % ('ID', 'Date', 'Description', 'Amount'))
    for expense in expenses:
        print('-' * 45)
        print('%-5s%-12s%-20s%-12s' %
              (expense['id'], expense['date'], expense['description'], expense['amount']))
    print('-' * 45, '\n')


def summary(args):
    sum = 0
    expenses = check_file()
    month_name = calendar.month_name[args.month]
    if args.month == 0:
        for expense in expenses:
            sum += expense['amount']
        print(f"Total expenses: ${sum}")
        return
    for expense in expenses:
        date = datetime.strptime(expense['date'], "%d-%m-%Y")
        if args.month == date.month:
            sum += expense['amount']
    print(f"Total expenses for {month_name}: ${sum}")


def delete(args):
    expenses = check_file()
    for expense in expenses:
        if expense['id'] == args.id:
            expenses.pop(expenses.index(expense))
            print(f"Expense removed")
            write_file(expenses)
            return
    print(f"Invalid expense id {args.id}")


# return a python list
def check_file():
    if os.path.exists("expenses.json"):
        try:
            with open("expenses.json", "r") as f:
                expenses = json.load(f)
        except json.decoder.JSONDecodeError:
            expenses = []
    else:
        expenses = []
    return expenses


# write changes to file
def write_file(expenses):
    with open("expenses.json", "w") as f:
        json.dump(expenses, f, indent=4)


if __name__ == "__main__":
    # create top-level parser
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(
        title='Valid Commands', description='Use these to perform actions')

    # create parser for 'add' command
    parser_add = subparsers.add_parser('add', help='add an expense')
    parser_add.add_argument('-d', '--description',
                            help='expense description', required=True)
    parser_add.add_argument('-a', '--amount', type=float,
                            help='expense amount', required=True)
    parser_add.set_defaults(func=add)

    # create parser for 'update' command
    parser_update = subparsers.add_parser('update', help='update an expense')
    parser_update.add_argument(
        '-i', '--id', type=int, help='expense id', required=True)
    parser_update.add_argument(
        '-d', '--description', help='expense description', default=None)
    parser_update.add_argument(
        '-a', '--amount', type=int, help='expense amount', default=None)
    parser_update.set_defaults(func=update)

    # create parser for 'list' command
    parser_list = subparsers.add_parser('list', help='list all expenses')
    parser_list.set_defaults(func=list)

    # create parser for 'summary' command
    parser_summary = subparsers.add_parser(
        'summary', help='sumaarize expense (all by default)')
    parser_summary.add_argument('-m', '--month', type=int,
                                help='month specific summary', default=0)
    parser_summary.set_defaults(func=summary)

    # create parser for 'delete' command
    parser_delete = subparsers.add_parser('delete', help='delete an expense')
    parser_delete.add_argument('-i', '--id', type=int,
                               help='expense id', required=True)
    parser_delete.set_defaults(func=delete)

    # parse the args and call whatever function was selected
    args = parser.parse_args()
    args.func(args)
