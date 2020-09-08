# Extra Utility
class Tree:
    """Abstract base class for representing a tree structure."""

    #---------------------------nested Position class----------------------------
    class Position:
        """An abstraction representing the location of a single element."""

        def element(self):
            """Return the element stored at this Position."""
            raise NotImplementedError("Must be implemented by subclass")

        def __eq__(self,other):
            """Return True if other Position represents the same location."""
            raise NotImplementedError("Must be implemented by subclass")

        def __ne__(self,other):
            """Return True if other does not represents the same location."""
            return not(self == other)           # opposite of __eq__

    #-----------abstract methods that contrete subclass bust support-----------
    def root(self):
        """Return Position representing the tree's root (or None if empty)."""
        raise NotImplementedError("Must be implemented by subclass")

    def parent(self,p):
        """Return Position representing p's parent (or None if p is root)."""
        raise NotImplementedError("Must be implemented by subclass")

    def num_children(self,p):
        """Return the number of children the Position p has."""
        raise NotImplementedError("Must be implemented by subclass")

    def children(self,p):
        """Generate an iteration of Positions representing p's children."""
        raise NotImplementedError("Must be implemented by subclass")

    def __len__(self):
        """Return the total number of elements in the tree."""
        raise NotImplementedError("Must be implemented by subclass")

    #--------------concrete methods implemented in this class------------------
    def is_root(self,p):
        """Return True if Position p representing the root of  the tree."""
        return (self.root() == p)

    def is_leaf(self,p):
        "Return True if Position p does not have any children"""
        return (self.num_children(p) == 0)

    def is_empty(self):
        """Return True id the tree is empty."""
        return len(self) == 0

    #-----------------------------new methods----------------------------------
    def depth(self,p):
        """Return the number of levels separating Position p from the root."""
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def _height1(self):             # works, but O(n**2) worst-case
        """Return the height of the tree."""
        return max(self.depth(p) for p in self.positions() is self.is_leaf(p))

    def _height2(self,p):           # time is linear in size of sub-tree
        """Return the height of the subtree rooted at Position p."""
        if self.is_leaf(p):
            return 0
        else:
            return max(self._height2(c) for c in self.children(p))

    def height(self,p=None):
        """Return the height of the subtree rooted at Position p.

        If p is None, return the height of the entire tree.
        """
        if p is None:
            p = self.root()
        return self._height2(p)         # start _height2 recursion

class BinaryTree(Tree):
    """Abstract base class representing a binary tree structure."""

    #-------------------------addtional abstract mathods---------------------------
    def left(self,p):
        """Return the Position representing p's left child.

        Return None if p does note have a left child.
        """
        raise NotImplementedError("Must be implemented by subclass.")

    def right(self,p):
        """Return the Position representing p's right child.

        Return None if p does note have a right child.
        """
        raise NotImplementedError("Must be implemented by subclass.")

    #---------------concrete methods implemented in this class-------------------
    def sibling(self,p):
        """Return a Position representing p's sibling (or None if no sibling)."""
        parent = self.parent(p)
        if parent is None:              # p must be the root
            return None                 # root has no sibling
        else:
            if p == self.left(parent):
                return self.right(parent)   # possibly None
            else:
                return self.left(parent)    # possibly None

    def children(self,p):
        """Generate an iteration of Position representing p's children."""
        if self.left(p) is not None:
            yield self.left(p)
        if self.rightt(p) is not None:
            yield self.right(p)
        
    


# Main Code

class TreeTraversals(BinaryTree):
    def inorder(self):
        """Generate a inorder iteration of positions in the tree."""
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p

    def  _subtree_inorder(self,p):
        """Generate an inorder iteration of positions in subtree rooted at p."""
        if self.left(p) is not None:        # if left child exists, traverse its subtree.
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p                             # visit p between its subtrees
        if self.right(p) is not None:       # if right child exists, traverse its subtree.
            for other in self._subtree_inorder(self.right(p)):
                yield other
