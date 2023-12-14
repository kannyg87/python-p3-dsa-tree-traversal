class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, id):
        return self._dfs_search(self.root, id)

    def _dfs_search(self, node, id):
        if node is None:
            return None
        if node['id'] == id:
            return node
        for child in node['children']:
            found = self._dfs_search(child, id)
            if found is not None:
                return found
        return None
