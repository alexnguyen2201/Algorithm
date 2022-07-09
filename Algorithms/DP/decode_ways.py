def numDecodings(self, s: str) -> int:
    size = len(s)
    f = [0] * size
    f[0] = s[0]

    count = 0
    for i in range(1, size):
        if f[i-1] == 1:

        elif if f[i-1] == 2:
        else:
            f[i] = f[i - 1]


s = "11106"
print(numDecodings)


def create(user):
    user.password = hash_function(user.password)
    db.add(user)
