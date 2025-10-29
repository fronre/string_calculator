def String_Calculator(number_string: str) -> int:
    if not number_string:
        return 0

    parts = number_string.split(",")

    if len(parts) == 1:
        return int(parts[0])

    return int(parts[0]) + int(parts[1])
