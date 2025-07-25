from aiohttp import web

routes = web.RouteTableDef()

@routes.get('/')
async def index(request):
    return web.FileResponse('templates/index.html')

@routes.get('/{filename}')
async def static_files(request):
    filename = request.match_info['filename']
    return web.FileResponse(f'templates/{filename}')

app = web.Application()
app.add_routes(routes)

if __name__ == '__main__':
    web.run_app(app, host='0.0.0.0', port=8080)
