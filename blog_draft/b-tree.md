# 读《The Ubiquitous B-Tree》

1970 年的论文《ORGANIZATION AND MAINTENANCE OF LARGE ORDERED INDICES》
1979 年的论文《The Ubiquitous B-Tree》

## 简介

先介绍背景：
访问组织好的文件的方式通常有两种 **Sequential and Random**。
然后说，对于随即访问，有 index 访问起来会更快，这里用文件夹和文件夹上的
A-Z 来描述索引，生动形象。（其实比作字典索引，也挺形象的。）

这篇论文的核心内容：
比较了 B-tree 的一些变种，尤其是 B+-tree，展示了为什么它变得如此流行。
论文还调查了 B-trees 相关的一些论文。另外，它还讨论了一种基于 B-tree
的通用文件访问方法。

> This paper, intended for
computer professionals who have heard of
B-trees and want some explanation or di-
rection for further reading, compares sev-
eral variations of the B-tree, especially the
B+-tree, showing why it has become popu-
lar. It surveys the literature on B-trees in-
cluding recent papers not mentioned in
textbooks. In addition, it discusses a general
purpose file access method based on the B-
tree.

## The Basic B-Tree

B-tree 的基本性质，order 是变量。插入删除时都要保证这个性质。
> In general, each node in a B-tree of order
d contains at most 2d keys and 2d + 1
pointers, as shown in Figure 4. Actually,
the number of keys may vary from node to
node, but each must have at least d keys
and d + 1 pointers. As a result, each node
is at least 1/~ full

B-tree 的平衡（balancing）：

B-tree 的优雅之处在于插入和删除都能保持树的平衡。
任何一个查找操作最多访问 1+logdN 个节点，N 是节点总数，d 是 order。
如何保持平衡是这里着重介绍一个点。

插入遇到节点 `full` 的话，需要 `split`。最坏的情况，是一直递归到 root，
root 进行 split，这样树的高度会加一。删除的时候，如果是删除一个非叶子节点，
则需要补一个相邻的节点进来。通常是找比它大的那个相邻节点。如果遇到
`underflow` 的话，也要重新平衡，就从邻居叶子借一个过来。
也可以多借几个来让两个邻居更均衡。如果加起来还不够 2d，则可以 concatenation。

查询，插入，删除的最坏复杂度都基本是logdN。插入和删除的细节看 wikipedia
更好懂一点，2333。

## B-tree 变种

插入和删除的时候，split 和 contatenation 都可以延迟，通过和邻居平衡。
next 查询

B*-trees 是一种节点必须有 2/3 满的树。单节点满的时候，从旁边的节点挪一挪。
两个节点满的时候，正好分为 3 个 2/3 的树。说这种方法，空间使用率最少有 66%。

B+-trees，只有叶子节点有 key，上层只有 index。
