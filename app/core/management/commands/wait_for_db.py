"""
Django command to wait for the database to be available
"""

import time
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for the database to be available"""

    def handle(self, *args, **options):
        """Entry point for the management command"""
        self.stdout.write('Waiting for database...')
        db_up = False

        while not db_up:
            try:
                self.check(databases=['default'])
                db_up = True
            except (OperationalError, Psycopg2Error):
                self.stdout.write('Database is unavailable. Waiting for 1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))