#
# This class defines a graph
# An graph includes:
#   - a set of vertices
#   - a set of edges
#
from Vertex import Vertex
from Edge import Edge


class Graph:
    def __init__(self, vertex_list, edge_list):
        self.vertex_set = set()
        vertex_dict = dict()
        for label, props in vertex_list:
            vertex = Vertex(label, props)
            self.vertex_set.add(vertex)
            vertex_dict[label] = vertex

        self.edge_set = set()
        for label_a, label_b, props_ab in edge_list:
            vertex_a = vertex_dict[label_a]
            vertex_b = vertex_dict[label_b]
            edge = Edge({vertex_a, vertex_b}, props_ab)
            self.edge_set.add(edge)

    def get_vertex_set(self):
        return self.vertex_set

    def get_edge_set(self):
        return self.edge_set

    def get_neighbor_vertices(self, vertex, max_time):
        return [
            [
                [vertex, edge.get_other_vertex(vertex)],
                edge.get_property('time')
            ]
            for edge in vertex.get_edge_set()
            if edge.get_property('time') <= max_time
        ]

    def extend_route(self, route, max_time):
        route_list = self.get_neighbor_vertices(route[0][-1], max_time)
        if not route_list:
            return None, route

        extended_route_list = []
        for route_vertex_list, route_time in route_list:
            extend_route_time = route[1] + route_time
            extend_vertex = route_vertex_list[-1]
            if extend_route_time > max_time or extend_vertex in route[0]:
                continue
            extended_route_list.append(
                [route[0] + [route_vertex_list[-1]], route[1] + route_time]
            )
        return extended_route_list, route

    def get_all_routes(self, vertex, max_time):
        route_list = [[[vertex], 0]]
        complete_route_list = []

        while True:
            new_route_list = []
            for route in route_list:
                extended_route = self.extend_route(route, max_time)
                extended_route_list, original_route = extended_route
                if extended_route_list:
                    new_route_list.extend(extended_route_list)
                else:
                    complete_route_list.append(original_route)

            if not new_route_list:
                break
            route_list = new_route_list

        return complete_route_list

    def optimized_route_list(self, complete_route_list):
        longest_route_list = []
        longest_route_length = 0
        for route in complete_route_list:
            vertex_list, _ = route
            vertex_list_length = len(vertex_list)
            if vertex_list_length == longest_route_length:
                longest_route_list.append(route)
            if vertex_list_length > longest_route_length:
                longest_route_length = vertex_list_length
                longest_route_list = [route]

        if not longest_route_list:
            return None

        fastest_route_list = []
        fastest_route_time = None
        for route in longest_route_list:
            _, route_time = route
            if fastest_route_time is None:
                fastest_route_time = route_time
            if route_time == fastest_route_time:
                fastest_route_list.append(route)
            if route_time < fastest_route_time:
                fastest_route_time = route_time
                fastest_route_list = [route]

        return fastest_route_list

    def get_neighbor_vertices_notime(self, vertex):
        return [
            [
                vertex, edge.get_other_vertex(vertex)
            ]
            for edge in vertex.get_edge_set()
        ]

    def extend_route_notime(self, route):
        route_list = self.get_neighbor_vertices_notime(route[0][-1])
        if not route_list:
            return None, route

        extended_route_list = []
        for route_vertex_list in route_list:
            extend_vertex = route_vertex_list[-1]
            if extend_vertex in route[0]:
                continue
            extended_route_list.append(
                [route[0] + [route_vertex_list[-1]]]
            )
            break
        return extended_route_list, route

    def get_all_routes_notime(self, vertex):
        route_list = [[[vertex]]]
        complete_route_list = []

        while True:
            new_route_list = []
            for route in route_list:
                extended_route = self.extend_route_notime(route)
                extended_route_list, original_route = extended_route
                if extended_route_list:
                    new_route_list.extend(extended_route_list)
                else:
                    complete_route_list.append(original_route)

            if not new_route_list:
                break
            route_list = new_route_list

        return complete_route_list

    def get_longest_route_notime(self, vertex):
        complete_route_list = self.get_all_routes_notime(vertex)
        longest_route_list = []
        longest_route_length = 0
        for route in complete_route_list:
            vertex_list = route
            vertex_list_length = len(vertex_list)
            if vertex_list_length == longest_route_length:
                longest_route_list.append(route)
            if vertex_list_length > longest_route_length:
                longest_route_length = vertex_list_length
                longest_route_list = [route]

        if not longest_route_list:
            return None
        return longest_route_list

    def component_check(self):
        components_list = []
        remove_vertex_list = []
        vertex_set = self.get_vertex_set()
        remaining_vertex_list = vertex_set.difference(remove_vertex_list)
        remaining_edge_list = []

        while True:
            current_vertex = remaining_vertex_list.pop()
            longest_routes_list = self.get_longest_route_notime(current_vertex)
            remove_vertex_list.extend(longest_routes_list[0][0])
            components_list.extend([longest_routes_list[0][0]])
            if len(remove_vertex_list) == len(vertex_set):
                break

            remaining_vertex_list = vertex_set.difference(remove_vertex_list)
            edge_set = self.get_edge_set()
            print(edge_set)
            for edge in edge_set:
                vertex_a, vertex_b = edge
                if vertex_a or vertex_b in remaining_vertex_list:
                    continue
                remaining_edge_list.append(edge)

            self = Graph(remaining_vertex_list, remaining_edge_list)

        return components_list

    def greedy_algorithm(self, fastest_route_list, components_list, max_time):
        optimal_route_list = []
        while True:
            optimal_route_list.extend(fastest_route_list)
            if len(fastest_route_list[0][0]) == len(components_list[0]):
                return optimal_route_list, None
                break
            components_set = set(components_list[0])
            fastest_route_set = set(fastest_route_list[0][0])
            remaining_vertex_set = components_set.difference(fastest_route_set)
            remaining_vertex_list = []
            for vertex in remaining_vertex_set:
                label = vertex.get_label()
                for vertex in vertex_list:
                    if label == vertex[0]:
                        remaining_vertex_list.append(vertex)

            if len(remaining_vertex_set) == 1:
                optimal_route_list.extend(list(remaining_vertex_set))
                return optimal_route_list, None
                break
            label_list = []
            for vertex in remaining_vertex_list:
                label_list.append(vertex[0])
            remaining_edge_list = []
            for edge in edge_list:
                vertex_a, vertex_b, _ = edge
                if vertex_a in label_list\
                        and vertex_b in label_list:
                    remaining_edge_list.append(edge)

            self = Graph(remaining_vertex_list, remaining_edge_list)
            # test_vertex_list = self.get_vertex_set()
            # for vertex in test_vertex_list:
            #     complete_route_list = self.get_all_routes(vertex, max_time)
            #     fastest_route_list = self.optimized_route_list(
            #         complete_route_list
            #         )
            #     break

        return optimal_route_list, self

    def __str__(self):
        return 'vertex_list:\n%s\nedge_list:\n%s' % (
            '\n'.join([
                '%s' % vertex for vertex in self.vertex_set
            ]),
            '\n'.join([
                '%s' % edge for edge in self.edge_set
            ])
        )


