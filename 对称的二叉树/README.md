# 题目
请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
# 解题思路
因为镜像二叉树是交换左右子树的节点，所以如果和镜像相同，岂不是左右子树所有节点值都相同了？

不是的，比如：

        8
       / \
      6   6
     / \ / \
    7  5 5  7

层次遍历二叉树，对称的二叉树每层的结果应该是对称的值。
# 注意点
特别注意这样的树：

        5
       / \
      5   5
       \   \
        5   5
这个树应该是不对称的，但是按照上面的思路，会判断为堆成。因为第三层的队列就是5，5，丢失了左右子树的信息。解决的方法是，给二叉树插入空子树（值为#）。注意如果访问到空子树了，则不会给空子树继续插入子节点了。

看别人的思路，改进版层次遍历，每次pop出2个节点，再依次放入左子树的左子树、右子树的右子树、左子树的右子树、右子树的左子树，每次比较取出的2个是否值相同即可。