from heapq import heappush, heappop
k = 2
prices = [0, 3, 2, 7, 6, 9, 12, 17, 2, 8, 1, 26]
n, ret, v, p = len(prices), 0, 0, 0
profits, vp_pairs = [], []
while p < n:
    # find next valley/peak pair
    v = p
    while v < n-1 and prices[v] >= prices[v+1]:
        v += 1
    p = v+1
    while p < n and prices[p] >= prices[p-1]:
        p += 1
    print(v, p)
    # save profit of 1 transaction at last v/p pair, if current v is lower than last v
    # this way we always chose to process the pair with hugest profit
    print("WHILE LOOP 1: ")
    print("vp_pairs: ", vp_pairs, "profits: ", profits)
    while (vp_pairs and prices[v] < prices[vp_pairs[-1][0]]):
        temp = vp_pairs.pop()
        # use negative profits in min heap to become a max heap
        heappush(profits, -prices[temp[1]-1]+prices[temp[0]])
    print("vp_pairs: ", vp_pairs, "profits: ", profits)

    # save profit difference between 1 transaction (last v and current p) and 2 transactions (last v/p + current v/p),
    # if current v is higher than last v and current p is higher than last p
    # this way we process the two end of this V/Ps, and if we have k left, we continue to get profit between this two end
    print("WHILE LOOP 2: ")
    print("vp_pairs: ", vp_pairs, "profits: ", profits)
    while (vp_pairs and prices[p-1] >= prices[vp_pairs[-1][1]-1]):
        heappush(profits, -prices[vp_pairs[-1][1]-1]+prices[v])
        v = vp_pairs.pop()[0]

    vp_pairs.append((v, p))
    print("vp_pairs: ", vp_pairs, "profits: ", profits)


# save profits of the rest v/p pairs
print("WHILE DONED: ")
print("vp_pairs: ", vp_pairs, "profits: ", profits)
while vp_pairs:
    temp = vp_pairs.pop()
    heappush(profits, -prices[temp[1]-1]+prices[temp[0]])
print("vp_pairs: ", vp_pairs, "profits: ", profits)

# sum up first k highest profits
k = min(k, len(prices))
for i in range(k):
    if profits:
        ret -= heappop(profits)
    else:
        break

print(ret)
