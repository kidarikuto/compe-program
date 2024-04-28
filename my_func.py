
def dijkstra(edges, num_node):
    """ 経路の表現(edges)
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

class UnionFind():
    #初期化
    def __init__(self, n):
        self.par  = [-1]*n #要素xの親頂点の番号(自身が根の場合は-1)
        self.rank = [0]*n  #要素xの属する根付き木の高さ
        self.siz  = [1]*n  #要素xの属する根付き木に含まれる頂点数
    
    #根を求める
    def root(self,x):
        if self.par[x] == -1: 
            return x
        else:
            #工夫2 経路圧縮
            #return root(par[x])
            self.par[x] = self.root(self.par[x])
            return self.par[x]
        
    #xとyが同じグループに属するか(根が一致するか)
    def issame(self, x, y):
        return self.root(x) == self.root(y)
    
    #xを含むグループとyを含むグループを併合する
    def unite(self, x, y):
        #x側とy側の根を調べる
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry:
            return False
        
        #工夫1 union by rank    2^(高さh)<頂点数N <=> 高さh<logN
        #ry側のランクを小さくする
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        #ryをrxの子にする
        self.par[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        self.siz[rx] += self.siz[ry]
        return True

    #xを含む根付き木のサイズを求める
    def size(self, x):
        return self.siz[self.root(x)]



if __name__ == '__main__':
    H, W = map(int,input().split())
    Q = int(input())
    trout = [[0 for i in range(W)] for j in range(H)]

    test = UnionFind(H*W)
    for i in range(Q):
        q = list(map(int,input().split()))
        if q[0] == 1:
            trout[q[1]-1][q[2]-1] = 1

            if   q[1]!=H:
                if trout[q[1]][q[2]-1]==1: 
                    test.par[(q[1]-1)*W+q[2]-1] = q[1]*W+q[2]-1
                    test.unite((q[1]-1)*W+q[2]-1, q[1]*W+q[2]-1)
            elif q[2]!=W:
                if trout[q[1]-1][q[2]]==1:    
                    test.par[(q[1]-1)*W+q[2]-1] = (q[1]-1)*W+q[2]
                    test.unite((q[1]-1)*W+q[2]-1, (q[1]-1)*W+q[2])
            elif q[1]!=1:
                if trout[q[1]-2][q[2]-1]==1 :    
                    test.par[(q[1]-1)*W+q[2]-1] = (q[1]-2)*W+q[2]-1
                    test.unite((q[1]-1)*W+q[2]-1, (q[1]-2)*W+q[2]-1)
            elif q[2]!=1:
                if trout[q[1]-1][q[2]-2]==1:    
                    test.par[(q[1]-1)*W+q[2]-1] = (q[1]-1)*W+q[2]-2
                    test.unite((q[1]-1)*W+q[2]-1, (q[1]-1)*W+q[2]-2)
        else:
            if test.issame((q[1]-1)*W+q[2]-1, (q[3]-1)*W+q[4]-1) == True:
                print("Yes")
            else:
                print("No")
        print(trout)
        print(test.par)