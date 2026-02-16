import keyword
import string
var_name = input()
allowed_chars = string.ascii_letters + string.digits + '_'
allowed = False
for ch in var_name:
    if ch in allowed_chars:
        allowed = True
    else:
        allowed = False
        break
if allowed and var_name not in keyword.kwlist \
        and var_name[0].isalpha():
    print('True')
else:
    print('False')