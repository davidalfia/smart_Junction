from junction_file_module import extract_junction_info
from _ast import And
from trafic_light import TrafficLight
from anytree import Node, RenderTree
from anytree.exporter import DotExporter
from junction import Junction
from roadUser import RoadUser
from controller import Controller
try:
    A1 = TrafficLight("A1", 100, 1, left="north", straight="east")
    A2 = TrafficLight("A2", 100, 1, right="south")
    A3 = TrafficLight("A3", 100, 1, right="west", straight="south")
    A4 = TrafficLight("A4", 100, 1, right="north", straight="west")
    A5 = TrafficLight("A5", 100, 1, left="south")
    A6 = TrafficLight("A6", 100, 1, right="east", straight="north")
    Aeast = Junction("A", "east", False, A1, A2, south="B", north="C", east="E", west=None)
    Anorth = Junction("A", "north", False, A3, south="B", north="C", east="E", west=None)
    Awest = Junction("A", "west", False, A4, A5, south="B", north="C", east="E", west=None)
    Asouth = Junction("A", "south", False, A6, south="B", north="C", east="E", west=None)
    A = [Aeast, Anorth, Awest, Asouth]

    B1 = TrafficLight("B1", 100, 1, left="south", right="north")
    B2 = TrafficLight("B2", 100, 1, straight="north", right="east")
    B3 = TrafficLight("B3", 100, 1, straight="south", left="east")
    Bwest = Junction("B", "west", False, B1, south=None, north="A", east=None, west=None)
    Bsouth = Junction("B", "south", False, B2, south=None, north="A", east=None, west=None)
    Bnorth = Junction("B", "north", False, B3, south=None, north="A", east=None, west=None)
    B = [Bwest, Bsouth, Bnorth]

    C1 = TrafficLight("C1", 100, 1, straight="north", right="east")
    C2 = TrafficLight("C3", 100, 1, left="south", right="north")
    C3 = TrafficLight("C2", 100, 1, straight="south", left="east")
    Csouth = Junction("C", "south", False, C3, south=None, north=None, east="D", west=None)
    Cwest = Junction("C", "west", False, C2, south=None, north=None, east="D", west=None)
    Cnorth = Junction("C", "north", False, C1, south=None, north=None, east="D", west=None)
    C = [Csouth,Cwest,Cnorth]

    D1 = TrafficLight("D1", 100, 1, left="south", straight="west")
    D2 = TrafficLight("D2", 100, 1, straight="east", right="south")
    D3 = TrafficLight("D3", 100, 1,  right="east", left="west")
    Dwest = Junction("D", "west", False, D1, south="E", north=None, east=None, west=None)
    Deast = Junction("D", "east", False, D2, south="E", north=None, east=None, west=None)
    Dsouth = Junction("D", "south", False, D3, south="E", north=None, east=None, west=None)
    D = [Deast,Dwest,Dsouth]

    E1 = TrafficLight("E1", 100, 1, right="north", straight="west")
    E2 = TrafficLight("E2", 100, 1, right="east", left="west")
    E3 = TrafficLight("E2", 100, 1, straight="east",left="north")
    Ewest = Junction("E", "west", False, E1, south=None, north=None, east=None, west=None)
    Esouth = Junction("E", "south", False, E2, south=None, north=None, east=None, west=None)
    Eeast = Junction("E", "east", False, E3, south=None, north=None, east=None, west=None)
    E = [Esouth,Ewest,Eeast]

    junction_map = {
        "A": A,
        "B": B,
        "C": C,
        "D": D,
        "E": E
    }

    users = []
    u1 = RoadUser("david","east",8,"A","E")
    u2 = RoadUser("ran","east",2,"A","D")
    u3 = RoadUser("dana","east",3,"A","D")
    users.append(u1)

    c = Controller(junction_map, users)
    c.drive(True)

except ImportError as error:
    print(error)
except IndexError as error:
    print(error)
