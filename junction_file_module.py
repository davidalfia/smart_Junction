import openpyxl
from junction import Junction
from trafic_light import TrafficLight

#cols numbers
min_row = 2
min_col = 2
junction_name_col = 2
num_of_lanes_col = 3
cardinal_direction_col = 4
red_time_col = 5
green_time_col = 6
traffic_light_number_col = 7
next_junction_col = 8
path_driving_time_col = 9

list_of_junctions = []


def open_file():
    junction_file = openpyxl.load_workbook("Junction_Info.xlsx")
    sheet1 = junction_file["Sheet1"]
    return sheet1


def get_info_from_xslx_file(sheet1):
    for row in range(min_row, sheet1.max_row + 1):
        junction_name = sheet1.cell(row, junction_name_col).value
        number = sheet1.cell(row, 3).value
        j = Junction(junction_name, number, False)
        for i in range(4, 7):
            hit_from = sheet1.cell(row, i).value
            t = TrafficLight(i, 5, hit_from)
            j.add_traffic_light(t)
        list_of_junctions.append(j)



def extract_junction_info():
    sheet = open_file()
    get_info_from_xslx_file(sheet)

try:
    extract_junction_info()

except FileExistsError as error:
    print(error)
except EOFError as error:
    print(error)
except FileNotFoundError as error:
    print(error)



