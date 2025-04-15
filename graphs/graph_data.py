import random

def get_random_graph():
    graphs = [
        # Graph 1: Start and End are far apart, no direct edge
        {
            'nodes': list(range(10)),
            'edges': [
                (0, 1, 7), (1, 2, 5), (2, 3, 6), (3, 4, 2), (4, 5, 8),
                (5, 6, 4), (6, 7, 9), (7, 8, 3), (8, 9, 10), 
                # Start (0) is far from End (9), no direct edge
                (0, 5, 9), (1, 6, 3), (2, 7, 4), (3, 8, 6)
                # Additional edges ensure connectivity
            ]
        },
        # Graph 2: Start and End are far apart, no direct edge
        {
            'nodes': list(range(12)),
            'edges': [
                (0, 1, 5), (1, 2, 8), (2, 3, 4), (3, 4, 6), (4, 5, 2),
                (5, 6, 3), (6, 7, 7), (7, 8, 6), (8, 9, 8), (9, 10, 1),
                (10, 11, 9),
                # Start (0) is far from End (11), no direct edge
                (0, 5, 6), (1, 7, 4), (2, 8, 5), (3, 9, 3), (4, 10, 7)
                # Additional edges ensure connectivity
            ]
        },
        # Graph 3: Start and End are far apart, no direct edge
        {
            'nodes': list(range(8)),
            'edges': [
                (0, 1, 5), (1, 2, 6), (2, 3, 7), (3, 4, 2), (4, 5, 8),
                (5, 6, 3), (6, 7, 4),
                # Start (0) is far from End (7), no direct edge
                (0, 4, 6), (1, 5, 5), (2, 6, 3)
                # Additional edges ensure connectivity
            ]
        },
        # Graph 4: Start and End are far apart, no direct edge
        {
            'nodes': list(range(15)),
            'edges': [
                (0, 1, 7), (1, 2, 9), (2, 3, 5), (3, 4, 4), (4, 5, 8),
                (5, 6, 6), (6, 7, 7), (7, 8, 3), (8, 9, 4), (9, 10, 2),
                (10, 11, 9), (11, 12, 5), (12, 13, 8), (13, 14, 3),
                # Start (0) is far from End (14), no direct edge
                (0, 6, 5), (1, 7, 4), (2, 8, 6), (3, 9, 7), (4, 10, 3)
                # Additional edges ensure connectivity
            ]
        },
        # Graph 5: Start and End are far apart, no direct edge
        {
            'nodes': list(range(20)),
            'edges': [
                (0, 1, 10), (1, 2, 9), (2, 3, 8), (3, 4, 7), (4, 5, 6),
                (5, 6, 5), (6, 7, 4), (7, 8, 3), (8, 9, 2), (9, 10, 1),
                (10, 11, 11), (11, 12, 12), (12, 13, 13), (13, 14, 14),
                (14, 15, 15), (15, 16, 16), (16, 17, 17), (17, 18, 18),
                (18, 19, 19),
                # Start (0) is far from End (19), no direct edge
                (0, 10, 15), (1, 12, 7), (2, 14, 10), (3, 16, 9), (4, 17, 8)
                # Additional edges ensure connectivity
            ]
        }
    ]
    
    g = random.choice(graphs)
    g['start'] = g['nodes'][0]  # Start node
    g['end'] = g['nodes'][-1]  # End node
    return g
