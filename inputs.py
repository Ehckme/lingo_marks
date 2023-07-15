# defining a function for taking surname input | user_2 = value_id_1, user_1 = value_id_1
# import pandas module
import pandas
# from openpyxl import Workbook


# define a function to request for surname
def request_surname():
    leaner_surname = surname_request
    return leaner_surname


# define a function to request for name
def request_name():
    learner_name = name_request
    return learner_name


if __name__ == "__main__":
    # request input for name and surname
    name_request = str(input('Enter name of learner: '))
    surname_request = str(input('Enter Surname of learner: '))

    # define a function for full names
    def full_learner_names():
        learner_full_names = request_name() + ' ' + request_surname()
        return learner_full_names

    # request input for prepared reading marks
    request_pr_marks = int(input('Provide Prepared Reading Marks: '))

    # define a function to request for prepared reading marks
    def input_pr_marks():
        pr_marks = request_pr_marks
        return pr_marks

    # request input for unprepared speech marks
    request_us_marks = int(input('Provide Unprepared Speech Marks: '))

    # define a function to request unprepared speech marks
    def input_us_marks():
        us_marks = request_us_marks
        return us_marks

    # request input for unprepared reading marks
    request_ur_marks = int(input('Provide Unprepared Reading Marks: '))

    # define a function to request for unprepared reading marks
    def input_ur_marks():
        ur_marks = request_ur_marks
        return ur_marks

    # define a function to request for learner's total marks
    def learner_total_marks():
        lt_marks = input_pr_marks() + input_us_marks() + input_ur_marks()
        return lt_marks

    # assign request_name & request_surname function(s) to name and surname variables
    name = request_name()
    surname = request_surname()

    print(f"Learner full names: {full_learner_names()} \n")
    print(f"Term 1 Total Marks {learner_total_marks()}")

    # create pandas data set function term1() using pandas
    def term1():
        term1_dataset = {
            'Name': [request_name()],
            'Surname': [request_surname()],
            'Prepared Reading': [input_pr_marks()],
            'Unprepared Speech': [input_us_marks()],
            'Unprepared Reading': [input_ur_marks()],
        }
        # create dataframe variable
        term1_dataframe = pandas.DataFrame(term1_dataset)

        return term1_dataframe
    # send term1() function data to Excel spreadsheet
    term1().to_excel("marks.xlsx", sheet_name="Sheet", index=True)

    # print term1() data
    print(term1())

    # converts term1() function to CSV file format
    csv_data = term1().to_csv()

    # print csv data
    print(csv_data)

    # create a new pandas dataset function to append
