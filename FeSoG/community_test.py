from user import user
import networkx as nx
import pickle
import community as community_louvain
import matplotlib.cm as cm
import matplotlib.pyplot as plt

class community():
    def __init__(self, user_list) -> None:
        self.user_list = user_list

    def drawGraph(self, user_list):
        G = nx.Graph()
        print(user_list[0].id_self)
        print(user_list[0].neighbors)
        for u in user_list:
            G.add_node(u.id_self) #增加了1节点
        for u in user_list:
            for social_u in u.neighbors:
                G.add_edge(u.id_self,social_u)
        partition = community_louvain.best_partition(G)
        print(partition[873])
        print(partition)
        # draw the graph
        community_dict = {}
        for p in partition:
                community_dict[partition[p]]=[]
        for p in partition:
                community_dict[partition[p]].append(p)
        print(community_dict)
        return community_dict