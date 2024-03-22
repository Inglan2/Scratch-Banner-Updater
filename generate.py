import os
os.system("pip install -U scratchattach")
import scratchattach as scratch3

user = scratch3.get_user("Inglan1")

print(user.join_date)
print(user.about_me)
print(user.wiwo)
print(user.country)
print(user.icon_url)
print(user.id)
print(user.scratchteam)