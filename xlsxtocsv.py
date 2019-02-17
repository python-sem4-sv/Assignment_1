import openpyxl
import csv
#file = "./iris_data.xlsx"
def xlsx_to_csv(file):
    wb = openpyxl.load_workbook(file)
    sheetName = wb.sheetnames[0].replace("\\", "")
    sheet = wb[sheetName]
    with open('./iris_data.csv', 'a', newline='') as output_file:
        for row in sheet:
            rowInfo = []
            for cellObj in row:
                rowInfo.append(cellObj.value)
            output_writer = csv.writer(output_file)
            output_writer.writerow(rowInfo)
    print("finished")
