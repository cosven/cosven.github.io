#  结构之法 - 字符串及链表

## 字符串

### 基础
- strstr: 平均 O(N)，最坏 O(NM)。
- strlen: O(n)。 gcc 里面有个优化的实现，看看挺好玩的。
- strcmp: strstr 会依赖 strcmp。

### 题目

1. 字符串移位包含
2. 编辑距离
3. 设计一个队列，能方便的取到最大值

### 疑问

1. 队列的底层数据结构是啥？

   How about stack?

   用两个 stack 实现一个 queue ... 不走寻常路

### 感悟

递归和动态规划有很大相似之处：

- 动态规划：大问题的计算依赖小问题，小问题经常被多次重复依赖
- 递归：大问题的计算转换为小问题
