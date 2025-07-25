import os
from aiohttp import web
from aiohttp_jinja2 import setup as jinja_setup, template
import jinja2

routes = web.RouteTableDef()

@routes.get('/')
@template('index.html')
async def index(request):
    return {}

@routes.get('/privacy')
@template('privacy.html')
async def privacy(request):
    return {}

@routes.get('/terms')
@template('terms.html')
async def terms(request):
    return {}

@routes.get('/health')
async def health(request):
    return web.json_response({'status': 'ok'})

app = web.Application()
jinja_setup(app, loader=jinja2.FileSystemLoader('templates'))
app.add_routes(routes)
app.router.add_static('/static/', path='static', name='static')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    web.run_app(app, port=port)
