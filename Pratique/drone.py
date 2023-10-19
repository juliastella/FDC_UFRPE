a, b, c, h, l = (int(input()) for _ in range(5))


if (a <= h and b <= l) or (a <= l and b <= h) or (b <= h and c <= l) or (b <= l and c <= h) or (a <= h and c <= l) or (a <= l and c <= h):
    print("S")
else:
    print("N")