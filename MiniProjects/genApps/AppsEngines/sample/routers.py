
#We have our Own routers.py
import sys, traceback
import os
import pdb
class MyAppRouter(object):
    """
    A router to control all database operations on models in the
    sample application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read sample models go to sample_db.
        """
        if model._meta.app_label == 'sample':
            return 'sample_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write sample models go to sample_db.
        """
        if model._meta.app_label == 'sample':
            return 'sample_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the sample app is involved.
        """
        if obj1._meta.app_label == 'sample' or            obj2._meta.app_label == 'sample':
           return True
        return None

    def allow_migrate(self, db, app_label, model=None, **hints):
        """
        Make sure the sample app only appears in the 'sample_db'
        database.
        """
        if app_label == 'sample':
            return db == 'sample_db'
        return None

