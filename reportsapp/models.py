import os
from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class GenreModel(models.Model):
    genre_name = models.CharField(max_length=100)

    def __str__(self):
        return self.genre_name


class CrimeModel(models.Model):
    genre = models.ForeignKey(GenreModel, on_delete=models.CASCADE)
    crime_name = models.CharField(max_length=100)
    crime_name_second = models.CharField(max_length=100, null=True, blank=True)
    crime_start_date = models.DateField(null=True, blank=True)
    crime_start_time = models.TimeField(null=True, blank=True)
    crime_end_date = models.DateField(null=True, blank=True)
    crime_end_time = models.TimeField(null=True, blank=True)
    crime_place = models.CharField(max_length=100)
    crime_fact = models.TextField()

    def __str__(self):
        return self.crime_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # モデルの保存処理を先に実行
        content = f"crime name: {self.crime_name}\n"  # ファイルに書き込む内容
        content += f"crime name second: {self.crime_name_second}\n"
        content += f"crime start date: {self.crime_start_date}\n"
        content += f"crime start time: {self.crime_start_time}\n"
        content += f"crime end date: {self.crime_end_date}\n"
        content += f"crime end time: {self.crime_end_time}\n"
        content += f"crime place: {self.crime_place}\n"
        content += f"crime fact: {self.crime_fact}\n"

        # 他のフィールドも同様に追加することができます

        # ファイルのパスを設定
        file_path = os.path.join(settings.BASE_DIR, 'reportsapp', f'crime_{self.pk}.txt')

        # ファイルに内容を書き出し
        with open(file_path, 'w') as file:
            file.write(content)


class SuspectModel(models.Model):
    crime = models.ForeignKey(CrimeModel, on_delete=models.CASCADE)
    honseki = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    job = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name



class VictimModel(models.Model):
    crime = models.ForeignKey(CrimeModel, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, null=True, blank=True)
    job = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name