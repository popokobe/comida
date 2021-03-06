# Generated by Django 3.0.2 on 2020-01-31 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comida_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('JPN', '和食'), ('LOCAL', '郷土料理'), ('SUSHI', '寿司'), ('RAMEN', 'ラーメン類'), ('CURRY', 'カレー'), ('FA', 'ファミレス・ファストフード'), ('MEAT', '焼肉・ステーキ等の肉関連'), ('BAR', '居酒屋・バー'), ('CHN', '中華'), ('WES', '洋食'), ('ITA', 'イタリアン'), ('FRA', 'フレンチ'), ('ASIA', 'アジア・エスニック'), ('CAFE', 'カフェ'), ('SWEETS', 'スイーツ'), ('OTHER', 'その他')], max_length=20),
        ),
    ]
