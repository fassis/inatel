import pandas as pd
from coreapp.models import HealthUnityFile
from django.core.exceptions import ValidationError

def dataframe_from_file(file):
    if file.name.endswith('.xlsx'):
        read_file = pd.read_excel(file)
    elif file.name.endswith('.csv'):
        read_file = pd.read_csv(file, encoding='utf8')
    else:
        raise Exception(
            'Formato inválido. São aceitos apenas arquivos .csv ou .xlsx')

    df = pd.DataFrame(read_file)

    headers = list(df)

    if not (set(HealthUnityFile.COLUMNS) <= set(headers)):
        raise Exception('Colunas inválidas. Deve conter: {}'.format(
            HealthUnityFile.COLUMNS))

    return df[df.columns.unique()]


def file_extension_validator(value):
    import os
    extension = os.path.splitext(value.name)[1]
    valid_extensions = ['.csv', '.xlsx']
    if not extension.lower() in valid_extensions:
        raise ValidationError(
            'São aceitos apenas arquivos .csv ou .xlsx')