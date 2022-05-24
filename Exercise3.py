# This code produces a class of CreateList to save the names and the numbers in it.
# It can be used for adding or removing names and grades. It can also search for an input name's grade.
class CreateList():
    def __init__(self, max_students, grade_limit):
        # Maximum number of students that our list can save.
        self.max_students = max_students
        # Maximum grade of the students.
        self.grade_limit = grade_limit
        self.all_data = {}
    
    def add_grade(self, name, grade):
        # Checking that the grade is in the defined range.
        if grade < self.grade_limit :
            # Checking the list to see the number of elements don't exceed the threshold.
            if len(self.all_data) < self.max_students:
                self.all_data[name] = grade
            else:
                print("The list is full!")
        else:
            print("The imported number is not in the range of grades!")
            
    # This method is used for removing a name and the corresponding grade from the list.
    def remove_grade(self, name):
        if name in self.all_data.keys():
            self.all_data.pop(name)
        else:
            print("The imported name is not in the list")
            
    # This method is used to search for a name's grade.
    def search_name(self, name):
        if name in self.all_data.keys():
            return self.all_data[name]
        else:
            print("There is no student with the name of {}".format(name))