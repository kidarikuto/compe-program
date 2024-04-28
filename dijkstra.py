#自作関数のインポート
import my_func
def dijkstra(edges, num_node):
    """ 経路の表現
            [終点, 辺の値]
            A, B, C, D, ... → 0, 1, 2, ...とする 
    始点の位置
    [
    0[ [終点,辺の値],・・・]
    1[ [2,3],[3,3],[4,3]   ]
    2[ [], [], [] ]
    ]
    """
    node = [float('inf')] * num_node    #スタート地点以外の値は∞で初期化
    node[0] = 0     #スタートは0で初期化
    node_name = [i for i in range(num_node)]     #ノードの名前を0~ノードの数で表す

    while len(node_name) > 0:
        r = node_name[0]
        #最もコストが小さい頂点を探す
        for i in node_name:
            if  node[i] < node[r]:
                r = i   #コストが小さい頂点が見つかると更新
        #最もコストが小さい頂点を取り出す
        min_point = node_name.pop(node_name.index(r))
        #経路の要素を各変数に格納することで，視覚的に見やすくする
        #コスト最小点の辺のリストを参照している
        if min_point == num_node-1:
            return node
        for factor in edges[min_point]:
            
            goal = factor[0]   #終点
            cost  = factor[1]   #コスト

            #更新条件
            if node[min_point] + cost < node[goal]:
                node[goal] = node[min_point] + cost 
        #print(node)
    return node

if __name__ == '__main__':
    N = int(input())
    edge = []
    for i in range(N-1):
        a,b,x = map(int,input().split())
        edge.append([[i+1,a],[x-1,b]])
    node = my_func.dijkstra(edge,N)
    print(node[-1])