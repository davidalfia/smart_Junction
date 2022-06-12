from junction_file_module import extract_junction_info
from _ast import And
from trafic_light import TrafficLight
from anytree import Node, RenderTree
from anytree.exporter import DotExporter
from sub_junction import Junction
from roadUser import RoadUser
from controller import Controller
from controller import junction_map
from controller import users
try:
    c = Controller(junction_map, users)
    c.set_map()
    c.drive(False)

    for u in users:
        print(u)

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
    A = Node(A.get_junction_name())
    MorashaN = Node(Morasha.get_junction_name(), parent=KfarSabeN)
    GlilotN = Node(Glilot.get_junction_name(), parent=MorashaN)
    YarkonN = Node(Yarkon.get_junction_name(), parent=MorashaN)
    BarIlanN = Node(BarIlan.get_junction_name(), parent=MorashaN)
    AlufSadeN = Node(AlufSade.get_junction_name(), parent=BarIlanN)

    for pre, fill, node in RenderTree(KfarSabeN):
        print("%s%s" % (pre, node.name))

    DotExporter(KfarSabeN).to_picture("RaananaJunctionTree.png")
"""





