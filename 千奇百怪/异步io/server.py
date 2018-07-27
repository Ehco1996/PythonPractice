from aiohttp import web

mylogger = logging.getLogger('aiohttp.access')


async def handle(request):
    name = request.match_info.get('name', 'Anonymous')
    text = "hello," + name
    return web.Response(text=text)

app = web.Application()
app.add_routes([
    web.get('/', handle),
    web.get('/{name}/', handle),
])


web.run_app(app, access_log=mylogger)
