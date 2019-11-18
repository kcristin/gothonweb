from nose.tools import *
from gothonweb.planisphere import *


def test_room():
    gold = Room("GoldRoom",
                """This room has gold in it you can grab. There's a
                door to the north.""")
    ok_(gold.name, "GoldRoom")
    assert_equals(gold.paths, {})

def test_room_paths():
    center = Room("Center", "Test room in the center.")
    north = Room("North", "Test room in the north.")
    south = Room("South", "Test room in the south.")

    center.add_paths({'north': north, 'south': south})
    ok_(center.go('north'), north)
    ok_(center.go('south'), south)

def test_map():
    start = Room("Start", "You can go west and down a hole.")
    west = Room("Trees", "There are trees here, you can go east.")
    down = Room("Dungeon", "It's dark down here, you can go up.")

    start.add_paths({'west': west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})

    ok_(start.go('west'), west)
    ok_(start.go('west').go('east'), start)
    ok_(start.go('down').go('up'), start)

def test_gothon_game_map():
    start_room = load_room(START)
    ok_(start_room.go('shoot!'), shoot_death)
    ok_(start_room.go('dodge!'), dodge_death)
    room = start_room.go('tell a joke')
    ok_(room, laser_weapon_armory)

    ok_(start_room.go('tell a joke').go('*'), code_death)

    ok_(start_room.go('tell a joke').go('0123').go('throw the bomb'), bomb_death)
    ok_(start_room.go('tell a joke').go('0123').go('slowly place the bomb'), escape_pod)

    ok_(start_room.go('tell a joke').go('0123').go('slowly place the bomb').go('2'), the_end_winner)
    ok_(start_room.go('tell a joke').go('0123').go('slowly place the bomb').go('*'), the_end_loser)
