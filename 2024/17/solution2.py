import z3


def add_cycle(a):
    b = z3.URem(a, 8)
    b = b ^ 5
    denom = z3.BitVecVal(1, 50) << b
    c = z3.UDiv(a, denom)
    b ^= 6
    a = z3.UDiv(a, 8)
    b = b ^ c
    output = z3.URem(b, 8)
    return a, output


def main():
    solver = z3.Solver()

    a_start = z3.BitVec('a_start', 50)

    # going for 16 outputs/cycles, so input is in `range(8^15, 8^16)`
    solver.add(a_start >= 8 ** 15, a_start < 8 ** 16)

    a = a_start
    for tgt in [2, 4, 1, 5, 7, 5, 1, 6, 0, 3, 4, 6, 5, 5, 3, 0]:
        a, output = add_cycle(a)
        solver.add(output == tgt)

    if solver.check():
        print(solver.model())
    else:
        print(f"Unsat")


if __name__ == '__main__':
    main()
