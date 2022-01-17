

def area_or_perimeter(length, width):
    if length == width:
        return length * width
    
    return (length * 2) + (width * 2)


print(area_or_perimeter(6, 10))
print(area_or_perimeter(4, 5))