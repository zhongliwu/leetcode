# -*- coding: utf-8 -*--

if __name__ == "__main__":
    tuple1 = (1, 2, 3)
    tuple2 = (2, 1, 3)
    tuple3 = (1, 2)

    tuple_set = set()
    tuple_set.add(tuple1)
    tuple_set.add(tuple2)
    tuple_set.add(tuple3)

    tuple4 = (1, 2, 3)
    tuple5 = (2, 1)

    print(tuple4 in tuple_set)
    print(tuple5 in tuple_set)
    print(tuple1[2])
