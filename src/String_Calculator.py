def String_Calculator(number_string: str) -> int:
    if not number_string:
        return 0

    parts = number_string.split(",")
    total = 0
    for p in parts:
        if p.strip():
            total += int(p)
    return total
