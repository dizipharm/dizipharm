from import_export import resources
from .models import bulkdata

class PersonResource(resources.ModelResource):
    class Meta:
        model = bulkdata
