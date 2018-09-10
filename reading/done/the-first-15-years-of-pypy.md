# 读《The First 15 Years of PyPy》

读后感：自己读了文章的前面一部分。前面这部分主要讲了项目是怎样发起的、项目前期遇到了哪些问题、
怎样解决这些问题、项目前期需要注意哪些事情。

PyPy is a Python interpreter written in Python.

#### 项目是怎样开始的？
邮件列表，一群 Python 爱好者自发组织。

#### 一开始：实现一个解释器
各地（各国）有一个带头人，组织进行开发，然后写了解释器，可以进行一些数学计算。

#### 团队早期是怎样进行项目管理的？

1. 比较全面的单元测试
2. 持续集成（在 2002 年）
3. 结对编程，让大家对代码都有一定的了解
4. 经常重构，保证代码质量
5. 功能上和 CPython 保持一致

#### 设立基金

EU Funding

没太仔细看，大概说了有一个组织支持它们，给他们投资，但是他们需要实现组织的一些要求，
比如实现一些特性。而这些特性在后期，有很多都被废除了。

这一步，可以说是**有利有弊**。

#### Bootstraping PyPy
（没有看太懂，大概是说 PyPy 实现了一个设计实现了基础结构）
实现了 Python 虚拟机？可以将 Python 代码转换为 C？还涉及到 RPython 啥的

#### RPython 模块化问题
RPython 在设计的时候没有考虑模块化的问题。

1. 一个 RPython 程序不方便拆分成小模块
2. 编译时候，需要整体变异？

#### Meta-JIT

在 bootstrapping VM 之后，就开始优化解释器等

#### JIT Generator

#### Promote
Promote is basically a way to easily introduce runtime feedback into the JIT produced by the JIT generator.

#### Virtuals

应该也是某种优化方法

#### xxx
后面的东西看不太懂了，也不太想继续看了。
