import openpyxl
import csv
import platform

# created from: https://en.wikipedia.org/wiki/Iris_flower_data_set#Data_set
#filename = './iris_data.xlsx'
def xlsx_to_csv(file):
    wb = openpyxl.load_workbook(file)
    sheet = wb.active
    file_path = file
    output_file_name = file_path[:-4] + "csv"

    with open(output_file_name, 'a', newline="") as output_file:
        output_writer = csv.writer(output_file)
        firstIteration = True
        
        for row in sheet:
            rowArr = []
            
            for cellObj in row:
                rowArr.append(cellObj.value)
            output_writer.writerow(rowArr)
            
            if firstIteration:
                firstLine = ",".join(rowArr)
                firstIteration = False
    
    if firstLine == "Sepal length,Sepal width,Petal length,Petal width,Species":
        print("Unit test complete")
    else:
        print ("Unit test failed")