if __name__ == "__main__":
    
    from Test_data import vertex_list, edge_list
    assert vertex_list and edge_list
    max_time = 60
    g = Graph(vertex_list, edge_list)

    for vertex in g.get_vertex_set():
        print(vertex.get_label())
        complete_route_list = g.get_all_routes(vertex, max_time)
        fastest_route_list = g.optimized_route_list(complete_route_list)
        for route_vertex_list, route_time in fastest_route_list:
            print(route_time, 'fastest_route_list: ', ' '.join([
                vertex.get_label() for vertex in route_vertex_list
            ]))
        components_list = g.component_check()
        for route_vertex_list in components_list:
            print('components_list: ', ' '.join([
                vertex.get_label() for vertex in route_vertex_list
            ]))
        while g is not None:
            greedy_result, new_g = g.greedy_algorithm(
                fastest_route_list,
                components_list,
                max_time)
            g = new_g
            for route in greedy_result:
                print('route: ', route)
        break

    # from Test_data import test_3_vertex_list, test_3_edge_list
    # assert test_3_vertex_list and test_3_edge_list
    # vertex_list = test_3_vertex_list
    # edge_list = test_3_edge_list
    # g = Graph(vertex_list, edge_list)
    # max_time = 50
    # for vertex in g.get_vertex_set():
    #     print(vertex.get_label())
    #     complete_route_list = g.get_all_routes(vertex, max_time)
    #     fastest_route_list = g.optimized_route_list(complete_route_list)
    #     for route_vertex_list, route_time in fastest_route_list:
    #         print(route_time, 'fastest_route_list: ', ' '.join([
    #             vertex.get_label() for vertex in route_vertex_list
    #         ]))
    #     components_list = g.component_check()
    #     for route_vertex_list in components_list:
    #         print('components_list: ', ' '.join([
    #             vertex.get_label() for vertex in route_vertex_list
    #         ]))
    #     greedy_result, new_g = g.greedy_algorithm(
    #         fastest_route_list,
    #         components_list,
    #         max_time)
    #     for route in greedy_result:
    #         print('route: ', route)
    #     break
