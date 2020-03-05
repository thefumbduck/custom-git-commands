import argparse

parser = argparse.ArgumentParser(
        prog='git-publish',
        description="Publish a branch remotely. Equivalent of 'git push --set-upstream origin {branch-name}'."
)

parser.add_argument('branch-name', action='store', help='the branch to be published')
