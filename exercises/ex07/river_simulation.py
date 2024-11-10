"""Create the actual simulations and river."""

__author__: str = "730748249"

from exercises.ex07.river import River

my_river: River = River(10, 2)
my_river.view_river()
my_river.one_river_week()
