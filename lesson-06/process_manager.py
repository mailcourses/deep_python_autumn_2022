import multiprocessing


class A:
    x = 42


def multy_func(dct):
    dct["data"] = A()
    dct["qwerty"] = 99


if __name__ == "__main__":
    dct = {}

    print("before", dct)

    p = multiprocessing.Process(target=multy_func, args=(dct,))
    p.start()
    p.join()

    print("after", dct)

    with multiprocessing.Manager() as manager:
        dct = manager.dict()

        print("before", dct)

        p = multiprocessing.Process(target=multy_func, args=(dct,))
        p.start()
        p.join()

        print("after", dct)

