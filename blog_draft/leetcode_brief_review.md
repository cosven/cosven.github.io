# 刷 leetcode 简单的记录

- [x] 尽量少记录内心活动..
- [x] 简要概括

### 034 - search for a range

####  问题简要描述

> Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.
>
> Your algorithm's runtime complexity must be in the order of *O*(log *n*).
>
> If the target is not found in the array, return `[-1, -1]`.
>
> For example,
> Given `[5, 7, 7, 8, 8, 10]` and target value 8,
> return `[3, 4]`.
>
>  [问题链接](https://leetcode.com/problems/search-for-a-range/)

1. 它要求复杂度 O(log n)

#### 思维过程

1. 哈希不行：O(n)
2. 二分法看起来可以

#### 解法

1. 递归找起点和终点 [python 代码实现](https://github.com/cosven/pat_play/blob/2f682e7c8415ebd051bae08513031750655247c9/leetcode/034.py)
2. 通过 A~n~ - A~n-1~ 来找起点和终点 （未尝试）


### 009 Palindrome Number

#### 问题简要描述

>  Determine whether an integer is a palindrome. Do this without extra space.

1. 要求不用额外空间

#### 思维过程

#### 解法

考虑各种细节

1. int 长度

   int	2 or 4 bytes	-32,768 to 32,767 or -2,147,483,648 to 2,147,483,647.

2. 负数