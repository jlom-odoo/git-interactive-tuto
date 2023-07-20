# Author: JLOM (jlom@odoo.com)

import sys
from greeter import Greeter

# When no name provided, default is Luis
user_name = "Luis"

if len(sys.argv) == 2:
    user_name = sys.argv[1]

greeter = Greeter(user_name)
greeter.greet()
