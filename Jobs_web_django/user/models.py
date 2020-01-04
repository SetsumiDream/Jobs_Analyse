import datetime

from django.db import models


# Create your models here.
class User(models.Model):
    SEX = (
        ('female', '女'),
        ('male', '男')
    )
    phonenum = models.CharField(max_length=32, verbose_name='手机号', unique=True)
    nickname = models.CharField(max_length=128, verbose_name='昵称', unique=True)
    sex = models.CharField(max_length=8, choices=SEX, verbose_name='性别')
    birth_year = models.IntegerField(default=2000, verbose_name='出生年')
    birth_month = models.IntegerField(default=1, verbose_name='出生月')
    birth_day = models.IntegerField(default=1, verbose_name='出生日')
    avatar = models.CharField(max_length=256, verbose_name='个人形象')
    location = models.CharField(max_length=128, verbose_name='常居地')

    class Meta:
        db_table = 'user'

    def __str__(self):
        return f'<User {self.nickname}>'

    @property
    def age(self):
        birthday = datetime.datetime(year=self.birth_year, month=self.birth_month,
                                     day=self.birth_day, )
        now = datetime.datetime.now()
        return (now - birthday).days // 365

    def to_dict(self):
        return {
            'phonenum': self.phonenum,
            'nickname': self.nickname,
            'sex': self.sex,
            'age': self.age,
            'avatar': self.avatar,
            'location': self.location,
        }