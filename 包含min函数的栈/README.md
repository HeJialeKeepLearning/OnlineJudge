# 题目
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
# 解题思路
push的时候就记录进入的元素，记录最小值。但是pop的时候，需要更新最小元素为次小元素，这里用了python的min方法，实际上是不对的，应该保持时间复杂度为o(1)。看别人的解法是，保存一个最小元素栈，如果当前入栈的元素比最小元素小，则压入最小元素栈，这样最小元素栈里面的元素就是次小元素了。