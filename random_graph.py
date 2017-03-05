import networkx as nx
import matplotlib.pyplot as plt

n = 40

er_g = nx.erdos_renyi_graph(n=n, p=0.1)

ws_g = nx.watts_strogatz_graph(n=n, k=15, p=0.2)

ba_g = nx.barabasi_albert_graph(n=n, m=5)

random_graphs = (er_g, ws_g, ba_g)

plt.figure(1)

plt.subplot(131)
nx.draw_shell(er_g)
plt.title('ER 网络')

plt.subplot(132)
nx.draw_shell(ws_g)
plt.title('WS 网络')

plt.subplot(133)
nx.draw_shell(ba_g)
plt.title('BA 网络')

plt.show()
