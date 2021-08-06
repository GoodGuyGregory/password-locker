#! /Users/user/.pyenv/versions/3.7.5/bin/python3
# passwordLocker.py - an insecure password locker program.

import sys
import pyperclip
PASSWORDS = {'email': 'F7min1BDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmaLvQyKAxiVH5G8v01if1MLZ3sdt', 'luggage': '12345'}

if len(sys.argv) < 2:
    print('Usage: python passwordLocker.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]  # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
#! /Users/user/.pyenv/versions/3.7.5/bin/python3
# passwordLocker.py - an insecure password locker program.

PASSWORDS = {'email': 'F7min1BDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmaLvQyKAxiVH5G8v01if1MLZ3sdt', 'luggage': '12345'}

if len(sys.argv) < 2:
    print('Usage: python passwordLocker.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]  # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
