from django.apps import AppConfig
from django.db import connection, OperationalError
import sys


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):
        try:
            connection.ensure_connection()
            print("✔ Database connected successfully.")
        except OperationalError:
            print("❌ Database connection failed.")
            sys.exit(1)
