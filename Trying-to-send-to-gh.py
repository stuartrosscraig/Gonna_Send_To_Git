# This is the first file I've made in the first Project I've made which intended to be made in pyc and added to an existing repo in gh

first_name = input("What's your first name? \n -->")
full_name = first_name
surname = input("What's your surname? \n -->")

got_mids = input("Here's a question, yes or no, any middle names? \n -->")

i = 0

if got_mids == "yes":
    num_mids = int(input("Ah cool, how many? \n -->"))
    middle_names = [0] * num_mids
    # print(middle_names[0], middle_names[1], middle_names[2])
    while i < num_mids:
        middle_names[i] = input("What is middle name number %d? \n -->" % (i+1))
        full_name = full_name + " " + middle_names[i]
        i = i +1

    full_name = full_name + " " + surname
    print("Lemme guess, your full name is " + full_name)

# elif got_mult_mids == "no":
#     middle_name_names = input("What is your middle name? \n -->")
#
#
#
# if got_mids == "no":
#     print("Lemme guess, your name is %s %s" % (first_name, surname))
# else:
#     print("This has become too difficult for me...")