# Author: JLOM (jlom@odoo.com)

import sys

# When no name provided, default is Luis
user_name = "Luis"

if len(sys.argv) == 2:
    user_name = sys.argv[1]

print("Hello,", user_name)
