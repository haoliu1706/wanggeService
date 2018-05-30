# Generated by Django 2.0.4 on 2018-05-28 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(db_index=True, default='', max_length=18, verbose_name='编码')),
                ('name', models.CharField(blank=True, max_length=60, verbose_name='板块名称')),
                ('value1', models.CharField(default='', max_length=50, verbose_name='预留1')),
                ('value2', models.CharField(default='', max_length=50, verbose_name='预留2')),
                ('value3', models.CharField(default='', max_length=50, verbose_name='预留3')),
                ('remarks', models.CharField(default='', max_length=250, verbose_name='备注')),
                ('isactived', models.BooleanField(choices=[(True, '是'), (False, '否')], default=True, verbose_name='有效')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('parentblock', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stocks.Block', verbose_name='上级板块')),
            ],
            options={
                'verbose_name': '板块',
            },
        ),
        migrations.CreateModel(
            name='BlockDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remark', models.CharField(default='', max_length=250, verbose_name='备注')),
                ('isactived', models.BooleanField(choices=[(True, '是'), (False, '否')], verbose_name='有效')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('blockname', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='stocks.Block')),
            ],
            options={
                'verbose_name': '版块明细',
            },
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(db_index=True, max_length=10, verbose_name='代码')),
                ('name', models.CharField(max_length=8, verbose_name='公司简称')),
                ('shortcut', models.CharField(default='', max_length=8, verbose_name='快捷键')),
                ('usedName', models.CharField(default='', max_length=255, verbose_name='曾用名')),
                ('market', models.IntegerField(choices=[(0, '深市'), (1, '沪市')], default=0, verbose_name='市场')),
                ('timeToMarket', models.DateField(verbose_name='上市日期')),
                ('decimalpoint', models.SmallIntegerField(default=2, verbose_name='价格小数位数')),
                ('volunit', models.IntegerField(default=100, verbose_name='每次交易最小成交单位')),
                ('category', models.SmallIntegerField(choices=[(10, '股票'), (11, '指数'), (12, '分级基金'), (13, '债券'), (14, '逆回购')], default=10, verbose_name='交易类别')),
                ('isdelisted', models.SmallIntegerField(choices=[(True, '是'), (False, '否')], default=False, verbose_name='是否退市')),
            ],
            options={
                'verbose_name': '证券列表',
            },
        ),
        migrations.CreateModel(
            name='RPS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rps120', models.DecimalField(decimal_places=3, max_digits=7, null=True, verbose_name='RPS120')),
                ('rps250', models.DecimalField(decimal_places=3, max_digits=7, null=True, verbose_name='RPS250')),
                ('tradedate', models.DateField(verbose_name='交易日期')),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='stocks.Listing', verbose_name='代码')),
            ],
            options={
                'verbose_name': '欧奈尔PRS',
            },
        ),
        migrations.CreateModel(
            name='RPSprepare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rps120', models.DecimalField(decimal_places=3, max_digits=7, null=True, verbose_name='RPS120')),
                ('rps250', models.DecimalField(decimal_places=3, max_digits=7, null=True, verbose_name='RPS250')),
                ('tradedate', models.DateField(verbose_name='交易日期')),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='stocks.Listing', verbose_name='代码')),
            ],
            options={
                'verbose_name': 'RPS准备',
            },
        ),
        migrations.CreateModel(
            name='StockDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('open', models.DecimalField(decimal_places=3, max_digits=9, null=True, verbose_name='开盘价')),
                ('close', models.DecimalField(decimal_places=3, max_digits=9, null=True, verbose_name='收盘价')),
                ('high', models.DecimalField(decimal_places=3, max_digits=9, null=True, verbose_name='最高价')),
                ('low', models.DecimalField(decimal_places=3, max_digits=9, null=True, verbose_name='最低价')),
                ('volumn', models.DecimalField(decimal_places=3, max_digits=9, null=True, verbose_name='vol')),
                ('amount', models.DecimalField(decimal_places=3, max_digits=9, null=True, verbose_name='金额')),
                ('tradedate', models.DateField(db_index=True, verbose_name='日期')),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='stocks.Listing', verbose_name='代码')),
            ],
            options={
                'verbose_name': '日数据',
            },
        ),
        migrations.CreateModel(
            name='Stocktradedate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tradedate', models.DateField(unique=True, verbose_name='交易日期')),
            ],
            options={
                'verbose_name': 'A股交易日',
            },
        ),
        migrations.AlterUniqueTogether(
            name='listing',
            unique_together={('code', 'market', 'category')},
        ),
        migrations.AddField(
            model_name='blockdetail',
            name='code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='stocks.Listing', verbose_name='代码'),
        ),
        migrations.AlterUniqueTogether(
            name='stockday',
            unique_together={('code', 'tradedate')},
        ),
        migrations.AlterUniqueTogether(
            name='rpsprepare',
            unique_together={('code', 'tradedate')},
        ),
        migrations.AlterUniqueTogether(
            name='blockdetail',
            unique_together={('code', 'blockname')},
        ),
        migrations.AlterUniqueTogether(
            name='block',
            unique_together={('name', 'parentblock')},
        ),
    ]
