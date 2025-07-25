from aiohttp import web
import aiohttp_jinja2
import jinja2
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = web.Application()
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(os.path.join(BASE_DIR, 'templates')))

routes = web.RouteTableDef()

@routes.get('/')
@aiohttp_jinja2.template('index.html')
async def index(request):
    return {
        "bots": [
            {
                "title": "Save Restricted Content Bot",
                "desc": "Bypass restrictions & save any Telegram media.",
                "price": "₹199/month"
            },
            {
                "title": "Auto Rename Bot",
                "desc": "Automatically rename files with speed & efficiency.",
                "price": "₹149/month"
            },
            {
                "title": "File Rename Bot",
                "desc": "Rename and organize files directly in Telegram.",
                "price": "₹99/month"
            },
            {
                "title": "Personal Bots",
                "desc": "Get custom bots built just for your needs.",
                "price": "Starts ₹499"
            }
        ]
    }

app.add_routes(routes)
app.router.add_static('/static/', path=os.path.join(BASE_DIR, 'static'), name='static')

if __name__ == '__main__':
    web.run_app(app, host='0.0.0.0', port=8080)
