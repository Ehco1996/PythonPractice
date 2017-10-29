'''
RPC server
RPC是指远程过程调用
client 
    server_client server_client.attack(xxx)
---------->
server
    logic.attack(xxx)

JSONRPC
'''

'''
需要实现什么

1 tcp server tcp client
    tcp server bind accept recv parse call
    tcp client connect send data

2 function name args kwargs
    json
    {
        'function_name':name,
        'function_agrs':args,
        'function_kwatgs':kwargs,
    }

3 client
    假设我们掉了这样一个接口
    c.foo(1,2,3)
    就会发送一个这样的json包
    send
    {
        'function_name':'foo',
        'function_agrs':(1,2,3),
        'function_kwatgs':{},
    }

    __getattr__ pack
    封包发出

4 server
    1 recv to json
    {
        'function_name':'foo',
        'function_agrs':(1,2,3),
        'function_kwatgs':{},
    }

    getattr(self,'foo')
    getattr(self,'foo')(*args,**kwargs)

'''
