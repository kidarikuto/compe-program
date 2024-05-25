def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start)  # 訪問したノードの処理

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)
def find_list(graph,element):
     for i in range(len(graph)):
          for j in range(len(graph[0])):
               if graph[i][j]==element:
                    return [i,j]
# グラフの定義（隣接リスト）
# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F'],
#     'D': ['B'],
#     'E': ['B', 'F'],
#     'F': ['C', 'E']
# }
graph=[
     [1,2,3],
     [4,5,6]
]
element=5
# DFSの実行
# dfs_recursive(graph, 'A')
ans=find_list(graph,element)
print(ans)