
class Student(object):
    
        """
        Returns a '''Student''' object with the given name, branch and year.

        """
        def __init__(self, name, branch, year):
            self.name = name
            self.branch = branch
            self.year = year
            print("A Student object is created.")

        def print_details(self):

        """
        Prints the details of the student.
        """

        print("Name:", self.name)
        print("Branch:", self.branch)
        print("Year:", self.year)
