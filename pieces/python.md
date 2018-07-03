### 字符串
#### 字符串 format 如何得到这种 {value} 形式的字符串

```python
'{{{hosts}}}'.format(hosts=','.join(['hello', 'world']))
```

### python 描述符

#### A.b, a.b 分别是如何工作的？

```python

class A(object):
    @property
    def h(self):
        return 1

a = A()
```

[参考链接](https://docs.python.org/3/howto/descriptor.html#invoking-descriptors)

> For objects, the machinery is in `object.__getattribute__()` which transforms b.x
into `type(b).__dict__['x'].__get__(b, type(b))`. The implementation works through
a precedence chain that gives data descriptors priority over instance variables,
instance variables priority over non-data descriptors, and assigns lowest priority
to `__getattr__()` if provided. The full C implementation can be found in
PyObject_GenericGetAttr() in Objects/object.c.

> For classes, the machinery is in `type.__getattribute__()` which transforms B.x
into `B.__dict__['x'].__get__(None, B)`. In pure Python, it looks like:
