## 题目
给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。

示例：

给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()

sumRange(0, 2) -> 1  
sumRange(2, 5) -> -1  
sumRange(0, 5) -> -3  
说明:

你可以假设数组不可变。
会多次调用 sumRange 方法。

## 解题思路
用python3的sum方法，感觉不太对，纯粹是练习类的使用了  
更新：因为重复调用，所以可以保存之前的结果。用f(n)表示a(1)+...+a(n)的和，然后a(i)+...+a(j)=f(j)-f(i)
## 成绩
时间>13.22%