# Generated by Django 3.2.3 on 2021-06-14 15:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import info.models_utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100, verbose_name='Fullname')),
                ('national_id', models.CharField(max_length=20, unique=True, validators=[info.models_utils.validate_national_id], verbose_name='National id')),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=20, verbose_name='Gender')),
                ('eye_color', models.CharField(max_length=50, verbose_name='Eye color')),
                ('weight', models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Weight')),
                ('height', models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Height')),
                ('blood_type', models.CharField(choices=[('a+', 'A+'), ('a-', 'A-'), ('b+', 'B+'), ('b-', 'B-'), ('o+', 'O+'), ('o-', 'O-'), ('ab+', 'AB+'), ('ab-', 'AB-')], default='a+', max_length=50, verbose_name='Blood type')),
                ('marital_status', models.CharField(choices=[('single', 'Single'), ('married', 'Married')], default='single', max_length=20, verbose_name='Maritual ctatus')),
                ('male_childern_number', info.models_utils.IntegerRangeField(verbose_name='Number of male children')),
                ('female_childern_number', info.models_utils.IntegerRangeField(verbose_name='Number of female children')),
                ('congenital_disease', models.CharField(choices=[('no', 'No'), ('yes', 'Yes')], default='no', max_length=20, verbose_name='Congenital disease')),
                ('congenital_disease_description', models.TextField(blank=True, default='', verbose_name='Congenital disease description')),
                ('blood_pressure', models.DecimalField(decimal_places=0, max_digits=2, verbose_name='Blood pressure')),
                ('diabetes_disease_background', models.CharField(choices=[('no', 'No'), ('yes', 'Yes')], default='no', max_length=20, verbose_name='Diabetes disease background')),
                ('hereditary_disease_background', models.CharField(choices=[('no', 'No'), ('yes', 'Yes')], default='no', max_length=20, verbose_name='Hereditary disease background')),
                ('hereditary_disease_description', models.TextField(blank=True, default='', verbose_name='Hereditary disease description')),
                ('surgery', models.CharField(choices=[('no', 'No'), ('yes', 'Yes')], default='no', max_length=20, verbose_name='Surgery background')),
                ('surgery_description', models.TextField(blank=True, default='', verbose_name='Surgery description')),
                ('surgery_date', models.DateField(blank=True, null=True, verbose_name='Date of surgery')),
                ('alcohol_consumption_background', models.CharField(choices=[('no', 'No'), ('yes', 'Yes')], default='no', max_length=20, verbose_name='Alcohol cunsumption background')),
                ('alcohol_consumption_description', models.TextField(blank=True, default='', verbose_name='Alcohol cunsumption')),
                ('tobacco_consumption_background', models.CharField(choices=[('no', 'No'), ('yes', 'Yes')], default='no', max_length=20, verbose_name='Tobacco cunsumption background')),
                ('tobacco_type', models.CharField(blank=True, default='', max_length=200, verbose_name='Type of tobacco')),
                ('tobacco_consumption_description', models.TextField(blank=True, default='', verbose_name='Tobacco cunsumption')),
                ('medications', models.TextField(default='', verbose_name='Medications')),
                ('medical_allergy_background', models.CharField(choices=[('no', 'No'), ('yes', 'Yes')], default='no', max_length=20, verbose_name='Medical allergy background')),
                ('medical_allergy_description', models.TextField(blank=True, default='', verbose_name='Medical allergy description')),
                ('food_allergy_background', models.CharField(choices=[('no', 'No'), ('yes', 'Yes')], default='no', max_length=20, verbose_name='Food allergy background')),
                ('food_allergy_description', models.TextField(blank=True, default='', verbose_name='Food allergy description')),
                ('emotional_shock_background', models.CharField(choices=[('no', 'No'), ('yes', 'Yes')], default='no', max_length=20, verbose_name='Emotional shock background')),
                ('emotional_shock_description', models.TextField(blank=True, default='', verbose_name='Emotional shock description')),
                ('single_child', models.CharField(choices=[('no', 'No'), ('yes', 'Yes')], default='no', max_length=20, verbose_name='Single child')),
                ('child_number', models.CharField(max_length=30, verbose_name='Child number')),
                ('nearby_waves', models.CharField(choices=[('no', 'No'), ('yes', 'Yes')], default='no', max_length=20, verbose_name='Nearby waves situation')),
                ('nearby_waves_description', models.TextField(blank=True, default='', verbose_name='Nearby waves dicription')),
                ('menopausal_condition', models.CharField(blank=True, choices=[('', '---------'), ('no', 'No'), ('yes', 'Yes')], max_length=20, verbose_name='Menopausal condition')),
                ('irregular_menopausal', models.CharField(blank=True, choices=[('', '---------'), ('no', 'No'), ('yes', 'Yes')], max_length=20, verbose_name='iregular menopausal')),
                ('birth_giving', models.CharField(blank=True, choices=[('', '---------'), ('no birth', 'No Birth'), ('natural', 'Natural'), ('cesarean', 'Cesarean')], max_length=20, verbose_name='Type of child birth')),
                ('doctor_considerations', models.TextField(blank=True, verbose_name='Considerations of the Doctor')),
                ('slug', models.SlugField(blank=True, max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Information',
                'verbose_name_plural': 'Information',
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='ECGInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ecg', info.models_utils.ContentTypeRestrictedFileField(upload_to=info.models_utils.file_directory_path)),
                ('slug', models.SlugField(blank=True, max_length=250)),
                ('recorded_at', models.DateTimeField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('doctor', models.ManyToManyField(limit_choices_to={'user_type': 1}, related_name='doctor_ecg_data', to=settings.AUTH_USER_MODEL, verbose_name='Doctor')),
                ('nurse', models.ForeignKey(limit_choices_to={'user_type': 2}, on_delete=django.db.models.deletion.PROTECT, related_name='nurse_ecg_data', to=settings.AUTH_USER_MODEL, verbose_name='Nurse')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ecg', to='info.information', verbose_name='Related patient')),
            ],
            options={
                'verbose_name': 'ECG Information',
                'verbose_name_plural': 'ECG Information',
            },
        ),
    ]
