import asyncio


async def my_coroutine():
    print('简单的循环')


def main():
    # 定义一个事件循环
    loop = asyncio.get_event_loop()

    # 让事件循环不断的运行
    # 直到所有的任务全部都执行完毕之后
    loop.run_until_complete(my_coroutine())

    # 关闭事件循环
    loop.close()


if __name__ == '__main__':
    main()
