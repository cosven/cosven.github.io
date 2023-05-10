* 读《The Log-Structured Merge-Tree》

** 问题

- [X] LSM-tree 的基本特点与优势
- [X] 摘要里面多次提到的 index 是指什么东西？可能特指“磁盘数据索引”。
- [X] LSM-tree 的结构
  - [X] multi-page block 没看太懂是个啥：朴素理解可能就可以了。
- [ ] 这个 LSM-tree 和 RocksDB 里面的 LSM-tree 真的是一个东西么？？？

- [ ] 可以看到，这种结构是针对机械磁盘（有磁盘臂）来设计的，对 ssd 能充分利用么？
- [ ] LSM-tree 读性能为什么被牺牲了？就因为内存结构么？

** 摘要

没看懂为什么要翻倍
> Unfortunately, standard disk-based index structures such as the B-tree will effectively double the I/O cost of the
transaction to maintain an index such as this in real time, increasing the total system cost up to
fifty percent.


LSM-tree 的中心思想

The Log-Structured Merge-tree (LSM-tree) is a disk-based data structure designed to provide
low-cost indexing for a file experiencing a high rate of record inserts (and deletes) over an
extended period.

特点1：低成本维护实时索引
The LSM-tree uses an algorithm that defers and batches index changes,
cascading the changes from a memory-based component through one or more disk components in an
efficient manner reminiscent of merge sort.

特点2：减少磁盘在xx场景的开销，相比于
The algorithm has greatly reduced disk arm
movements compared to a traditional access methods such as B-trees, and will improve costperformance in domains where disk arm costs for inserts with traditional access methods
overwhelm storage media costs.

特点3：适合写多读少（在介绍部分又强调了一次）
However, indexed finds requiring immediate response will lose I/O efficiency in some cases, so the LSM-tree is most useful in applications where index inserts are
more common than finds that retrieve the entries.

** 介绍

介绍了背景：需求（负载）的变化，导致了对 “日志类数据结构” 新的需求。
> The need to answer queries about a vast number of past activity logs implies
that indexed log access will become more and more important.

5 分钟访问一次就应该缓存起来 -> 60s 一次则应该扩大内存，这样来降低成本？
通过 TPC-A 的负载，来分析描述磁盘 IO 和系统性能的关系，想说明索引是有必要的。

讲了 B-tree 在实现索引时，性能不好在哪里，说 LSM-tree 可以更好的处理。
但对负载有要求，就是它的查询频率要在一定范围内。不是一点点，也不能太多。

总的来说：这一节就是讲索引有用，而 B-tree 实现索引还不够好，LSM-tree 更好。

** The Two Component LSM-tree Algorithm

讲了一行数据的写入流程：先写到内存里，内存超限时或时间较长，落到磁盘中，
落盘过程叫做 rolling merge。rolling merge 的步骤：暂时跳过，比较细节。
一个重要信息就是它不会覆盖，二是追加的写入。

第二章介绍了 LSM-Tree 的基本结构和基本操作，以及增删改查的基本操作。
rolling merge 没看太懂，但基本意思能理解。

** LSM-tree 的性价比分析
** Concurrency and Recovery in the LSM-tree
** Cost-Performance Comparisons with Other Access Methods
** Conclusions and Suggested Extensions
** 其它

disk arm -> 这个命名有点意思

* 读《LSM-based storage techniques: a survey》

读这一篇的目的主要是看看 memtable, sstable 这些概念是从哪里引入的。
