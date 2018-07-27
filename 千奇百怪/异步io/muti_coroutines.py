import time
import random
import asyncio


# 创建一个需要未来对象作为参数的func
async def my_coroutine(id):
    process_time = random.randint(1, 5)
    await asyncio.sleep(process_time)
    print('id：{} 执行成功 耗时：{}'.format(id, process_time))


async def main():

    tasks = []
    for i in range(10):
        tasks.append(asyncio.ensure_future(my_coroutine(i)))

    await asyncio.gather(*tasks)

t1 = time.time()
loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(main())
finally:
    loop.close()

print('total time :{}'.format(time.time()-t1))
