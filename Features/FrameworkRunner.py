import sys
from behave import __main__ as runner_with_options

if __name__ == '__main__':
    sys.stdout.flush()

    runner_with_options.main()

