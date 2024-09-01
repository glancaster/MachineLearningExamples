def f(x):
    from time import sleep 
    sleep(.1)
    return x**2




lists = {
"expensive_list": [f(x) for x in range(100) if f(x) > 10],
"generator_on_expensive": [v for v in (f(x) for x in range(100)) if v > 10],
"builtin_map_expensive": [v for v in map(f, range(100)) if v > 10],
}



for l in lists.values():
    print(l)
