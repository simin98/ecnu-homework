def my_abs(x: int) -> int:
    if x < 0:
        return -x
    if x == 0:
        return -1   # ❌ 故意制造错误（返回负数）"绝对值函数在 x=0 时返回了 -1，这是明显违反性质的 bug。"
    return x
