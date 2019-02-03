# hello = "hello python World !"
# print(hello[-20])
#
# hello = "hello python World !"
# python_string = "Python Programming"
# print(hello[0])
# print(python_string[1:5])
# print(hello[0:4])

# #Concatenation
# a = "Hello "
# b = "Python "
# c = "Programmer"
# print(a+b+c)
#
# #Slice
# print(a[1])
#
# #Range slice
# print(c[0:6])
#
# #Membership
# if "x" in a:
#     print("X is present")
# if "P" in b:
#     print("P is in b.")

# #Membership_2
# hero_list = ["Superman","Batman","IronMan","Spiderman","Captain America","Hulk","Thor","Hawkeye","Black Panther","Black Widow","Doctor Strange"]
# if "Superman" in hero_list:
#     print("Superman is alive.")
# else:
#     print("Superman is dead.")

# #Membership 3
# Game = ["Pubg","Kizi","FortNite","Roblox"]
# if "FortNite" in Game:
#     print("Yeah Fortnite's there but you know it cuz it still sucks.")
# else:
#     print("Nope")
# print("Part 2")
# if "Archit is mad" not in Game:
#     print("I am sad to say its a NNNNOOOOO")
# else:
# #     print("Yeah")
# s = "I am A SuperBoy"
# print(s.capitalize())
# print(s.isalpha())
# print(s.lower())
# print(s.upper())
#
# alp = "abcdefghi"
# print("alp.isalpha()",alp.isalpha())
# print("alp.isalnum()",alp.isalnum())
# print("alp.replace()",alp.replace("abcdefghi", "22220000s"))

# alp1 = "Levicorpa"
# alp2 = alp1.replace("Levicorpa","Wingardiam Leviosa")
# print(alp2)
# final = alp2.replace("Wingardiam Leviosa","Avada Kedarva")
# print(final)

# #function
# def string_to_uppercase(s):
#     y = s.upper()
#     return y
#
#
# output = string_to_uppercase("I am superboy.")
# print(output)
#
# #next level useof functions
# hero_list = ["Superman","Batman","IronMan","Spiderman","Captain America","Hulk","Thor","Hawkeye","Black Panther","Black Widow","Doctor Strange"]
# for hero in hero_list:
#     print(string_to_uppercase(hero))
#
def stoc(s):
    n = s.capitalize()
    return  n
def lwr(s):
    r = s.lower()
    return r
def rplce(s):
    m = s.replace("a","1")
    return  m
hero_list = ["Superman","Batman","IronMan","Spiderman","Captain America","Hulk","Thor","Hawkeye","Black Panther","Black Widow","Doctor Strange"]
for hero in hero_list:
    print(stoc(hero))
    print(lwr(hero))
    print(rplce(hero))


