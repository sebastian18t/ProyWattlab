# Generated by Django 3.0.4 on 2020-05-01 13:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('factura', '0006_auto_20200501_1149'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nmbre_bnco', models.CharField(max_length=50)),
                ('drccn', models.CharField(max_length=150)),
                ('tlfno', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ciudad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nmbre_cdd', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Consumo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kwh', models.IntegerField()),
                ('prdo_cnsmo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nmbre_dprtmnto', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='EstadoSucursalCliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dscrpcn_estdo_scrsl_clnte', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Facturacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnsctvo_trfa', models.FloatField()),
                ('vlr_cnsmo', models.FloatField()),
                ('vlr_intrss_mra', models.FloatField()),
                ('vlr_rcnxn', models.FloatField()),
                ('vlr_ttl', models.FloatField()),
                ('fcha_lmte_pgo', models.DateField()),
                ('cntdd_fctrs_pndts', models.IntegerField()),
                ('fcha_crte_srvco', models.DateField()),
                ('estdo_fctra', models.BooleanField()),
                ('cnsctvo_cnsmo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='factura.Consumo')),
            ],
        ),
        migrations.CreateModel(
            name='SubEstacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('drccn', models.CharField(max_length=150)),
                ('tlfno', models.CharField(max_length=50)),
                ('lngtd', models.IntegerField()),
                ('lttd', models.IntegerField()),
                ('cnsctvo_cdd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='factura.ciudad')),
            ],
        ),
        migrations.CreateModel(
            name='Tarifa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vlr_kwh', models.FloatField()),
                ('inco_vgnca', models.DateField()),
                ('fn_vgnca', models.DateField()),
                ('obsrvcn', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='tipoCliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dscrpcn_tpo_clnte', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TipoIdentificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dscrpcn_tpo_idntfcn', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Transformador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tnsn_prmra', models.IntegerField()),
                ('tnsn_mxma_srvco', models.IntegerField()),
                ('tnsn_scndra', models.IntegerField()),
                ('ptnca_nmnl', models.IntegerField()),
                ('rlcn_trnsfrmcn', models.IntegerField()),
                ('intnsdd_nmnl_prmra', models.IntegerField()),
                ('tnsn_crto_crcto', models.IntegerField()),
                ('grpo_cnxn', models.IntegerField()),
                ('lngtd', models.IntegerField()),
                ('lttd', models.IntegerField()),
                ('nmro_unco_idntfccn_sub_estcn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='factura.SubEstacion')),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vlr_pgdo', models.FloatField()),
                ('fcha_pgo', models.DateField()),
                ('cnsctvo_fctra', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='factura.Facturacion')),
                ('nmro_unco_idntfccn_bnco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='factura.Banco')),
                ('nmro_unco_idntfccn_usro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nmro_unco_idntfccn_clnte', models.IntegerField()),
                ('estrt_scl', models.CharField(max_length=150)),
                ('drccn', models.CharField(max_length=150)),
                ('cnsctvo_cdd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='factura.ciudad')),
            ],
        ),
        migrations.AddField(
            model_name='consumo',
            name='nmro_unco_idntfccn_cntrto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='factura.Contrato'),
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nmro_idntfccn', models.CharField(max_length=50)),
                ('prmr_nmbre', models.CharField(max_length=50)),
                ('sgndo_nmbre', models.CharField(max_length=50)),
                ('prmr_aplldo', models.CharField(max_length=50)),
                ('sgndo_aplldo', models.CharField(max_length=50)),
                ('fcha_ncmnto', models.DateField()),
                ('cnsctvo_tpo_clnte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='factura.tipoCliente')),
                ('cnsctvo_tpo_idntfcn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='factura.TipoIdentificacion')),
            ],
        ),
        migrations.AddField(
            model_name='ciudad',
            name='cnsctvo_dprtmnto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='factura.departamento'),
        ),
        migrations.AddField(
            model_name='banco',
            name='cnsctvo_cdd',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='factura.ciudad'),
        ),
    ]
