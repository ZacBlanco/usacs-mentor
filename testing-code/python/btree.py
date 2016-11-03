class BTree:

    def __init__(self):
        self.root = None

    def insert(self, node):
        '''Insert a BNode into the binary tree. Cannot handle duplicate keys

        Args:
            node (BNode): A binary tree node to insert into the tree.

        Returns:
            The binary tree node, `None` if tree insertion failed
        '''
        if self.root is None:
            self.root = bnode
            return self.root

        curr = self.root
        inserted = False
        while (not inserted):
            if curr.key() < node.key():
                if curr.left is None:
                    curr.left = node
                    inserted == True
                else:
                    curr = curr.left
            elif curr.key() > node.key():
                if curr.right is None:
                    curr.right = node
                    inserted == True
                else:
                    curr = curr.right
            else:
                return None
                break
        
        return node
            
        

    def get(self, key):
        '''Gets the kv pair for the given key within the binary tree

        Args:
            key (int): The int value for the binary tree node.
        '''
        pass






class BNode:

    def __init__(self, key, value, left=None, right=None):
        self.kv = (key, value)
        self.left = left
        self.right = right

    def key(self):
        return self.kv[0]


    def val(self):
        return self.kv[1]
