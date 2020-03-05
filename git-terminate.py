import argparse
import subprocess

parser = argparse.ArgumentParser(
    prog='git-terminate',
    description='Checkout to master, pull, delete a branch and refresh remote refs.'
)

parser.add_argument('branch_name', metavar='branch-name', help='the branch to be deleted')
parser.add_argument('--default-branch', action='store', default='master', help='the branch the pull request has been merged to')

args = parser.parse_args()

subprocess.run('git checkout'.split() + [args.default_branch])
subprocess.run('git pull'.split())
subprocess.run('git branch -d'.split() + [args.branch_name])
subprocess.run('git fetch -p'.split())
