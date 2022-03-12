#Find height of a given tree
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
 
def height(root):
 
    # Check if the binary tree is empty
    if root is None:
        # If TRUE return 0
        return 0 
    # Recursively call height of each node
    left = height(root.left)
    right = height(root.right)
 
    # Return max(leftHeight, rightHeight) at each iteration
    return max(left, rightn) + 1
 
# Test the algorithm
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
 
print("Height of the binary tree is: " + str(height(root)))
