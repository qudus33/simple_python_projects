dc_comic = {}
dc_comic["superman"] = "clark kent"
dc_comic["batman"] = "bruce wayne"
dc_comic["wonderwoman"] = "princess diana"
dc_comic["flash"] = "barry allen"
dc_comic["greenlantern"] = "hal jordan"
dc_comic["greenarrow"] = "oliver twist"

heroes_list = dc_comic.keys()
print("DC heroes are: ")
for hero in heroes_list:
    print(hero.title())
name = input("""
    Type the name of a superhero
    to get their identity

>>""")

name = name.lower()
if name not in heroes_list:
    print("Hero not found")
else:
    print("Hero name: {}, secret identity: {}".format(name.title(), dc_comic[name]).title())
