students= ["div", "sam", "sun", "mai", "peh", "prer"]

for name in students:
    if name == "sun":
        print("We found his name {0} ".format(name))
        break
    else:
        print("Currently testing for name {0} " .format(name))
