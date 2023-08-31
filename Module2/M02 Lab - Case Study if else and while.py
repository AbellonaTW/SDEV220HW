#This assignment is required to do before the discussion
lastname = input("Please enter the students last name: ")
while lastname != "ZZZ":
    firstname = input("Please enter students first name: ")
    GPA = float(input("Please enter the student's GPA: "))
    if GPA >= 3.5:
        print(firstname, lastname, "has made the Dean's List.")
    elif GPA >= 3.25:
         print(firstname, lastname, "has made the Honor Roll.")
    else:
        if GPA < 3.25:
            print(firstname, lastname, "is not on any Honor Roll list.")
    lastname = input ("Enter Student Last Name: ")
    #this should repeat until "ZZZ" is typed in

