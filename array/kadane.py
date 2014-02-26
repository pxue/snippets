def max_subarray(graph):
    local_max = max = 0

    for x in graph:
        local_max = max(0, local_max + x)
        max = max(max, local_max)

    return max

# O(n), dynamic programming
