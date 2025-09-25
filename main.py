from message import get_user_name as pdiddy
import platform
import datetime 
import math

from OOP.Manager import Manager
from OOP.Developer import Developer


dt = datetime.datetime.now()
print(dt.time())
pf = platform.system()

emp1 = Manager("Nathan", 5000, "IT")
emp2 = Developer("Prince", 2300, "HTML")

emp1.show_deets()
print("|_______||_______||_______|")
emp2.show_deets()