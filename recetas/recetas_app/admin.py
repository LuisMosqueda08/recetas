from django.contrib import admin

from recetas_app.models.receta import Receta, Ingrediente, Paso

class PasoInline(admin.TabularInline):
    model = Paso

    extra = 0

class IngredienteInline(admin.TabularInline):
    model = Ingrediente

    extra = 0


class RecetaAdmin(admin.ModelAdmin):
    inlines = [IngredienteInline, PasoInline]
    list_display = ['nombre', 'created_at']



admin.site.register(Receta, RecetaAdmin)