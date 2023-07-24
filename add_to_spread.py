# import pandas

import pandas


# define a function to request name
def request_name(name_request):
    learners_name = name_request
    return learners_name


# define a function to request for surname
def request_surname(surname_request):
    learners_surname = surname_request
    return learners_surname


# define a function for full names learner
def full_learner_names():
    learner_full_names = learner_name + " " + learner_surname
    print(f"Learner full names: {learner_full_names}")
    return learner_full_names


# define a function to request for prepared reading marks
def input_pr_marks(request_pr_marks):
    pr_marks = request_pr_marks
    return pr_marks


# define a function to request unprepared speech marks
def input_us_marks(request_us_marks):
    us_marks = request_us_marks
    return us_marks


# define a function to request for unprepared reading marks
def input_ur_marks(request_ur_marks):
    ur_marks = request_ur_marks
    return ur_marks


# define a function to request for learner's total marks
def learner_total_marks():
    # Try and except integer input of none numeric values
    try:
        lt_marks = int(pr_marks) + int(us_marks) + int(ur_marks)
    # except the value error
    except ValueError:
        # Provide the message to user
        print("Total", None, "Not applicable, user provided invalid inputs")
    else:
        # if no error print out total marks provided
        print(f"Total: {lt_marks}")


# create pandas data set function term1() using pandas
def term1():
    term1_dataset = {
        'Name': [learner_name],
        'Surname': [learner_surname],
        'Prepared Reading': [pr_marks],
        'Unprepared Speech': [us_marks],
        'Unprepared Reading': [ur_marks],
        }
    # create dataframe variable
    term1_dataframe = pandas.DataFrame(term1_dataset)
    return term1_dataframe


if __name__ == "__main__":

    # Call request name function
    learner_name = request_name(input("Enter name of learner: ").strip())

    # Call request surname function
    learner_surname = request_surname(input("Enter surname of learner: ").strip())

    # Call the full learner names function combined
    full_learner_names()

    # Call input pr marks function
    pr_marks = input_pr_marks(input("Provide Unprepared Speech Marks: ").strip())

    # Call input us marks function
    us_marks = input_us_marks(input("Provide Unprepared Speech Marks: ").strip())

    # Call input ur marks function
    ur_marks = input_ur_marks(input("Provide Unprepared Reading Marks: ").strip())

    # Call learner total marks
    learner_total_marks()

    # Call and ssend term1 function to excell
    # term1()

    # send term1() function data to Excel spreadsheet
    term1().to_excel("marks.xlsx", sheet_name="Sheet", index=False)

    # print term1() data
    print(term1())
