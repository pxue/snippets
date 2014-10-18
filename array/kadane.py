def max_subarray(graph=[]):
    local_max = gmax = 0

    for x in graph:
        local_max = max(0, local_max + x)
        gmax = max(gmax, local_max)

    return gmax

# O(n), dynamic programming
