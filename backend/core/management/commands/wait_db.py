import time

from django.core.management import BaseCommand
from django.db import connection, OperationalError
from django.db.backends.mysql.base import DatabaseWrapper


connection: DatabaseWrapper = connection


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write('Wait start db...')
        db_connection = False

        while not db_connection:
            try:
                connection.ensure_connection()
                db_connection = True

            except OperationalError:
                self.stdout.write('Database unavailable, please wait 5 second...')
                time.sleep(5)

        self.stdout.write('Database available')
