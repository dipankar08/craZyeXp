
#We have our Own routers.py
import sys, traceback
import os
import pdb
class MyAppRouter(object):
    """
    A router to control all database operations on models in the
    cleanCode application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read cleanCode models go to cleanCode_db.
        """
        if model._meta.app_label == 'cleanCode':
            return 'cleanCode_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write cleanCode models go to cleanCode_db.
        """
        if model._meta.app_label == 'cleanCode':
            return 'cleanCode_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the cleanCode app is involved.
        """
        if obj1._meta.app_label == 'cleanCode' or            obj2._meta.app_label == 'cleanCode':
           return True
        return None

    def allow_migrate(self, db, app_label, model=None, **hints):
        """
        Make sure the cleanCode app only appears in the 'cleanCode_db'
        database.
        """
        if app_label == 'cleanCode':
            return db == 'cleanCode_db'
        return None

