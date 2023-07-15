# import pandas module to edit the xlsx file spread as CSV or Dataframe
import pandas


# create a function to fetch data from xlsx file using the panda module
def import_excel_data():

    # Declare a variable and import to it the spread as pandas Dataframe
    excel_data = pandas.read_excel('marks.xlsx', sheet_name='Sheet', )

    # create an input searching variable named search_surname
    search_surname = str(input('Search surname: '))

    # Assign input variable search_surname to a new variable named surname_search
    surname_search = search_surname

    # use the surname_search variable to query the Dataframe
    query_var = excel_data.query("Surname == @surname_search")
    print(query_var)

    # find and get the index value from dataframe
    row_index = next(iter(query_var[query_var['Surname'] == surname_search].index))
    print(row_index)

    # This method deletes the data frame
    df = pandas.DataFrame(excel_data.drop(row_index, axis=0))
    # excel_data.drop(row_index, axis=0)
    df.to_excel("marks.xlsx", sheet_name="Sheet", index=False)


import_excel_data()
