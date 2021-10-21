import pyfiglet
from auto_reg_config import auto_reg_functions, menu_configs
from tabulate import tabulate
from colored import fore, back, style, attr
attr(0)
print(fore.LIGHT_SKY_BLUE_1 + style.BOLD)
print("""Script by Lil Zevi
Github : https://github.com/LilZevi""")
print(pyfiglet.figlet_format("aminoautoregfxck", font="smkeyboard", width=50))
print(tabulate(menu_configs.main_menu, tablefmt="fancy_grid"))
select = input("Select >> ")

if select == "1":
	password = input("Password for All Accounts >> ")
	auto_reg_functions.auto_register(password=password)
	
elif select == "2":
	print("Decode this for getting Account Gen")
	print("TWFtbW90aCwgeW91IHdlcmUgc2NhbW1lZCBsZWFybiBweXRob24KCdCc0LDQvNC+0L3RgiDRgtC10LHRjyDQt9Cw0YHQutCw0LzQuNC70LguINCX0LDRgdC60LDQvNC40Lsg0LzQsNC80L7QvdGC0LA=")
