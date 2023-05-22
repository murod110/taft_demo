from django.contrib import admin
from .models import *

admin.site.register(CustomUser)
admin.site.register(Category)
admin.site.register(Quality)
admin.site.register(Product)

admin.site.register(Design)
admin.site.register(ClientOrder)

admin.site.register(OurCustomers)
admin.site.register(Views)

