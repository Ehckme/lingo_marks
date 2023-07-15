import pandas


if __name__ == "__main__":
    # create a function to fetch data from xlsx file using the panda module
    def import_excel_data():
        excel_data = pandas.read_excel('marks.xlsx',
                                       sheet_name='Sheet', )

        #  create a searching variable named search_surname
        search_surname = str(input('Search surname: '))
        surname_search = search_surname

        query_var = excel_data.query("Surname == @surname_search")
        print(query_var)
        # find the index value from data frame
        row_index = next(iter(query_var[query_var['Surname'] == surname_search].index))
        print(row_index)

        return query_var


    import_excel_data()
