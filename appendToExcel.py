# import inputs
import pandas

if __name__ == "__main__":

    name_request = str(input('Enter name of learner: '))
    surname_request = str(input('Enter Surname of learner: '))
    request_pr_marks = int(input('Provide Prepared Reading Marks: '))
    request_us_marks = int(input('Provide Unprepared Speech Marks: '))
    request_ur_marks = int(input('Provide Unprepared Reading Marks: '))

    def request_surname():
        leaner_surname = surname_request
        return leaner_surname

    # define a function to request for name
    def request_name():
        learner_name = name_request
        return learner_name

    # define a function for full names
    def full_learner_names():
        learner_full_names = request_name() + ' ' + request_surname()
        return learner_full_names

    # define a function to request for prepared reading marks
    def input_pr_marks():
        pr_marks = request_pr_marks
        return pr_marks

    # define a function to request unprepared speech marks
    def input_us_marks():
        us_marks = request_us_marks
        return us_marks

    # define a function to request for unprepared reading marks

    def input_ur_marks():
        ur_marks = request_ur_marks
        return ur_marks

    def append_new_dataset():
        appending_dataset = {'Name': [request_name()],
                             'Surname': [request_surname()],
                             'Prepared Reading': [input_pr_marks()],
                             'Unprepared Speech': [input_us_marks()],
                             'Unprepared Reading': [input_ur_marks()],

                             }
        # create a new dataset to append to Excel file spreadsheet
        new_dataframe = pandas.DataFrame(appending_dataset)

        # create a variable to read Excel file
        reader = pandas.read_excel("marks.xlsx")

        # create a variable to write to Excel
        writer = pandas.ExcelWriter("marks.xlsx", mode='a', if_sheet_exists='overlay')

        # send new_dataset to Excel
        new_dataframe.to_excel(writer,
                               sheet_name="Sheet",
                               index=True,
                               header=False,
                               startcol=0,
                               startrow=len(reader)+1)

        # close writer Excel sheet
        writer.close()

        # print output results
        print("Appended successfully. ")

        # return new_dataframe


    # call append_new_dataset
    append_new_dataset()
