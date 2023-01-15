from django.db import models

class Inkoranya(models.Model):
    name=models.CharField(max_length=200)
    description= models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class Ubukwe(models.Model):
    name=models.CharField(max_length=200)
    description=models.FileField(upload_to='ubukwe/descriptions')

    def __str__(self):
        return self.name

class Imbyino(models.Model):
    name=models.CharField(max_length=200)
    cover=models.ImageField(upload_to='imbyino/covers',null=True,blank=True)
    description=models.FileField(upload_to='ubukwe/descriptions')

    def __str__(self):
        return self.name

class Ibikoresho(models.Model):
    name=models.CharField(max_length=200)
    image=models.ImageField(upload_to='ibikoresho/images',null=True,blank=True)
    description=models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Ubuhinzi(models.Model):
    name=models.CharField(max_length=200)
    description=models.FileField(upload_to='ubuhinzi/descriptions')

    def __str__(self):
        return self.name

class Indamukanyo(models.Model):
    name=models.CharField(max_length=200)
    description=models.FileField(upload_to='indamukanyo/descriptions')

    def __str__(self):
        return self.name


class Amasano(models.Model):
    name=models.CharField(max_length=200)
    description=models.FileField(upload_to='amasano/descriptions')

    def __str__(self):
        return self.name

class Ikibonezamvugo(models.Model):
    name=models.CharField(max_length=200)
    cover=models.ImageField(upload_to='ikibonezamvugo/covers',null=True,blank=True)
    description=models.FileField(upload_to='ikibonezamvugo/descriptions')

    def __str__(self):
        return self.name

class Umurage(models.Model):
    name=models.CharField(max_length=200)
    description=models.FileField(upload_to='umurage/descriptions')

    def __str__(self):
        return self.name

class Hugura(models.Model):
    cover=models.ImageField(upload_to='hugura/covers', null=True,blank=True)
    name=models.CharField(max_length=200)
    
    def __str__(self):
        return self.name



