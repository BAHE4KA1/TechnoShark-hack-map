import osmnx as ox
from random import *

def traffic():
    city_name = 'Краснодар'

    graph = ox.graph_from_place(city_name, network_type='all')

    gdf_nodes, gdf_edges = ox.graph_to_gdfs(graph)

    streets = gdf_edges['name'].dropna().tolist()

    a = []
    for s in streets:
        if type(s) == type([]):
            for i in s:
                if i not in a: a.append(i)
        else:
            if s not in a: a.append(s)

    streets = a

    t = [f'{i}:00' for i in range(0, 24)]
    t = t + [f'{i}:30' for i in range(0, 24)]

    k = 10
    for i in streets:
        k -= 1
        log = Streets(name=i, traffic_value=randint(1, 10), time_start=choice(t))
        print(log)
        if k == 0: break