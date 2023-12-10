from flask import Flask

from src.db.database import connection
from src.services.ads import ads_router


class Builder:
    def __init__(self, app: Flask):
        self.app = app
        self.db = connection

    def run(self, *args, **kwargs) -> None:
        self.db.init_models()
        self.register_routers()
        self.app.run(*args, **kwargs)

    def register_routers(self):
        self.app.register_blueprint(ads_router)
