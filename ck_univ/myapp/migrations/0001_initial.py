# Generated by Django 4.1.1 on 2023-12-14 09:27

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='adcourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=60)),
                ('cdetails', models.CharField(max_length=60, null=True)),
                ('cduration', models.CharField(max_length=60)),
                ('cprice', models.CharField(max_length=100)),
                ('cgst', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='locations_add',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loc_name', models.CharField(max_length=60)),
                ('status', models.CharField(max_length=60, null=True)),
                ('created_at', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='paydetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candid_name', models.CharField(max_length=60)),
                ('amount', models.CharField(max_length=100, null=True)),
                ('final_amount', models.CharField(max_length=100, null=True)),
                ('gst_p', models.CharField(max_length=100, null=True)),
                ('dat', models.DateField(null=True)),
                ('ckid', models.IntegerField(null=True)),
                ('discount', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='qualifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualification', models.CharField(max_length=60)),
                ('remark', models.CharField(max_length=60, null=True)),
                ('created_at', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Rep_id',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipt_id', models.IntegerField(default=0)),
                ('dat', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_name', models.CharField(max_length=60)),
                ('status', models.CharField(max_length=60, null=True)),
                ('created_at', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ck_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Location', models.CharField(max_length=100)),
                ('education', models.CharField(max_length=60)),
                ('comp_year', models.IntegerField(blank=True, null=True)),
                ('parent_name', models.CharField(max_length=60)),
                ('ph_num', models.CharField(max_length=20, unique=True)),
                ('al_ph_num', models.CharField(max_length=20)),
                ('parent_ph_num', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('address', models.CharField(max_length=100)),
                ('source', models.CharField(max_length=20, null=True)),
                ('payment_type', models.CharField(max_length=50)),
                ('payment_mode', models.CharField(max_length=50)),
                ('amount', models.CharField(max_length=100)),
                ('remark', models.CharField(max_length=50)),
                ('receipt_id', models.CharField(default=0, max_length=20)),
                ('candid_name', models.CharField(max_length=60, null=True)),
                ('price', models.CharField(max_length=100, null=True)),
                ('blc_amnt', models.CharField(max_length=100, null=True)),
                ('dat', models.DateField(auto_now_add=True, null=True)),
                ('nxt_month', models.DateField(null=True)),
                ('status', models.CharField(max_length=20)),
                ('inactive_dat', models.DateField(null=True)),
                ('dis_price', models.CharField(max_length=100, null=True)),
                ('discount', models.CharField(max_length=100, null=True)),
                ('final_amount', models.CharField(max_length=100, null=True)),
                ('gst_amount', models.CharField(max_length=100, null=True)),
                ('gst_p', models.CharField(max_length=100, null=True)),
                ('cgst', models.CharField(max_length=100, null=True)),
                ('candid_no', models.CharField(max_length=25, null=True)),
                ('acourse', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.adcourse')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('role', models.CharField(blank=True, default='Admin', max_length=50, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'auth_user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
