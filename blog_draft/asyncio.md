- [x] await sendall vs transport.write vs await reader.readline?
  实际上这些都不能保证将内容发送到了内核 buf
- [x] 怎样终止 readline?
  feed_eof
- [ ] 任务怎样主动来检测 eof?
  在 web_protocol 中，它没有主动检测 eof，而是在连接关闭的时候，
  把处理任务给 done 掉，给 reader feed eof。
  在 StreamReaderProtocol 中，对于 reader，它也是在连接关闭的时後 feed eof,
  对于 writer, 调用 write drain.
- [ ] reader 和 writer 的 paused 是用来干啥的？流控


写流程：调用 `transport.write` 方法将数据加到 transport 的 buffer 中，
并注册一个真正的 socket.send 任务，这个任务负责将 buffer 中的数据全部发送完。
如果 write 的数据大小超过自己设定的最大值，transport 会尝试将自己设置为 paused，
这时後，如果 await drain，则会等待。

1. 是不是每个 write 操作之后都应该 await drain 呐？

> This method is not subject to flow control.
> Calls to write() should be followed by drain().

2. aiohttp 是怎样处理 drain 和 write 的？
   在 write 后 drain 一下。

3. `loop.sock_sendall` 有没有调用 drain 方法呢？

`sock_sendall` 方法没有使用 StreamWriter，它也没有 buffer,
它直接往 socket 中写数据。相当于在操作系统层面来作 flow control。

引申出另外一个问题：为什么 Transport 要有个 buffer？

据 [njs blog][njs blog] 这篇文章说，transport writer 的 buffer 可能是个多余的设计。
另外，这个答案下的讨论也有值得阅读一下：https://stackoverflow.com/a/52616376/4302892

据个人考证：aiohttp 从来没有 disable watermarks 过，也就是它并没有 `set_write_buffer_limits(0)`。
另外，值得一提的是 asyncio `TCP_NODELAY` 是 True.



[njs blog]: https://vorpus.org/blog/some-thoughts-on-asynchronous-api-design-in-a-post-asyncawait-world/

4. socket 应该先关读，还是先关写？在 Linux 下，关写实际上并没有动作。
