title: python小问题收集
date: 2015-09-17 10:37:48
tags: [python]
---


**一个比较标准的python装饰器函数**

```
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper
```

**一个函数return多种结果，下个函数一个一个判断，是否有更加优雅的解决方案？**

**\A\Z 和 ^$的区别**

如果用regex来做验证的话，选择`\A\Z`

[stackoverflow](http://stackoverflow.com/questions/577653/difference-between-a-z-and-in-ruby-regular-expressions)
