from junction_file_module import list_of_junctions
from trafic_light import TrafficLight
from anytree import Node, RenderTree
from anytree.exporter import DotExporter
from junction import Junction
from roadUser import RoadUser
from controller import Controller

try:
    u1 = RoadUser("david", "south", 10, 0, "A")
    A1 = TrafficLight("A1", 100, 1, right="south")
    A2 = TrafficLight("A2", 100, 1, left="north", straight="east")
    B1 = TrafficLight("B1", 100, 1, straight="south", left="east")
    C1 = TrafficLight("B1", 100, 1, straight="north", right="east")
    A = Junction("A", 2, False, A1, A2, Asouth="B", north="C", east=None, west=None)
    B = Junction("B", 1, False, B1, south=None, north=None, east=None, west=None)
    C = Junction("C", 1, False, C1, south=None, north=None, east=None, west=None)
    c = Controller(A=A, B=B, C=C)

    """"
    print("----------")
    print("start here-->")
    print(u1)
    traffic_l, next_cd = A.get_traffic_light_by_turn_choice("right")
    print(traffic_l)
    nextJ_name = A.get_next_junction_by_cd(next_cd)
    nextJunc = c.get_junction_from_map(nextJ_name)
    u1.set_curr_cardinal_direction(next_cd)
    u1.add_travel_time(traffic_l.get_curr_timer_red())
    u1.set_current_junction(nextJ_name)
    print(u1)
    traffic_l, next_cd = nextJunc.get_traffic_light_by_turn_choice("straight")
    print(traffic_l)
    nextJ_name = nextJunc.get_next_junction_by_cd(next_cd)
    u1.set_curr_cardinal_direction(next_cd)
    u1.add_travel_time(traffic_l.get_curr_timer_red())
    """

    """"
    s = A.name+B.name;
    print(c.get_path_time(s))
    print(c.get_path_time(s))
    print(c.get_path_time("AD"))
    print(c.get_path_time("AA"))
    """

    """"
    u2 = RoadUser("2","south",0,0,"A")
    u3 = RoadUser("3","south",0,0,"A")
    u4 = RoadUser("4","south",0,0,"A")
    u5 = RoadUser("5","south",0,0,"A")

    A1.push_user_to_traffic_light(u2)
    A1.display_current_queue_size()
    u = A1.pop_user_from_traffic_light()
    A1.display_current_queue_size()
    """
    print(u1)
    current_junction_name = u1.get_current_junction_name()
    junction = c.get_junction_from_map(current_junction_name)
    #from A posibble are: left:north:c ,right:south:B,straight:east:None
    current_traffic_light, next_user_cardinal_direction = junction.get_traffic_light_and_next_cd_by_turn_choice("left")
    next_junction_in_user_path_name = junction.get_next_junction_by_cd(next_user_cardinal_direction)
    current_traffic_light.push_user_to_traffic_light(u1)
    u1.set_curr_cardinal_direction(next_user_cardinal_direction)
    u1.add_travel_time(current_traffic_light.get_curr_timer_red(u1.get_social_priority(),junction.get_is_smart()))
    u1.set_current_junction(next_junction_in_user_path_name)
    s = current_junction_name+next_junction_in_user_path_name
    u1.add_travel_time(c.get_path_time(s))
    current_traffic_light.pop_user_from_traffic_light()
    print(u1)

    u1.set_current_junction("A")
    u1.restart_travel_time()
    print("--------------------------")
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


except ImportError as error:
    print(error)
except IndexError as error:
    print(error)
except MemoryError as error:
    print(error)
except NameError as error:
    print(error)


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

