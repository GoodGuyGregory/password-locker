#! /Users/python3
# passwordLocker.py - an insecure password locker program.

import sys
import pyperclip
PASSWORDS = {
                'lang-smith': '06D7$8a$bp<p*',
            }

if len(sys.argv) < 2:
    print('Usage: python passwordLocker.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]  # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named: ' + account)
