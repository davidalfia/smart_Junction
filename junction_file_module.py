import openpyxl
from junction import Junction
from trafic_light import TrafficLight

min_row = 2
traffic_lights_direction_min_column = 4
junction_name_column = 2
number_of_lanes_column = 3
list_of_junctions = []


def open_file():
    junction_file = openpyxl.load_workbook("Junction_Info.xlsx")
    sheet1 = junction_file["Sheet1"]
    return sheet1


def get_info_from_xslx_file(sheet1):
    for row in range(min_row, sheet1.max_row + 1):
        junction_name = sheet1.cell(row, junction_name_column).value
        number = sheet1.cell(row, number_of_lanes_column).value
        j = Junction(junction_name, number, False)
        for i in range(traffic_lights_direction_min_column, traffic_lights_direction_min_column+number):
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



