from aiohttp import web
import aiohttp_jinja2
import jinja2
import os

# Initialize the app
app = web.Application()

# Setup Jinja2 templates
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('templates'))

# Routes
@aiohttp_jinja2.template('index.html')
async def index(request):
    return {}

@aiohttp_jinja2.template('privacy.html')
async def index(request):
    return {}

@aiohttp_jinja2.template('shipping.html')
async def index(request):
    return {}
    
@aiohttp_jinja2.template('terms.html')
async def terms(request):
    return {}

@aiohttp_jinja2.template('contact.html')
async def contact(request):
    return {}

@aiohttp_jinja2.template('refund.html')
async def refund(request):
    return {}

# Add routes
app.router.add_get('/', index)
app.router.add_get('/terms', terms)
app.router.add_get('/contact', contact)
app.router.add_get('/refund', refund)

# Serve static files (CSS, images, etc.)
app.router.add_static('/static/', path='static', name='static')

# Run the server
if __name__ == '__main__':
    web.run_app(app, host='0.0.0.0', port=8080)
