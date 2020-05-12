import json
from django.db import models
from django.core.serializers.json import DjangoJSONEncoder
import functools

class SaleItem:
    def __init__(self, particulars, hsn_code, unit, unit_per_package,
                 no_of_packages, rate_per_unit, *args, **kwargs):
        self.particulars = particulars
        self.hsn_code = hsn_code
        self.unit = unit
        self.unit_per_package = int(unit_per_package)
        self.no_of_packages = no_of_packages
        self.total_quantity = float(no_of_packages) * float(unit_per_package)
        self.rate_per_unit = float(rate_per_unit)
        self.amount = self.total_quantity * self.rate_per_unit


class SaleItemsListField(models.TextField):
    def to_python(self, value):
        if value == "":
            return None

        if isinstance(value, str):
            return [SaleItem(**item) for item in json.loads(value)]

        return value

    def get_db_prep_save(self, value, *args, **kwargs):
        if value == "":
            return None

        if isinstance(value, list):
            value = json.dumps(value, cls=DjangoJSONEncoder)

        return super().get_db_prep_save(value, *args, **kwargs)
