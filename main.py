
from aiohttp import web
import aiohttp_jinja2
import jinja2
import os

app = web.Application()

# Setup Jinja2
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('templates'))

# Routes
@aiohttp_jinja2.template('index.html')
async def home(request):
    return {}

# Static files
app.router.add_static('/static/', path='static', name='static')
app.router.add_get('/', home)

# Run app
if __name__ == '__main__':
    web.run_app(app, host='0.0.0.0', port=8080)
