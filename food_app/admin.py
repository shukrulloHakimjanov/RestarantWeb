from django.contrib import admin
from . models import About,About2,Service,Menu,Booking,ContactUs,Clients,Map,Vidio


class BookingAdmin(admin.ModelAdmin):
    list_display=['name','data','people','text',]


class ClientsAdmin(admin.ModelAdmin):
    list_display=['title','description','stoke',]


class MenusAdmin(admin.ModelAdmin):
    list_display=['title','description','stoke','img']

admin.site.register(About)
admin.site.register(About2)
admin.site.register(Service)
admin.site.register(Map)
admin.site.register(Menu,MenusAdmin)
admin.site.register(Booking,BookingAdmin)
admin.site.register(ContactUs)
admin.site.register(Vidio)
admin.site.register(Clients , ClientsAdmin)
