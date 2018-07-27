import asyncio


# 创建一个需要未来对象作为参数的func
async def my_coroutine(future):
    # 模拟一些耗时操作
    await asyncio.sleep(1)
    future.set_result('我的协程任务完成了')


async def main():
    # 创建一个未来对象
    future = asyncio.Future()

    # 通过ensure_future方法将未来对象传入
    # 我们需要执行的协程之中
    await asyncio.ensure_future(my_coroutine(future))

    # 打印出结果
    print(future.result())

loop = asyncio.get_event_loop()

try:
    loop.run_until_complete(main())
finally:
    loop.close()
