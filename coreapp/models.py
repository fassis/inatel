from django.db import models

class HealthUnityFile(models.Model):

    file = models.FileField(upload_to='imports')
    created_at = models.DateTimeField(auto_now_add=True)

    CNES = 'CNES'
    UF = 'UF'
    IBGE = 'IBGE'
    NOME = 'NOME'
    LOGRADOURO = 'LOGRADOURO'
    BAIRRO = 'BAIRRO'
    LATITUDE = 'LATITUDE'
    LONGITUDE = 'LONGITUDE'

    COLUMNS = [CNES, UF, IBGE, NOME, LOGRADOURO, BAIRRO, LATITUDE, LONGITUDE]

    class Meta:
        verbose_name = 'Arquivo de Unidade Básica de Saúde'
        verbose_name_plural = 'Arquivos de Unidades Básicas de Saúde'

    def __str__(self):
        """HealthUnityFile head representation."""
        return str(self.pk)
    
    def field_list(self):
        return [
                (u'Id', self.pk),
                (u'Nº UBSs', self.healthunity_set.all().count()),
                (u'Arquivo', self.file),
                (u'Importado em', self.created_at),
                ]

    def save_data_frame(self, df):
        unities = []

        for item in df.index:
            validated_dict = df.loc[item].to_dict()
            unities.append(
                HealthUnity(
                    file=self,
                    cnes_code=str(validated_dict[HealthUnityFile.CNES]),
                    ibge_uf=str(validated_dict[HealthUnityFile.UF]),
                    ibge_city=str(validated_dict[HealthUnityFile.IBGE]),
                    name=str(validated_dict[HealthUnityFile.NOME]),
                    address=str(validated_dict[HealthUnityFile.LOGRADOURO]),
                    district=str(validated_dict[HealthUnityFile.BAIRRO]),
                    lat=str(validated_dict[HealthUnityFile.LATITUDE]),
                    lon=str(validated_dict[HealthUnityFile.LONGITUDE]),
                    )
            )

        HealthUnity.objects.bulk_create(unities)


class HealthUnity(models.Model):
    file = models.ForeignKey(HealthUnityFile, on_delete=models.CASCADE)
    cnes_code = models.PositiveIntegerField()
    ibge_uf = models.PositiveIntegerField()
    ibge_city = models.PositiveIntegerField()
    name = models.CharField(max_length=253)
    address = models.CharField(max_length=253)
    district = models.CharField(max_length=253,null=True,blank=True)
    lat = models.FloatField(null=True,blank=True)
    lon = models.FloatField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Unidade de Saúde'
        verbose_name_plural = 'Unidades de Saúde'

    def __str__(self):
        """HealthUnitySaude head representation"""
        return str(self.name)
    
    def field_list(self):
        return [
                (u'CNES', self.cnes_code),
                (u'Nome', self.name),
                (u'Logradouro', self.address),
                ]

