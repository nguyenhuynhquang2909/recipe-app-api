"""
Django command to wait for the database to be ready before starting the application.
"""
import time
from psycopg2 import OperationalError as Pscopq2Error
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand
class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        """Entry point for command"""
        self.stdout.write('Waiting for database...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Pscopq2Error, OperationalError):
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available!'))