# futures

## PEP-3148 -- futures - execute computations asynchronously

### Motivation

1. parallelizing simple operations requires a lot of work
2. difficult to design an application with a global process/thread
limit when each component invents its own parallel execution strategy.

### Specification
#### Naming
解释为什么把 futures 这个包放在 concurrent 下

#### Interface
主要两个类：`Executor` and `Future`。

An Executor receives asynchronous work requests (in terms of a callable and its arguments)
and returns a Future to represent the execution of that work request.

```python
import abc


class Executor(object):

    @abc.abstractmethod
    def submit(self, fn, *args, **kwargs):
        pass

    def map(self, func, timeout=None):
        pass

    def shutdown(wait=True):
        """
        Signal the executor that it should free any resources
        that it is using when the currently pending futures
        are done executing.
        """
        pass

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, exc_tb):
        pass
```

**`ProcessPoolExecutor`**

- The callable objects and arguments passed to ProcessPoolExecutor.submit
must be pickleable.

- Calling Executor or Future methods from within a callable submitted to
a ProcessPoolExecutor will result in deadlock.

**`ThreadPoolExecutor`**

- Deadlock can occur when the callable associated with a Future waits on
the results of another Future.

**`Future`**

```python
class Future(object):
    def cancel(self):
        pass

    def cancelled(self):
        pass

    def running(self):
        pass

    def done(self):
        pass

    def result(timeout=None):
        raise TimeoutError
        raise CancelledError
        pass

    def exception(timeout=None):
        pass

    def add_done_callback(self, fn):
        pass

    def _set_running_or_notify_cancel(self):
        # called by executor
        pass

    def _set_result(self, result):
        pass

    def _set_exception(self, exception):
        pass

done, not_done = wait(futures,
    timeout=None,
    return_when=ALL_COMPLETED/FIRST_EXCEPTION/FIRST_COMPLETED)

as_completed(futures, timeout=None)
```

### Rationale
这东西是参考 java.util.concurrent 设计的，2333。

Future 设计之初本来有个 `remove_done_callback` 方法，不过没有找到
合适的使用场景，于是就被废弃了。
