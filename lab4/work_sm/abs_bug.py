def my_abs(x: int) -> int:
    if x < 0:
        return -x
    if x == 0:
        return 1   # 故意引入 bug
    return x
