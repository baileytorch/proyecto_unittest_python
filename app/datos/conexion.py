from decouple import config
from peewee import DatabaseProxy, MySQLDatabase



def _crear_conexion():
    return MySQLDatabase(config('db'), **{
        'charset': 'utf8mb4',
        'host': config('host'),
        'port': config('port', cast=int),
        'user': config('user'),
        'password': config('password'),
    })


class _DatabaseProxy(DatabaseProxy):
    def __getattr__(self, nombre):
        if self.obj is None:
            self.initialize(_crear_conexion())
        return super().__getattr__(nombre)


database = _DatabaseProxy()


def base_datos():
    if database.obj is None:
        database.initialize(_crear_conexion())
    return database