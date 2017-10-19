# python 对象序列化的库比较

目前已知的一些：

1. django-restframework 的 serializer
2. schematics
3. marshmallow

看功能，schematics 和 marshmallow 两者差不了多少，要使用才知道...比如看接口用起来怎样：
语义？重复？代码好不好写？感觉需要自己对这个东西有一定经验才能评判

- [ ] 论如何评价一个库的好与坏？
  - [x] 是不是专心做一件事情，这件事情做得专不专业？

### schematics: Python Data Structures for Humans™.

> Schematics is a Python library to combine types into structures, validate them, and transform the shapes of your data based on simple descriptions.

- Design and document specific data structures
- Convert structures to and from different formats such as JSON or MsgPack
- Validate API inputs
- Remove fields based on access rights of some data’s recipient
- Define message formats for communications protocols, like an RPC
- Custom persistence layers

翻译过来：带类型的数据结构，有 validation 功能，可以对数据进行格式转换。

### marshmallow: simplified object serialization

> marshmallow is an ORM/ODM/framework-agnostic library for converting complex datatypes, such as objects, to and from native Python datatypes.

- Validate input data.
- Deserialize input data to app-level objects.
- Serialize app-level objects to primitive Python types. The serialized objects can then be rendered to standard formats such as JSON for use in an HTTP API.
