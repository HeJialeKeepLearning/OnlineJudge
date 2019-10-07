# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        ret_str = str(root.val)
        queue = [root]
        right = root
        while queue:
            p = queue.pop(0)
            if p.val != '#':
                if not p.left:
                    p.left = TreeNode('#')
                if not p.right:
                    p.right = TreeNode('#')
                queue.append(p.left)
                queue.append(p.right)
            if p == right:
                if not queue:
                    break
                right = queue[-1]
                all_none_flag = True
                cur_level_str = ''
                for node in queue:
                    cur_level_str += (',' + str(node.val))
                    if node.val != '#':
                        all_none_flag = False
                if not all_none_flag:
                    ret_str += cur_level_str
        return ret_str

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return
        parts = data.split(',')
        head = TreeNode(parts[0])
        queue = [head]
        parts = parts[1:]
        left, right = 0, 1
        while right < len(parts):
            p = queue.pop(0)
            if parts[left] != '#':
                p.left = TreeNode(parts[left])
                queue.append(p.left)
            if parts[right] != '#':
                p.right = TreeNode(parts[right])
                queue.append(p.right)
            left += 2
            right += 2
        return head

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
