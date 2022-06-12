def solution(sizes):
    sizes.sort()
    for size in sizes:
        if size[0] < size[1]:
            temp = size[0]
            size[0] = size[1]
            size[1] = temp

    width = 0
    height = 0

    for size in sizes:
        if width < size[0]:
            width = size[0]
        if height < size[1]:
            height = size[1]
    
    return width*height