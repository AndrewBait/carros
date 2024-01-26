from django.db import models

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    # autofield é uma função de autoincremento
    # primary_key True é a chave primaria   
    model = models.CharField(max_length=200)
    # charfield eh campo de string campo de texto aceita td tipo de caractere
    # max_length eh numero maximo de caracteres
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand')
    # ForeingKey seria a cheve estrangeira relacionada a tabela Brand q seria o primeiro argumento passado
    # on_delete=PROTECT protege contra alguem tentar deletar
    # related_name é o nom,e dessa relacao entre car e brand
    factory_year = models.IntegerField(blank=True, null=True)
    # intergefield campo de numero inteiro
    # blank=True posso deixar em branco qnd for criar novo carro, nao abrigatorio preencher
    # null=True posso deixar nulo tbm
    model_year = models.IntegerField(blank=True, null=True)
    # blank=True posso deixar em branco qnd for criar novo carro, nao abrigatorio preencher
    # null=True posso deixar nulo tbm
    plate = models.CharField(max_length=10, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    # floatfield eh o tipo float, numero real, com virgula
    # blank=True posso deixar em branco qnd for criar novo carro, nao abrigatorio preencher
    # null=True posso deixar nulo tbm
    photo = models.ImageField(upload_to='cars/', blank=True, null=True)
    # armazena imagens na raiz de Cars
    bio = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.model
    

class CarInventory(models.Model):
    cars_count = models.IntegerField()
    cars_value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f'{self.cars_count} - {self.cars_value}'
