import code_116_populating_next_right_pointers_in_each_node as c

def test_example_1():
    s = c.Solution()
    root = c.Node(1, c.Node(2, c.Node(4), c.Node(5)), c.Node(3, c.Node(6), c.Node(7)))

    n7 = c.Node(7)
    n6 = c.Node(6,None,None,n7)
    n5 = c.Node(5,None,None,n6)
    n4 = c.Node(4,None,None,n5)
    n3 = c.Node(3, n6, n7)
    n2 = c.Node(2, n4, n5, n3)
    n1 = c.Node(1, n2, n3)
    
    assert s.connect(root) == n1