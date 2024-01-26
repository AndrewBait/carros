from django.contrib import admin
#adcionar caminho p importar a classe e poder usar no admin.site.register
from cars.models import Car, Brand

class CarAdmin(admin.ModelAdmin):
	list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    #o cabeçalho que aparecera na tabela no painel admin: modelo, marca, ano fabricação, ano modelo, preço
	search_fields = ('model', 'brand',)
	#campo de busca se será achado pelo modelo
	
class BrandAdmin(admin.ModelAdmin):
	list_display = ('name',)
	search_fields = ('name',)

#e usar a funcao p registrar
admin.site.register(Car, CarAdmin)
#Car seria qual modelo
#CarAdmin seria config do admin
admin.site.register(Brand, BrandAdmin)