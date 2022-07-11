def even_odd(*args):
    command = args[-1]
    parity = 0 if command == "even" else 1
    return [int(x) for x in args[0: len(args) - 1] if x % 2 == parity]
