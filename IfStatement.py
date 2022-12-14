# temparature = 1
#
# if temparature > 30:
#     print("It's a Hot Day.")
#     print("Plenty of water.")
# elif temparature > 20: # (20, 30)
#     print("It's a nice day")
# elif temparature > 10: # (10,20)
#     print(("It's a bit cold"))
# else:
#     print("it's Cold")
# print("Done")

# is_conv = input("What do you want to convert to(kg/lbs)? ")
# if is_conv == "kg":
#     lbs = float(input("What is you're weight in pounds? "))
#     kg = lbs / 2.20462
#     print(kg)
# if is_conv == "lbs":
#     kg = float(input("What is you're weight in kilograms? "))
#     lbs = kg * 2.20462
#     print (lbs)

weight = float(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    converted = weight / 0.45
    print("Weight in Lbs: " + str(converted))
else:
    converted = weight * 0.45
    print(("Weight in Kgs: ") + str(converted))
