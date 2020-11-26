# 写一个简单的解释器 - 语法分析

## 上下文无关文法

> 上下文无关文法（英语：context-free grammar，缩写为CFG），在计算机科学中，
若一个形式文法 G = (N, Σ, P, S) 的产生式规则都取如下的形式：V -> w，则谓之。
其中 V∈N ，w∈(N∪Σ)* 。上下文无关文法取名为“上下文无关”的原因就是因为字符 V
总可以被字符串 w 自由替换，而无需考虑字符 V 出现的上下文。

### 什么是“文法”？

## LL(1) 文法

## 具象语法树与抽象语法树

主要参考资料：https://ruslanspivak.com/lsbasi-part7/

> So, what is a parse tree? A parse-tree (sometimes called a concrete syntax tree)
> is a tree that represents the syntactic structure of a language construct
> according to our grammar definition.

> An abstract syntax tree (AST) is a tree that represents the abstract syntactic
> structure of a language construct where each interior node and the root node
> represents an operator, and the children of the node represent the operands of that operator

![2 * 7 + 3](https://ruslanspivak.com/lsbasi-part7/lsbasi_part7_ast_01.png)

我一直都觉得 CST(concret syntax tree) 比较好理解，

### “函数”的抽象语法树长什么样？
