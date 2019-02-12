# This is the first file I've made in the first Project I've made which intended to be made in pyc and added to an existing repo in gh
# UPDATE: it doesn't add to an existing repo - it creates a new repo of it's own

first_name = input("What's your first name? \n --> \n")
full_name = first_name
surname = input("What's your surname? \n --> \n")

got_mids = input("Here's a question, yes or no, any middle names? \n --> \n")

i = 0
# j = 0

if got_mids == "yes":
    num_mids = int(input("Ah cool, how many? \n --> \n"))
    middle_names = [0] * num_mids

    # Alternate (very flexible) way to create list:
    # lst = []
    # for j in range(10):
    #     lst.append(j)

    # Another great way:
    # my_lst = [k for k in range(10)]

    while i < num_mids:
        middle_names[i] = input("What is middle name number %d? \n --> \n" % (i+1))
        full_name = full_name + " " + middle_names[i]
        i = i +1

    full_name = full_name + " " + surname
    print("Lemme guess, your full name is " + full_name)

elif got_mids == "no":
    full_name = full_name + " " + surname
    print("Cool, in that case, your name must be " + full_name)

else:
    print("Woops, I didn't understand that respone...")