import openpyxl
from junction import Junction
from trafic_light import TrafficLight

min_row = 2
junction_name_col = 2
number_of_traffic_lights_col = 3
junction_path_col = 4
list_of_junctions = []


def set_data(sheet):
    row = min_row
    num_of_junctions = sheet.cell(2, 1).value

    for n in range(num_of_junctions):
        direction = ""
        num_of_traffic_light_in_direction = 0
        col = number_of_traffic_lights_col
        if n != 0:
            row += 1
        junction_name = sheet.cell(row, junction_name_col).value
        num_of_traffic_light_in_junction = sheet.cell(row, number_of_traffic_lights_col).value
        junction = []

        for i in range(num_of_traffic_light_in_junction):
            row += 1

            traffic_lights = []
            col = number_of_traffic_lights_col
            num_of_traffic_light_in_direction = sheet.cell(row, number_of_traffic_lights_col).value
            col += 1
            direction = sheet.cell(row, col).value

            for j in range(num_of_traffic_light_in_direction):
                traffic_light_name = ""
                traffic_light_sign = []
                traffic_light_red_timer = 0
                traffic_light_green_timer = 0

                col += 1
                traffic_light_name = sheet.cell(row, col).value
                col += 1
                traffic_light_sign = sheet.cell(row, col).value.split(",")
                col += 1
                traffic_light_red_timer = sheet.cell(row, col).value.split(",")[0]
                traffic_light_green_timer = sheet.cell(row, col).value.split(",")[1]
                # print(traffic_light_name + " " + traffic_light_red_timer + " " + traffic_light_green_timer)
                # print(traffic_light_sign)

                traffic_lights.append(TrafficLight(traffic_light_name, traffic_light_red_timer,
                                                   traffic_light_green_timer, list(traffic_light_sign)))
                print("Tname=" + traffic_light_name + " ,red/green timer=" + traffic_light_red_timer + "/" + traffic_light_green_timer + ", options:" + str(traffic_light_sign))
                #print(traffic_lights)
            print(traffic_lights.__str__())
            #row += num_of_traffic_light_in_junction
            #junction.append(Junction(junction_name, direction, False, traffic_lights, []))
            name = junction_name + direction
            globals()['%s' % name] = Junction(junction_name, direction, False, traffic_lights, [])
            junction.append(globals()['%s' % name])
        globals()['%s' % junction_name] = junction
        list_of_junctions.append(globals()['%s' % junction_name])
        #print(junction)
    #print(list_of_junctions)

    # row = min_row+1
    # num_of_traffic_lights_at_path = sheet.cell(row, junction_path_col).value
    # junction_path = sheet.cell(row, junction_path_col).value
    # traffic_light_name = sheet.cell(row, junction_path_col+1).value
    # traffic_light_name_data = sheet.cell(row, junction_path_col+2).value
    # print(traffic_light_name_data)
    # turn = traffic_light_name_data.split(',')[0].split("=")[0]
    # cd = traffic_light_name_data.split(',')[0].split("=")[1]
    #
    # a = {
    #     turn: cd
    # }
    # #print(a)


def open_file():
    junction_file = openpyxl.load_workbook("Junction_Info.xlsx")
    sheet1 = junction_file["Sheet1"]
    return sheet1


def extract_junction_info():
    sheet = open_file()
    set_data(sheet)


try:
    extract_junction_info()

except FileExistsError as error:
    print(error)
except EOFError as error:
    print(error)
except FileNotFoundError as error:
    print(error)



