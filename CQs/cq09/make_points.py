from CQs.cq09.point import Point

random_point = Point(1, 2)
random_point.scale_by(3)
print(random_point.y)

random_point_2 = Point(1, 2)
random_point_3 = random_point_2.scale(3)
print(random_point_2.y)
print(random_point_3.y)
