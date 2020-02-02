import cProfile


def simple_generator(val):
    while val > 0:
        val -= 1
        yield 1


gen_iter = simple_generator(5)
cProfile.run('sum((i * 2 for i in range(10000000) if i % 3 == 0 or i % 5 == 0))') # выражение генератора
cProfile.run('sum([i * 2 for i in range(10000000) if i % 3 == 0 or i % 5 == 0])') # генератор списка 