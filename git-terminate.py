import argparse

parser = argparse.ArgumentParser(
    prog='git-terminate',
    description='Checkout to master, pull, delete a branch and refresh remote refs.'
)

parser.add_argument('branch_name', metavar='branch-name', help='the branch to be deleted')
