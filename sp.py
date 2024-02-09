def sphere_volume(radius):
    pi = 3.141
    volume = (4 / 3) * pi * (radius ** 3)
    return volume
radius = float(input("Введите радиус: "))
volume = sphere_volume(radius)
print("Объем сферы равен: ", volume)
