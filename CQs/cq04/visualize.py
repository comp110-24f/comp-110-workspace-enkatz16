"""File for data visualization, importing functions"""

__author__ = "730748249"

from CQs.cq04.concatenation import concat
from CQs.cq04.coordinates import get_coords

x: str = "123"
y: str = "abc"

print(concat(str1=x, str2=y))
get_coords(xs=x, ys=y)
