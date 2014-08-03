from django.db import models
import ast

class ListField(models.TextField):
    __metaclass__ = models.SubfieldBase
    description = "Stores a python list"

    def __init__(self, *args, **kwargs):
        super(ListField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if not value:
            value = []

        if isinstance(value, list):
            return value

        return ast.literal_eval(value)

    def get_prep_value(self, value):
        if value is None:
            return value

        return unicode(value)

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)

class DictField(models.TextField):
    __metaclass__ = models.SubfieldBase
    description = "Stores a python list"

    def __init__(self, *args, **kwargs):
        super(DictField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if not value:
            value = {}

        if isinstance(value, dict):
            return value

        return ast.literal_eval(value)

    def get_prep_value(self, value):
        if value is None:
            return value

        return unicode(value)

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)

class SetField(models.TextField):
    __metaclass__ = models.SubfieldBase
    description = "Stores a python list"

    def __init__(self, *args, **kwargs):
        super(SetField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if not value:
            value = set([])

        if isinstance(value, set):
            return value

        return ast.literal_eval(value)

    def get_prep_value(self, value):
        if value is None:
            return value

        return unicode(value)

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)

################# Test ###################
#class Dummy(models.Model):
#    mylist = ListField()
#    mydect = DictField()
#    #myset = SetField() <-- Cannot be suported as Django code Not support this
#
#    def __unicode__(self):
#        return u"TT:%s " % self.id
#
#>>>
#>>> d=Dummy()
#>>> d.mylist.append('hello')
#>>> d.mylist.append('hfello')
#>>> d.mylist.append('eello')
#>>> d.mylist.append('wello')
#>>> d.mylist
#['hello', 'hfello', 'eello', 'wello']
#>>> d.mylist.remove('eello')
#>>> d.mylist
#['hello', 'hfello', 'wello']
#>>> d.save()
#>>> d.mydect['sss']='ssss'
#>>> d.mydect['abc']=[1,2,3]
#>>> d.mydect
#    {'abc': [1, 2, 3], 'sss': 'ssss'}
#>>> d.mydect.get('abc')
#[1, 2, 3]
#>>> d.save()
#>>> Dummy.objects.all()
#[<Dummy: TT:1 >, <Dummy: TT:2 >]
#>>> Dummy.objects.filter(mylist__contains='he')
#[<Dummy: TT:1 >, <Dummy: TT:2 >]