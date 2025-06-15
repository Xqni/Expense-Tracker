
# Expense Tracker

A simple command line program in Python programming language to track your expenses. Beginner level project.

## Hello 👋
Thank you for checking my project, if you find any mistakes please let me know and I will try to imporve it.

## Commands
```python
add - requires a description and an amount
usage: add --description "Dinner" --amount 20 | add -d "Dinner" -a 20

update - requires an id, optionally either a description or amount
usage: update --id 1 --description "Lunch" --amount 20 | update -i 1 -d "Lunch" -a 20

list - requries no arguments
usage: list

summary - takes optional argument of month
usage: summary | summary -m 5 | summary --month 5

delete - requires an id
usage: delete --id 1 | delete -i 1
```

## Usage/Examples 🤔

```python
python main.py --help
# displays help about program

python main.py add --help
# displays help for 'add' command, replace 'add' with other valid commands to view help

python main.py add -d Dinner -a 20
# Expense added successfully (ID 1)

python main.py update -i 1 -d Lunch
# Updates expense with id 1

python main.py list
# Lists all expenses in a nice table format (atleast I think its nice!)

python main.py summary
# Summarizes all expenses

python main.py summary -m 5
# Summarizes all expenses for month 5

python main.py delete -i 1
# Deletes expense with id 1
```
## Websites Used 🛜

 - [Expense Tracker Project](https://roadmap.sh/projects/expense-tracker)
 - [Argparse Python](https://docs.python.org/3/library/argparse.html)
 - [Roadmap.sh](https://roadmap.sh/roadmaps)
 - [ChatGPT](https://www.chatgpt.com/)
 - [Readme](https://readme.so/)

