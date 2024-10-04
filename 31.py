from collections import defaultdict


def tarjan_scc(graph):
    index = 0
    stack = []
    indices = {}
    lowlinks = {}
    on_stack = defaultdict(bool)
    sccs = []

    def strongconnect(node):
        nonlocal index
        indices[node] = index
        lowlinks[node] = index
        index += 1
        stack.append(node)
        on_stack[node] = True

        for neighbor in graph[node]:
            if neighbor not in indices:
                strongconnect(neighbor)
                lowlinks[node] = min(lowlinks[node], lowlinks[neighbor])
            elif on_stack[neighbor]:
                lowlinks[node] = min(lowlinks[node], indices[neighbor])

        if lowlinks[node] == indices[node]:
            scc = []
            while True:
                w = stack.pop()
                on_stack[w] = False
                scc.append(w)
                if w == node:
                    break
            sccs.append(scc)

    nodes = list(graph.keys())
    for node in nodes:
        if node not in indices:
            strongconnect(node)

    return sccs


def solution(graph):
    graph = defaultdict(list, graph)
    sccs = tarjan_scc(graph)

    largest = max(sccs, key=len)
    recursive = {func: False for func in graph}

    for scc in sccs:
        if len(scc) > 1 or (len(scc) == 1 and scc[0] in graph[scc[0]]):
            for func in scc:
                recursive[func] = True

    return largest, recursive


tests = [
    {"foo": ["bar"], "bar": ["bazz"], "baZ": ["baZZZ"], "bazz": ["foo"], "baZZZ": ["baZZZ"]},
    {"foo": ["baz", "bar", "foo1"], "bar": ["baz", "foo2", "foo1"], "foo1": ["foo2"], "foo2": ["foo2"]},
    {"foo": ["bar", "bar2"], "bar": ["bar1", "foo", "baz"]}
]

for case in tests:
    largest_scc, recursive = solution(case)
    print('Наибольшая рекурсивная компонента:', largest_scc)
    print('Рекурсивные вызовы для каждой функции:')
    for func, is_recursive in recursive.items():
        print(f"{func}: {'Y' if is_recursive else 'N'}")
    print('\n')
