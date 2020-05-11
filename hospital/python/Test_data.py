vertex_list = [
    ["CH", {"weight": 100, "loading time": 10}],
    ["MF", {"weight": 90, "loading time": 11}],
    ["OC", {"weight": 80, "loading time": 12}],
    ["OG", {"weight": 70, "loading time": 13}],
    ["OR", {"weight": 60, "loading time": 14}],
    ["QC", {"weight": 50, "loading time": 15}],
    ["HH", {"weight": 40, "loading time": 16}],
    ["GH", {"weight": 30, "loading time": 17}]
]

test_1_vertex_list = [
    ["CH", {"weight": 100, "time": 10}],
    ["MF", {"weight": 90, "time": 11}]
]

test_2_vertex_list = [
    ["CH", {"weight": 100, "time": 10}],
    ["MF", {"weight": 90, "time": 11}],
    ["OC", {"weight": 80, "time": 12}]
]

test_3_vertex_list = [
    ["CH", {"weight": 100, "time": 10}],
    ["MF", {"weight": 90, "time": 11}],
    ["OC", {"weight": 80, "time": 12}],
    ["OG", {"weight": 70, "time": 13}]
]

edge_list = [
    ["CH", "MF", {"distance": 20, "time": 12}],
    ["CH", "OC", {"distance": 19, "time": 11}],
    ["CH", "OG", {"distance": 5, "time": 1}],
    ["CH", "OR", {"distance": 6, "time": 2}],
    ["CH", "QC", {"distance": 23, "time": 17}],
    ["CH", "HH", {"distance": 24, "time": 18}],
    ["CH", "GH", {"distance": 26, "time": 20}],
    ["MF", "OC", {"distance": 20, "time": 12}],
    ["MF", "OG", {"distance": 20, "time": 12}],
    ["MF", "OR", {"distance": 20, "time": 12}],
    ["MF", "QC", {"distance": 25, "time": 19}],
    ["MF", "HH", {"distance": 23, "time": 17}],
    ["MF", "GH", {"distance": 26, "time": 20}],
    ["OC", "OG", {"distance": 21, "time": 13}],
    ["OC", "OR", {"distance": 18, "time": 10}],
    ["OC", "QC", {"distance": 18, "time": 10}],
    ["OC", "HH", {"distance": 22, "time": 16}],
    ["OC", "GH", {"distance": 25, "time": 19}],
    ["OG", "OR", {"distance": 8, "time": 4}],
    ["OG", "QC", {"distance": 24, "time": 18}],
    ["OG", "HH", {"distance": 25, "time": 19}],
    ["OG", "GH", {"distance": 28, "time": 21}],
    ["OR", "QC", {"distance": 22, "time": 16}],
    ["OR", "HH", {"distance": 23, "time": 16}],
    ["OR", "GH", {"distance": 24, "time": 19}],
    ["QC", "HH", {"distance": 30, "time": 23}],
    ["QC", "GH", {"distance": 35, "time": 26}],
    ["HH", "GH", {"distance": 20, "time": 12}]
]

test_1_edge_list = [
    ["CH", "MF", {"distance": 20, "time": 12}]
]

test_2_edge_list = [
    ["CH", "MF", {"distance": 20, "time": 12}],
    ["CH", "OC", {"distance": 19, "time": 11}],
    ["MF", "OC", {"distance": 20, "time": 15}]
]

test_3_edge_list = [
    ["CH", "MF", {"distance": 20, "time": 12}],
    ["CH", "OC", {"distance": 19, "time": 11}],
    ["CH", "OG", {"distance": 5, "time": 1}],
    ["OC", "OG", {"distance": 15, "time": 13}],
    ["MF", "OG", {"distance": 20, "time": 12}],
    ["MF", "OC", {"distance": 20, "time": 15}]
]
