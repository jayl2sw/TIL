V = 6

arr = [9, 5, 3, 4, 8, 1]

tree = [0 for _ in range(V+1)]

last = 1

for i in range(len(arr)):
    if not tree[last]:
        tree[last] = arr[i]
    else:
        last += 1
        child = last
        parent = child //2

        tree[child] = arr[i]
        print(tree, parent, child)
        while tree[parent] > tree[child]:
            # 부모와 자식 간에 크기 비교 후 parent가 더 크다면 parent와 child 변경
            tree[parent], tree[child] = tree[child], tree[parent]

            # 자식 위치를 부모로 변경
            child = parent
            # 부모 위의 조상 노드
            parent = child // 2

print(*tree)