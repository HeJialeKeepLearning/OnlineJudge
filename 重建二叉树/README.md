## 题目
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
## 解题思路
递归，除非输入的2个序列均为空，否则左子树的前序遍历为根节点后x个字符，x是根节点在中序遍历中根节点前面的节点数，右子树类似
## 总结
递归中对于终止条件的判断非常重要