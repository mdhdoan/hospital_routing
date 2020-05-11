#
# This class defines an edge of any graph
# An edge includes:
#   - a pair of vertices (start and end)
#   - a dictionary of properties (each item has a pair of name and value)
#


class Edge:
    def __init__(self, vertex_set, props):
        self.vertex_set = vertex_set
        for vertex in self.vertex_set:
            vertex.add_edge(self)
        self.props = props

    def get_vertex_set(self):
        return self.vertex_set

    def get_other_vertex(self, vertex):
        return self.vertex_set.difference({vertex}).pop()

    def get_props(self):
        return self.props

    def get_property(self, name):
        if name in self.props:
            return self.props[name]
        return None

    def set_property(self, name, value):
        self.props[name] = value

    def __str__(self):
        return 'endpoints:\n%s\nproperties:\n%s\n' % (
            '\n'.join([
                '%s' % vertex for vertex in self.vertex_set
            ]),
            '\n'.join([
                '\t%s: %s' % (name, self.props[name])
                for name in sorted(self.props.keys())
            ])
        )

    def __hash__(self):
        return hash('@@@'.join(sorted([
            vertex.get_label()
            for vertex in self.vertex_set
        ])))


if __name__ == "__main__":
    from Test_data import edge_list, vertex_list
    from Vertex import Vertex
    assert edge_list and len(edge_list) > 0

    label_a, props_a = vertex_list[0]
    vertex_a = Vertex(label_a, props_a)
    label_b, props_b = vertex_list[1]
    vertex_b = Vertex(label_b, props_b)

    vertex_set = {vertex_a, vertex_b}
    _, _, props_ab = edge_list[0]
    edge_ab = Edge(vertex_set, props_ab)
    assert edge_ab.get_other_vertex(vertex_a) == vertex_b
    assert edge_ab.get_other_vertex(vertex_b) == vertex_a
    assert edge_ab.get_property("time")
    edge_ab.set_property("cost", 90)
    assert edge_ab.get_property("cost") == 90
    print(edge_ab)

    label_c, props_c = vertex_list[2]
    vertex_c = Vertex(label_c, props_c)
    vertex_set2 = {vertex_b, vertex_c}
    _, _, props_bc = edge_list[1]
    edge_bc = Edge(vertex_set2, props_bc)
    print(edge_bc)

    edge_set = set()
    edge_set.add(edge_ab)
    assert len(edge_set) == 1
    print(edge_set)
    edge_set.add(edge_bc)
    assert len(edge_set) == 2
    print(edge_set)
