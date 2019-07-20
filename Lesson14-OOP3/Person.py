class Person:
    FirstName = ""
    LastName  = ""
    Phone     = ""
    Mail      = ""

    def __str__(self):
        return "{} {}".format(self.FirstName,self.LastName)

