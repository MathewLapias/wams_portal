# functions/main.py
from firebase_functions import https_fn, options
from firebase_admin import initialize_app
from app import app

# Atur region server agar lebih dekat ke Indonesia
options.set_global_options(region=options.SupportedRegion.ASIA_SOUTHEAST1)

initialize_app()

@https_fn.on_request()
def wams_app(req: https_fn.Request) -> https_fn.Response:
    with app.request_context(req.environ):
        return app.full_dispatch_request()
    