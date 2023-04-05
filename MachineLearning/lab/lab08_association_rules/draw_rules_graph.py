#!/usr/bin/env python
# coding: utf-8

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

def draw_graph(rules, rules_to_show=5):
    """
    draws the rules as a graph linking antecedents and consequents
    "rule nodes" are yellow, with name "R<n>", "item nodes" are green
    arrows colors are different for each rule, and go from the antecedent(s)
    to the rule node and to the consequent(s)
    the "rules_to_show" parameter limits the rules to show to the initial
    part of the "rules" dataframe
    Warning: it requires the package networkx, if necessary pip install networkx
    """
    N = 50
    np.random.seed(42)
    colors = np.random.rand(N)
    G1 = nx.DiGraph()
    color_map = []
    strs = []  # will store the names of the rules   
    for i in range(rules_to_show):
        G1.add_nodes_from(["R" + str(i)])
        strs.append("R" + str(i))  # stores in a list the "names" of the rules
        for a in rules.iloc[i]['antecedents']:
            G1.add_nodes_from([a])
            G1.add_edge(a, "R" + str(i), color=colors[i], weight=2)
        for c in rules.iloc[i]['consequents']:
            G1.add_nodes_from([c])
            G1.add_edge("R" + str(i), c, color=colors[i], weight=2)
    for node in G1:  # set the appropriate color for rule nodes and item nodes
        if node in strs:
            color_map.append('yellow')
        else:
            color_map.append('green')
    edges = G1.edges()
    colors = [G1[u][v]['color'] for u, v in edges]
    weights = [G1[u][v]['weight'] for u, v in edges]
    pos = nx.spring_layout(G1, k=16, scale=1)
    nx.draw(G1, pos, node_color=color_map, edge_color=colors, width=weights,
            font_size=16, with_labels=False)
    for p in pos:  # raise text positions
        pos[p][1] += 0.07
    nx.draw_networkx_labels(G1, pos)
    plt.show()
# ##################
# draw_graph() end #
# ##################

