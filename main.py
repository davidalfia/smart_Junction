from junction_file_module import extract_junction_info
from _ast import And
from trafic_light import TrafficLight
from anytree import Node, RenderTree
from anytree.exporter import DotExporter
from junction import Junction
from roadUser import RoadUser
from controller import Controller
try:

    c = Controller()
    c.set_map()
    c.build_users()
    c.start_simulation(False)
    c.start_simulation(True)
    c.display_result()

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

