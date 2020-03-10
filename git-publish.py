import argparse
import subprocess

def get_current_branch_name():
    return subprocess.check_output('git branch --show-current'.split()).decode(encoding='utf-8').strip()

parser = argparse.ArgumentParser(
        prog='git-publish',
        description="Publish a branch remotely. Equivalent of 'git push --set-upstream origin {branch-name}'."
)

parser.add_argument('branch_name', metavar='branch-name', action='store', help='the branch to be published')
parser.add_argument('--remote', action='store', default='origin', help='the remote the branch will be published to')

args = parser.parse_args()

subprocess.run('git push --set-upstream'.split() + [args.remote, args.branch_name])
