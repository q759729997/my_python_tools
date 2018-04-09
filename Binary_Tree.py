'''
二叉树的遍历
'''
class TreeNode(object):
    def __init__ (self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


# 先序遍历
# 访问结点，遍历左子树，如果左子树为空，则遍历右子树，
# 如果右子树为空，则向上走到一个可以向右走的结点，继续该过程
def preorder(root):
    if root:
        print(root.data)
        preorder(root.left)
        preorder(root.right)
# 中序遍历
# 从根开始，一直走向左下方，直到无结点可以走则停下，访问该节点
# 然后走向右下方到结点，继续走向左下方：如果结点无右孩子，则向上走回父亲结点
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)
# 后序遍历
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data)

node11 = TreeNode('-')
node21 = TreeNode('+')
node22 = TreeNode('➗')
node11.left = node21
node11.right = node22
node31 = TreeNode('a')
node32 = TreeNode('*')
node21.left = node31
node21.right = node32
node33 = TreeNode('e')
node34 = TreeNode('f')
node22.left = node33
node22.right = node34
node41 = TreeNode('b')
node42 = TreeNode('-')
node32.left = node41
node32.right = node42
node51 = TreeNode('c')
node52 = TreeNode('d')
node42.left = node51
node42.right = node52

print('先序遍历：根=》左=》右')
preorder(node11)
print('中序遍历：左=》根=》右')
inorder(node11)
print('后序遍历：左=》右=》根')
postorder(node11)