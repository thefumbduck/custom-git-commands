import argparse

parser = argparse.ArgumentParser(
        prog='git-publish',
        description="Publish a branch remotely. Equivalent of 'git push --set-upstream origin {branch-name}'."
)

parser.add_argument('branch_name', metavar='branch-name', action='store', help='the branch to be published')
parser.add_argument('--remote', action='store', default='origin', help='the remote the branch will be published to')