except MemoryError as error:
    print(error)
except NameError as error:
    print(error)


    """"
    j = c.get_junction_hit_from_by_junction_name_and_cardinal_direction("A")
    for ju in j:
        if "east" == ju.get_hit_from():
            ju.print_junction()
    """

    """
    u2 = RoadUser("2", "south", 0, 0, "A")
    u3 = RoadUser("3", "south", 0, 0, "A")
    u4 = RoadUser("4", "south", 0, 0, "A")
    u5 = RoadUser("5", "south", 0, 0, "A")

    A1.push_user_to_traffic_light(u2)
    A1.display_current_queue_size()
    u = A1.pop_user_from_traffic_light()
    A1.display_current_queue_size()
    """
    """
    print("--------------start simulation-----------------")
    u1 = RoadUser("david", "east", 8, 0, "A")
    print("David start------------------------------------")
    print(u1)
    current_junction_name = u1.get_current_junction_name()
    junction = c.get_junction_from_map(current_junction_name)
    # from A posibble are: left:north:c ,right:south:B,straight:east:None
    current_traffic_light, next_user_cardinal_direction = junction.get_traffic_light_and_next_cd_by_turn_choice("left")
    next_junction_in_user_path_name = junction.get_next_junction_by_cd(next_user_cardinal_direction)
    current_traffic_light.push_user_to_traffic_light(u1)
    u1.set_curr_cardinal_direction(next_user_cardinal_direction)
    u1.add_travel_time(current_traffic_light.get_curr_timer_red(u1.get_social_priority(), junction.get_is_smart()))
    u1.set_current_junction(next_junction_in_user_path_name)
    s = current_junction_name + next_junction_in_user_path_name
    u1.add_travel_time(c.get_path_time(s))
    current_traffic_light.pop_user_from_traffic_light()
    print(u1)

    current_junction_name = u1.get_current_junction_name()
    junction = c.get_junction_from_map(current_junction_name)
    # from A posibble are: left:north:c ,right:south:B,straight:east:None
    current_traffic_light, next_user_cardinal_direction = junction.get_traffic_light_and_next_cd_by_turn_choice("right")
    next_junction_in_user_path_name = junction.get_next_junction_by_cd(next_user_cardinal_direction)
    current_traffic_light.push_user_to_traffic_light(u1)
    u1.set_curr_cardinal_direction(next_user_cardinal_direction)
    u1.add_travel_time(current_traffic_light.get_curr_timer_red(u1.get_social_priority(), junction.get_is_smart()))
    u1.set_current_junction(next_junction_in_user_path_name)
    s = current_junction_name + next_junction_in_user_path_name
    u1.add_travel_time(c.get_path_time(s))
    current_traffic_light.pop_user_from_traffic_light()
    print(u1)

    current_junction_name = u1.get_current_junction_name()
    junction = c.get_junction_from_map(current_junction_name)
    # from A posibble are: left:north:c ,right:south:B,straight:east:None
    current_traffic_light, next_user_cardinal_direction = junction.get_traffic_light_and_next_cd_by_turn_choice("right")
    next_junction_in_user_path_name = junction.get_next_junction_by_cd(next_user_cardinal_direction)
    current_traffic_light.push_user_to_traffic_light(u1)
    u1.set_curr_cardinal_direction(next_user_cardinal_direction)
    u1.add_travel_time(current_traffic_light.get_curr_timer_red(u1.get_social_priority(), junction.get_is_smart()))
    u1.set_current_junction(next_junction_in_user_path_name)
    s = current_junction_name + next_junction_in_user_path_name
    u1.add_travel_time(c.get_path_time(s))
    current_traffic_light.pop_user_from_traffic_light()
    print(u1)

    print("smart--------------------------")
    u1.set_current_junction("A")
    u1.restart_travel_time()
    print(u1)
    current_junction_name = u1.get_current_junction_name()
    junction = c.get_junction_from_map(current_junction_name)
    junction.set_is_smart(True)
    # from A posibble are: left:north:c ,right:south:B,straight:east:None
    current_traffic_light, next_user_cardinal_direction = junction.get_traffic_light_and_next_cd_by_turn_choice("left")
    next_junction_in_user_path_name = junction.get_next_junction_by_cd(next_user_cardinal_direction)
    current_traffic_light.push_user_to_traffic_light(u1)
    u1.set_curr_cardinal_direction(next_user_cardinal_direction)
    u1.add_travel_time(current_traffic_light.get_curr_timer_red(u1.get_social_priority(), junction.get_is_smart()))
    u1.set_current_junction(next_junction_in_user_path_name)
    s = current_junction_name + next_junction_in_user_path_name
    u1.add_travel_time(c.get_path_time(s))
    current_traffic_light.pop_user_from_traffic_light()
    print(u1)
    current_junction_name = u1.get_current_junction_name()
    junction = c.get_junction_from_map(current_junction_name)
    # from A posibble are: left:north:c ,right:south:B,straight:east:None
    current_traffic_light, next_user_cardinal_direction = junction.get_traffic_light_and_next_cd_by_turn_choice("right")
    next_junction_in_user_path_name = junction.get_next_junction_by_cd(next_user_cardinal_direction)
    current_traffic_light.push_user_to_traffic_light(u1)
    u1.set_curr_cardinal_direction(next_user_cardinal_direction)
    u1.add_travel_time(current_traffic_light.get_curr_timer_red(u1.get_social_priority(), junction.get_is_smart()))
    u1.set_current_junction(next_junction_in_user_path_name)
    s = current_junction_name + next_junction_in_user_path_name
    u1.add_travel_time(c.get_path_time(s))
    current_traffic_light.pop_user_from_traffic_light()
    print(u1)

    current_junction_name = u1.get_current_junction_name()
    junction = c.get_junction_from_map(current_junction_name)
    # from A posibble are: left:north:c ,right:south:B,straight:east:None
    current_traffic_light, next_user_cardinal_direction = junction.get_traffic_light_and_next_cd_by_turn_choice("right")
    next_junction_in_user_path_name = junction.get_next_junction_by_cd(next_user_cardinal_direction)
    current_traffic_light.push_user_to_traffic_light(u1)
    u1.set_curr_cardinal_direction(next_user_cardinal_direction)
    u1.add_travel_time(current_traffic_light.get_curr_timer_red(u1.get_social_priority(), junction.get_is_smart()))
    u1.set_current_junction(next_junction_in_user_path_name)
    s = current_junction_name + next_junction_in_user_path_name
    u1.add_travel_time(c.get_path_time(s))
    current_traffic_light.pop_user_from_traffic_light()
    print(u1)
    print("David end------------------------------------")

    u1 = RoadUser("Dor", "east", 5, 0, "A")
    Aeast.set_is_smart(False)
    print("Dor start------------------------------------")
    print(u1)
    current_junction_name = u1.get_current_junction_name()
    junction = c.get_junction_from_map(current_junction_name)
    # from A posibble are: left:north:c ,right:south:B,straight:east:None
    current_traffic_light, next_user_cardinal_direction = junction.get_traffic_light_and_next_cd_by_turn_choice("left")
    next_junction_in_user_path_name = junction.get_next_junction_by_cd(next_user_cardinal_direction)
    current_traffic_light.push_user_to_traffic_light(u1)
    u1.set_curr_cardinal_direction(next_user_cardinal_direction)
    u1.add_travel_time(current_traffic_light.get_curr_timer_red(u1.get_social_priority(), junction.get_is_smart()))
    u1.set_current_junction(next_junction_in_user_path_name)
    s = current_junction_name + next_junction_in_user_path_name
    u1.add_travel_time(c.get_path_time(s))
    current_traffic_light.pop_user_from_traffic_light()
    print(u1)

    current_junction_name = u1.get_current_junction_name()
    junction = c.get_junction_from_map(current_junction_name)
    # from A posibble are: left:north:c ,right:south:B,straight:east:None
    current_traffic_light, next_user_cardinal_direction = junction.get_traffic_light_and_next_cd_by_turn_choice("right")
    next_junction_in_user_path_name = junction.get_next_junction_by_cd(next_user_cardinal_direction)
    current_traffic_light.push_user_to_traffic_light(u1)
    u1.set_curr_cardinal_direction(next_user_cardinal_direction)
    u1.add_travel_time(current_traffic_light.get_curr_timer_red(u1.get_social_priority(), junction.get_is_smart()))
    u1.set_current_junction(next_junction_in_user_path_name)
    s = current_junction_name + next_junction_in_user_path_name
    u1.add_travel_time(c.get_path_time(s))
    current_traffic_light.pop_user_from_traffic_light()
    print(u1)

    current_junction_name = u1.get_current_junction_name()
    junction = c.get_junction_from_map(current_junction_name)
    # from A posibble are: left:north:c ,right:south:B,straight:east:None
    current_traffic_light, next_user_cardinal_direction = junction.get_traffic_light_and_next_cd_by_turn_choice("right")
    next_junction_in_user_path_name = junction.get_next_junction_by_cd(next_user_cardinal_direction)
    current_traffic_light.push_user_to_traffic_light(u1)
    u1.set_curr_cardinal_direction(next_user_cardinal_direction)
    u1.add_travel_time(current_traffic_light.get_curr_timer_red(u1.get_social_priority(), junction.get_is_smart()))
    u1.set_current_junction(next_junction_in_user_path_name)
    s = current_junction_name + next_junction_in_user_path_name
    u1.add_travel_time(c.get_path_time(s))
    current_traffic_light.pop_user_from_traffic_light()
    print(u1)

    print("smart--------------------------")
    u1.set_current_junction("A")
    u1.restart_travel_time()
    print(u1)
    current_junction_name = u1.get_current_junction_name()
    junction = c.get_junction_from_map(current_junction_name)
    junction.set_is_smart(True)
    # from A posibble are: left:north:c ,right:south:B,straight:east:None
    current_traffic_light, next_user_cardinal_direction = junction.get_traffic_light_and_next_cd_by_turn_choice("left")
    next_junction_in_user_path_name = junction.get_next_junction_by_cd(next_user_cardinal_direction)
    current_traffic_light.push_user_to_traffic_light(u1)
    u1.set_curr_cardinal_direction(next_user_cardinal_direction)
    u1.add_travel_time(current_traffic_light.get_curr_timer_red(u1.get_social_priority(), junction.get_is_smart()))
    u1.set_current_junction(next_junction_in_user_path_name)
    s = current_junction_name + next_junction_in_user_path_name
    u1.add_travel_time(c.get_path_time(s))
    current_traffic_light.pop_user_from_traffic_light()
    print(u1)
    current_junction_name = u1.get_current_junction_name()
    junction = c.get_junction_from_map(current_junction_name)
    # from A posibble are: left:north:c ,right:south:B,straight:east:None
    current_traffic_light, next_user_cardinal_direction = junction.get_traffic_light_and_next_cd_by_turn_choice("right")
    next_junction_in_user_path_name = junction.get_next_junction_by_cd(next_user_cardinal_direction)
    current_traffic_light.push_user_to_traffic_light(u1)
    u1.set_curr_cardinal_direction(next_user_cardinal_direction)
    u1.add_travel_time(current_traffic_light.get_curr_timer_red(u1.get_social_priority(), junction.get_is_smart()))
    u1.set_current_junction(next_junction_in_user_path_name)
    s = current_junction_name + next_junction_in_user_path_name
    u1.add_travel_time(c.get_path_time(s))
    current_traffic_light.pop_user_from_traffic_light()
    print(u1)

    current_junction_name = u1.get_current_junction_name()
    junction = c.get_junction_from_map(current_junction_name)
    # from A posibble are: left:north:c ,right:south:B,straight:east:None
    current_traffic_light, next_user_cardinal_direction = junction.get_traffic_light_and_next_cd_by_turn_choice("right")
    next_junction_in_user_path_name = junction.get_next_junction_by_cd(next_user_cardinal_direction)
    current_traffic_light.push_user_to_traffic_light(u1)
    u1.set_curr_cardinal_direction(next_user_cardinal_direction)
    u1.add_travel_time(current_traffic_light.get_curr_timer_red(u1.get_social_priority(), junction.get_is_smart()))
    u1.set_current_junction(next_junction_in_user_path_name)
    s = current_junction_name + next_junction_in_user_path_name
    u1.add_travel_time(c.get_path_time(s))
    current_traffic_light.pop_user_from_traffic_light()
    print(u1)
    print("Dor end------------------------------------")


    u1 = RoadUser("Dana", "east", 1, 0, "A")
    Aeast.set_is_smart(False)
    print("Dana start------------------------------------")
    print(u1)
    current_junction_name = u1.get_current_junction_name()
    junction = c.get_junction_from_map(current_junction_name)
    # from A posibble are: left:north:c ,right:south:B,straight:east:None
    current_traffic_light, next_user_cardinal_direction = junction.get_traffic_light_and_next_cd_by_turn_choice("left")
    next_junction_in_user_path_name = junction.get_next_junction_by_cd(next_user_cardinal_direction)
    current_traffic_light.push_user_to_traffic_light(u1)
    u1.set_curr_cardinal_direction(next_user_cardinal_direction)
    u1.add_travel_time(current_traffic_light.get_curr_timer_red(u1.get_social_priority(), junction.get_is_smart()))
    u1.set_current_junction(next_junction_in_user_path_name)
    s = current_junction_name + next_junction_in_user_path_name
    u1.add_travel_time(c.get_path_time(s))
    current_traffic_light.pop_user_from_traffic_light()
    print(u1)

    current_junction_name = u1.get_current_junction_name()
    junction = c.get_junction_from_map(current_junction_name)
    # from A posibble are: left:north:c ,right:south:B,straight:east:None
    current_traffic_light, next_user_cardinal_direction = junction.get_traffic_light_and_next_cd_by_turn_choice("right")
    next_junction_in_user_path_name = junction.get_next_junction_by_cd(next_user_cardinal_direction)
    current_traffic_light.push_user_to_traffic_light(u1)
    u1.set_curr_cardinal_direction(next_user_cardinal_direction)
    u1.add_travel_time(current_traffic_light.get_curr_timer_red(u1.get_social_priority(), junction.get_is_smart()))
    u1.set_current_junction(next_junction_in_user_path_name)
    s = current_junction_name + next_junction_in_user_path_name
    u1.add_travel_time(c.get_path_time(s))
    current_traffic_light.pop_user_from_traffic_light()
    print(u1)

    current_junction_name = u1.get_current_junction_name()
    junction = c.get_junction_from_map(current_junction_name)
    # from A posibble are: left:north:c ,right:south:B,straight:east:None
    current_traffic_light, next_user_cardinal_direction = junction.get_traffic_light_and_next_cd_by_turn_choice("right")
    next_junction_in_user_path_name = junction.get_next_junction_by_cd(next_user_cardinal_direction)
    current_traffic_light.push_user_to_traffic_light(u1)
    u1.set_curr_cardinal_direction(next_user_cardinal_direction)
    u1.add_travel_time(current_traffic_light.get_curr_timer_red(u1.get_social_priority(), junction.get_is_smart()))
    u1.set_current_junction(next_junction_in_user_path_name)
    s = current_junction_name + next_junction_in_user_path_name
    u1.add_travel_time(c.get_path_time(s))
    current_traffic_light.pop_user_from_traffic_light()
    print(u1)

    print("smart--------------------------")
    u1.set_current_junction("A")
    u1.restart_travel_time()
    print(u1)
    current_junction_name = u1.get_current_junction_name()
    junction = c.get_junction_from_map(current_junction_name)
    junction.set_is_smart(True)
    # from A posibble are: left:north:c ,right:south:B,straight:east:None
    current_traffic_light, next_user_cardinal_direction = junction.get_traffic_light_and_next_cd_by_turn_choice("left")
    next_junction_in_user_path_name = junction.get_next_junction_by_cd(next_user_cardinal_direction)
    current_traffic_light.push_user_to_traffic_light(u1)
    u1.set_curr_cardinal_direction(next_user_cardinal_direction)
    u1.add_travel_time(current_traffic_light.get_curr_timer_red(u1.get_social_priority(), junction.get_is_smart()))
    u1.set_current_junction(next_junction_in_user_path_name)
    s = current_junction_name + next_junction_in_user_path_name
    u1.add_travel_time(c.get_path_time(s))
    current_traffic_light.pop_user_from_traffic_light()
    print(u1)
    current_junction_name = u1.get_current_junction_name()
    junction = c.get_junction_from_map(current_junction_name)
    # from A posibble are: left:north:c ,right:south:B,straight:east:None
    current_traffic_light, next_user_cardinal_direction = junction.get_traffic_light_and_next_cd_by_turn_choice("right")
    next_junction_in_user_path_name = junction.get_next_junction_by_cd(next_user_cardinal_direction)
    current_traffic_light.push_user_to_traffic_light(u1)
    u1.set_curr_cardinal_direction(next_user_cardinal_direction)
    u1.add_travel_time(current_traffic_light.get_curr_timer_red(u1.get_social_priority(), junction.get_is_smart()))
    u1.set_current_junction(next_junction_in_user_path_name)
    s = current_junction_name + next_junction_in_user_path_name
    u1.add_travel_time(c.get_path_time(s))
    current_traffic_light.pop_user_from_traffic_light()
    print(u1)

    current_junction_name = u1.get_current_junction_name()
    junction = c.get_junction_from_map(current_junction_name)
    # from A posibble are: left:north:c ,right:south:B,straight:east:None
    current_traffic_light, next_user_cardinal_direction = junction.get_traffic_light_and_next_cd_by_turn_choice("right")
    next_junction_in_user_path_name = junction.get_next_junction_by_cd(next_user_cardinal_direction)
    current_traffic_light.push_user_to_traffic_light(u1)
    u1.set_curr_cardinal_direction(next_user_cardinal_direction)
    u1.add_travel_time(current_traffic_light.get_curr_timer_red(u1.get_social_priority(), junction.get_is_smart()))
    u1.set_current_junction(next_junction_in_user_path_name)
    s = current_junction_name + next_junction_in_user_path_name
    u1.add_travel_time(c.get_path_time(s))
    current_traffic_light.pop_user_from_traffic_light()
    print(u1)
    print("Dana end------------------------------------")
    print("--------------end simulation-----------------")
    """


"""
try:
    KfarSabe, Morasha, Glilot, Yarkon, BarIlan, AlufSade = list_of_junctions
    KfarSabeN = Node(KfarSabe.get_junction_name())
    MorashaN = Node(Morasha.get_junction_name(), parent=KfarSabeN)
    GlilotN = Node(Glilot.get_junction_name(), parent=MorashaN)
    YarkonN = Node(Yarkon.get_junction_name(), parent=MorashaN)
    BarIlanN = Node(BarIlan.get_junction_name(), parent=MorashaN)
    AlufSadeN = Node(AlufSade.get_junction_name(), parent=BarIlanN)

    for pre, fill, node in RenderTree(KfarSabeN):
        print("%s%s" % (pre, node.name))

    DotExporter(KfarSabeN).to_picture("RaananaJunctionTree.png")

"""

