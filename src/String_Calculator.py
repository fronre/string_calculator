def String_Calculator(number_string: str) -> int:
    if not number_string:
        return 0

    if "," in number_string:
        parts = number_string.split(",")
        return sum(int(p) for p in parts)

    return int(number_string)
