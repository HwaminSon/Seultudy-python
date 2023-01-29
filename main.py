# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# import networkx as nx
import osmnx as ox
import requests
import matplotlib.cm as cm
import matplotlib.colors as colors

ox.config(use_cache=True, log_console=True)


def download_graph(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi 1, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    G = ox.graph_from_place(name, network_type='drive')

    ox.save_graph_shapefile(G, filepath="./data/test0109.shp")
    # fig, ax = ox.plot_graph(G)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    download_graph('대한민국')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
