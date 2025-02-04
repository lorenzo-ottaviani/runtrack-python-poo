class Student:
    """ Class to manage "La Plateforme" students. """

    def __init__(self, first_name, last_name, student_number, student_credits=0):
        """ Initialisation of the class. """
        self.__first_name = first_name
        self.__last_name = last_name
        self.__student_number = student_number
        self.__student_credits = student_credits
        self.__level = self.__students_eval()

    def add_credits(self, credits_amount):
        """
        Add an amount of credits to student credits.
        :param credits_amount: The number of credits to add.
        :return: ∅
        """
        try:
            credits_amount = int(credits_amount)
            if credits_amount > 0:
                self.__student_credits += credits_amount
                self.__level = self.__students_eval()
            else:
                print("Credits value must be positive")
        except ValueError:
            print("Not an integer")

    def __students_eval(self):
        """
        Evaluate a student.
        :return: Student grade.
        """
        if self.__student_credits >= 90:
            grade = "Zeus"
        elif 80 <= self.__student_credits < 90:
            grade = "Hercules"
        elif 70 <= self.__student_credits < 80:
            grade = "Caesar"
        elif 60 <= self.__student_credits < 70:
            grade = "Otto von Bismarck"
        else:
            grade = "Lieutenant Colonel Custer"
        return grade

    def students_info(self):
        """"""
        infos = (f"Student informations!\nFirst name: {self.__first_name}\nLast name: {self.__last_name}\n"
                 f"Student number: {self.__student_number}\nCredits: {self.__student_credits}\n"
                 f"Grade reached: {self.__level}\n")
        return infos


student_1 = Student("Patrick", "Rascasse", 2024.00253)
student_1.add_credits(47)
print(student_1.students_info())

student_2 = Student("Chenapan", "Ultime", 2024.00787)
student_2.add_credits(78)
print(student_2.students_info())
