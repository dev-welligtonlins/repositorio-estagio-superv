from django.db import models
from django.utils import timezone
from acompanhamentos.models import Acompanhamentos

class Feedbacks(models.Model):
    fee_id = models.AutoField(db_column='fee_id', primary_key=True)
    fee_titulo = models.CharField(db_column='fee_titulo', max_length=255)
    fee_descricao = models.TextField(db_column='fee_descricao', max_length=255, blank=True, null=True)
    fee_data = models.DateTimeField(db_column='fee_data', default = timezone.now)
    fee_arquivo = models.FileField(db_column='fee_arquivo', blank=True, null=True)
    fee_acompanhamento = models.ForeignKey(Acompanhamentos, on_delete=models.SET_NULL, db_column='fee_acompanhamento', blank=True, null=True)
    def __str__(self):
        return self.fee_titulo

    class Meta:
        managed = False
        db_table = 'feedbacks'
