boxTypes = [[1, 3], [2, 2], [3, 1]]

boxTypes.sort(key=lambda x: -x[1])
truckSize = 4

box_cnt = 0
max_unit = 0


for item in boxTypes:
    box_cnt += item[0]
    max_unit += item[0] * item[1]
    if box_cnt > truckSize:
        max_unit -= (box_cnt - truckSize) * item[1]
        break


print(max_unit)
