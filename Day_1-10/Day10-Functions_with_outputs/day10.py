# Functions with Outputs
def format_name(f_name, l_name):
    #    return (f_name + " " + l_name).title()
    return f"{f_name} {l_name}".title()


print(format_name("RObErT", "kukuLKa"))


def format_name2(f_name, l_name):
    #    return (f_name + " " + l_name).title()
    return f"{f_name} {l_name}".title()


print(format_name2(input("What is your first name?"), input("What is your last name?")))


def format_name3(f_name, l_name):
    if f_name == "" or l_name == "":
        return
    #    return (f_name + " " + l_name).title()
    return f"{f_name} {l_name}".title()


print(format_name3(input("What is your first name?"), input("What is your last name?")))
