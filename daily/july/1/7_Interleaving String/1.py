from functools import lru_cache


s1 = "a"
s2 = "b"
s3 = "ab"

memo1 = [[0]*len(s1) for _ in range(len(s2))]
memo2 = [[0]*len(s2) for _ in range(len(s1))]


@lru_cache
def check(s1, s2, s3):
    print("s1,s2,s3: ", s1, s2, s3)
    if s2 == "" and s1 == s3:
        return True

    prefix = ""
    for i in range(len(s1)):
        prefix += s1[i]
        if len(prefix) > len(s3):
            return False

        if s3[:len(prefix)] != prefix:
            return False

        if check(s2, s1[len(prefix):], s3[len(prefix):]):
            return True

    return False


s1 = ""
s2 = ""
s3 = ""

print(check(s1, s2, s3) or check(s2, s1, s3))
