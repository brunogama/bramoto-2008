from django.db import models
CATEGORIAS = (
    ('oficina','Oficina'),
    ('contato','Contato'),
)
class CaixaPostal(models.Model):
    nome = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 100, verbose_name = 'E-Mail')
    categoria = models.CharField(choices = CATEGORIAS, max_length = 8)
    def __unicode__(self):
        return self.nome
    class Meta:
        verbose_name = 'Caixa Postal'
        verbose_name_plural = 'Caixas Postais'
    

# Create your models here.
