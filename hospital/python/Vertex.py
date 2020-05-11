#
# This class defines a vertex of any graph
# A vertex includes:
#   - a label
#   - a dictionary of properties (each item has a pair of name and value)
#


class Vertex:
    def __init__(self, label, props):
        # props is a dictionary
        self.label = label
        self.props = props
        self.edge_set = set()

    def get_label(self):
        return self.label

    def get_props(self):
        return self.props

    def get_property(self, name):
        if name in self.props:
            return self.props[name]
        return None

    def set_propety(self, name, value):
        self.props[name] = value

    def get_edge_set(self):
        return self.edge_set

    def add_edge(self, edge):
        self.edge_set.add(edge)

    def __str__(self):
        return '%s\n%s' % (
            self.label,
            '\n'.join([
                '\t%s: %s' % (name, self.props[name])
                for name in sorted(self.props.keys())
            ])
        )

    def __hash__(self):
        return hash(self.label)


if __name__ == "__main__":
    from Test_data import vertex_list
    assert vertex_list and len(vertex_list) > 1

    label_a, props_a = vertex_list[0]
    vertex_a = Vertex(label_a, props_a)
    assert vertex_a.get_label() == label_a
    print("Use __str__ function:\n%s\n" % vertex_a)
    print('Use member functions:\n\tlabel: \
            %s\n\tprops: %s\n\tweight_property: %s\n' % (
        vertex_a.get_label(),
        vertex_a.get_props(),
        vertex_a.get_property("weight"))
    )
    vertex_a.set_propety("load", 90)
    assert vertex_a.get_property("load") == 90
    print("Use set_propety function:\n%s\n" % vertex_a)

    label_b, props_b = vertex_list[1]
    vertex_b = Vertex(label_b, props_b)
    # print('vertex_a %s vertex_b'
    # % ('is equal to' if vertex_a == vertex_b else 'is NOT equal to'))

    vertex_set = set()
    vertex_set.add(vertex_a)
    print(vertex_set)
    assert vertex_set and len(vertex_set) == 1

    vertex_set.add(vertex_b)
    print(len(vertex_set))
    assert len(vertex_set) == 2

    vertex_set.remove(vertex_b)
    print(len(vertex_set))
    assert len(vertex_set) == 1

    vertex_set.remove(vertex_a)
    print(len(vertex_set))
    assert len(vertex_set) == 0
