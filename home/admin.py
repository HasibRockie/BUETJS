from django.contrib import admin
from home.models import Post, Contact, AllComment, Gellery, Viewer, Members, AboutUs

# Register your models here.
admin.site.register(Post)
admin.site.register(Contact)
admin.site.register(AllComment)
admin.site.register(Gellery)
admin.site.register(Viewer)
admin.site.register(Members)
admin.site.register(AboutUs)