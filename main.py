from junction_file_module import list_of_junctions
from trafic_light import TrafficLight
from anytree import Node, RenderTree
from anytree.exporter import DotExporter
from junction import Junction
from roadUser import RoadUser
from controller import Controller

try:
    u1 = RoadUser("david", "south", 0, 0, "A" )
    A1 = TrafficLight("A1", 1, 1, right="south")
    A2 = TrafficLight("A2", 1, 1, left="north", straight="east")
    B1 = TrafficLight("B1", 1, 1, straight="south")
    C1 = TrafficLight("B1", 1, 1, straight="north")
    A = Junction("A", 2, False, A1, A2, south="B", north="C", east=None, west=None)
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

