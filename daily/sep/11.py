n = 6
speed = [2, 10, 3, 1, 5, 8]
efficiency = [5, 4, 3, 9, 7, 2]
k = 2

candidates = list(zip(efficiency, speed))

candidates = sorted(candidates, key=lambda x: x[0], reverse=True)

print(candidates)
speed_heap = []
speed_sum, perf = 0, 0
for curr_efficiency, curr_speed in candidates:
    if len(speed_heap) > k-1:
        pass
