from django.contrib import admin
from catalog.models import *
# Register your models here.
admin.site.register(Genre)
admin.site.register(Country)
# admin.site.register(ProfileUser)
# admin.site.register(Actor)
# admin.site.register(Director)
@admin.register(Comment)
class adminComment(admin.ModelAdmin):
    list_display = ('user','timedata','kino','active')

@admin.register(ProfileUser)
class adminProfileUser(admin.ModelAdmin):
    list_display = ('user','podpiska')


@admin.register(Actor)
class adminActor(admin.ModelAdmin):
    list_display = ('name','lastname')
    list_display_links = ('name','lastname')

@admin.register(Director)
class adminDirector(admin.ModelAdmin):
    list_display = ('name','lastname')
    list_display_links = ('name','lastname')

# admin.site.register(Podpiska)

@admin.register(Kino)
class adminKino(admin.ModelAdmin):
    list_display = ('title','genre','director','year','country', 'displayAct')
    fieldsets = (('О фильме',{'fields':('title','genre','opisanie')}),
                 ('Люди',{'fields':('director','actors')}),
                 ('Остальное',{'fields':('country','year','podpiska','image','trailer')})
                 )
    list_filter = ('genre','podpiska','country','year')


class PodpiskaLine(admin.TabularInline):
    model = Kino

@admin.register(Podpiska)
class adminPod(admin.ModelAdmin):
    lines = [PodpiskaLine]

