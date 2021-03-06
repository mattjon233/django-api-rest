# Generated by Django 4.0.4 on 2022-05-17 22:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vulnerabilities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=60)),
                ('ip', models.CharField(max_length=15)),
                ('risk_factor', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='VulnerabilityInAsset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solved', models.BooleanField(default=False)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets.asset')),
                ('vulnerability', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vulnerabilities.vulnerability')),
            ],
        ),
        migrations.AddField(
            model_name='asset',
            name='vulnerabilities',
            field=models.ManyToManyField(through='assets.VulnerabilityInAsset', to='vulnerabilities.vulnerability'),
        ),
    ]
