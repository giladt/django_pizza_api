# Generated by Django 4.1.9 on 2023-05-24 22:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Status',
            new_name='OrderStatus',
        ),
        migrations.RenameField(
            model_name='orderstatus',
            old_name='status_name',
            new_name='order_status_name',
        ),
        migrations.AlterUniqueTogether(
            name='item',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='item',
            name='is_ready',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='order_status', to='api.orderstatus'),
        ),
        migrations.AlterField(
            model_name='item',
            name='flavour',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='flavour', to='api.flavour'),
        ),
        migrations.AlterField(
            model_name='item',
            name='size',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='size', to='api.size'),
        ),
        migrations.AlterField(
            model_name='order',
            name='client',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='client', to='api.client'),
        ),
        migrations.AlterUniqueTogether(
            name='item',
            unique_together={('flavour', 'size')},
        ),
        migrations.RemoveField(
            model_name='item',
            name='order',
        ),
        migrations.RemoveField(
            model_name='item',
            name='status',
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('item', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='item', serialize=False, to='api.item')),
                ('order', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='order', to='api.order')),
            ],
            options={
                'unique_together': {('order', 'item')},
            },
        ),
    ]
