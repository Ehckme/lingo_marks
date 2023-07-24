# importing the module
from openpyxl import Workbook
# import the style for editing Excel cells user_2 = value_id_1, user_1_value_id_1
from openpyxl.styles import Alignment


# define and create a function that creates a workbook spread as .xlsx file
def create_workbook(path):

    workbook = Workbook()
    # Get and access workbook working sheet of the spreadsheet
    sheet = workbook.active

    # Set the height of the required row
    sheet.row_dimensions[1].height = 100
    sheet.row_dimensions[1].width = 10

    # Set the text alignment of the required cells
    cell_adjust_1 = sheet['B1']
    cell_adjust_1.alignment = Alignment(textRotation=90)
    cell_adjust_1 = sheet['C1']
    cell_adjust_1.alignment = Alignment(textRotation=90)
    cell_adjust_1 = sheet['D1']
    cell_adjust_1.alignment = Alignment(textRotation=90)
    cell_adjust_1 = sheet['E1']
    cell_adjust_1.alignment = Alignment(textRotation=90)
    cell_adjust_1 = sheet['F1']
    cell_adjust_1.alignment = Alignment(textRotation=90)

    workbook.save(path)


if __name__ == "__main__":
    # create and assign a new workbook name and set it to path
    create_workbook("marks.xlsx")

# print out message if the file is successfully created
print("A spread file created successfully")
