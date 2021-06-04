from django.db import models
from django.utils.text import slugify
from django.urls import reverse

from customUser.models import User
from .models_utils import (ContentTypeRestrictedFileField, IntegerRangeField,
                    validate_national_id, file_directory_path)


class Information(models.Model) :
    GENDER = (
        ('male' , 'Male'),
        ('female' , 'Female'),
    )

    MARITAL_STATUS = (
        ('single' , 'Single'),
        ('married' , 'Married'),
    )

    BLOOD = (
        ('a+' , 'A+'),
        ('a-' , 'A-'),
        ('b+' , 'B+'),
        ('b-' , 'B-'),
        ('o+' , 'O+'),
        ('o-' , 'O-'),
        ('ab+', 'AB+'),
        ('ab-', 'AB-'),
    )

    CHILDBIRTH = (
        ('', '---------'),  ## 9 dashes
        ('no birth', 'No Birth'),
        ('natural', 'Natural'),
        ('cesarean', 'Cesarean'),
    )

    REGULAR = (
        ('no' , 'No'),
        ('yes' , 'Yes'),
    )

    FEMALE_ONLY_REGULAR = (
        ('', '---------'),  ## 9 dashes
        ('no' , 'No'),
        ('yes' , 'Yes'),
    )

    fullname = models.CharField(verbose_name='Fullname', max_length=100)
    national_id = models.CharField(verbose_name='National id', max_length=20, validators=[validate_national_id], unique=True)
    gender = models.CharField(verbose_name='Gender', max_length=20, choices=GENDER, default='male')
    eye_color = models.CharField(verbose_name='Eye color', max_length=50)
    weight = models.DecimalField(verbose_name='Weight', max_digits=4, decimal_places=1)
    height = models.DecimalField(verbose_name='Height', max_digits=4, decimal_places=1)
    blood_type = models.CharField(verbose_name='Blood type', max_length=50, choices=BLOOD, default='a+')
    marital_status = models.CharField(verbose_name='Maritual ctatus', max_length=20, choices=MARITAL_STATUS, default='single')
    male_childern_number = IntegerRangeField(verbose_name='Number of male children', max_value=99)
    female_childern_number = IntegerRangeField(verbose_name='Number of female children', max_value=99)


    ## yes/no/description
    congenital_disease = models.CharField(verbose_name='Congenital disease', max_length=20, choices=REGULAR, default='no')
    congenital_disease_description = models.TextField(verbose_name='Congenital disease description', default='', blank=True)

    blood_pressure = models.DecimalField(verbose_name='Blood pressure', max_digits=2, decimal_places=0)

    ## yes/no
    diabetes_disease_background = models.CharField(verbose_name='Diabetes disease background', max_length=20, choices=REGULAR, default='no')

    ## yes/no/description
    hereditary_disease_background = models.CharField(verbose_name='Hereditary disease background', max_length=20, choices=REGULAR, default='no')
    hereditary_disease_description = models.TextField(verbose_name='Hereditary disease description', default='', blank=True)

    ## yes/no/description/date
    surgery = models.CharField(verbose_name='Surgery background', max_length=20, choices=REGULAR, default='no')
    surgery_description = models.TextField(verbose_name='Surgery description', default='', blank=True)
    surgery_date = models.DateField(verbose_name='Date of surgery', blank=True, null=True)

    ## yes/no/description
    alcohol_consumption_background = models.CharField(verbose_name='Alcohol cunsumption background', max_length=20, choices=REGULAR, default='no')
    alcohol_consumption_description = models.TextField(verbose_name='Alcohol cunsumption', default='', blank=True)

    ## yes/no/type/description
    tobacco_consumption_background = models.CharField(verbose_name='Tobacco cunsumption background', max_length=20, choices=REGULAR, default='no')
    tobacco_type = models.CharField(verbose_name='Type of tobacco', max_length=200, default='', blank=True)
    tobacco_consumption_description = models.TextField(verbose_name='Tobacco cunsumption', default='', blank=True)

    medications = models.TextField(verbose_name='Medications', default='')

    ## yes/no/description
    medical_allergy_background = models.CharField(verbose_name='Medical allergy background', max_length=20, choices=REGULAR, default='no')
    medical_allergy_description = models.TextField(verbose_name='Medical allergy description', default='', blank=True)

    ## yes/no/description
    food_allergy_background = models.CharField(verbose_name='Food allergy background', max_length=20, choices=REGULAR, default='no')
    food_allergy_description = models.TextField(verbose_name='Food allergy description', default='', blank=True)

    ## yes/no/description
    emotional_shock_background = models.CharField(verbose_name='Emotional shock background', max_length=20, choices=REGULAR, default='no')
    emotional_shock_description = models.TextField(verbose_name='Emotional shock description', default='', blank=True)

    ## yes/no/child_number
    single_child = models.CharField(verbose_name='Single child', max_length=20, choices=REGULAR, default='no')
    child_number = models.CharField(verbose_name='Child number', max_length=30)

    ## yes/no/description
    nearby_waves = models.CharField(verbose_name='Nearby waves situation', max_length=20, choices=REGULAR, default='no')
    nearby_waves_description = models.TextField(verbose_name='Nearby waves dicription', default='', blank=True)

    ## only for female gender
    menopausal_condition = models.CharField(verbose_name='Menopausal condition', max_length=20, choices=FEMALE_ONLY_REGULAR, blank=True)
    irregular_menopausal = models.CharField(verbose_name='iregular menopausal', max_length=20, choices=FEMALE_ONLY_REGULAR, blank=True)
    birth_giving = models.CharField(verbose_name='Type of child birth', max_length=20, choices=CHILDBIRTH, blank=True)

    doctor_considerations = models.TextField(verbose_name='Considerations of the Doctor', blank=True)


    slug = models.SlugField(max_length=250, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta :
        verbose_name = 'Information'
        verbose_name_plural = 'Information'
        ordering = ('created',)

    # def clean(self) :
    #     data = self.cleaned_data

    # def get_absolute_url(self) :
    #     return reverse('info:single', kwargs={'pk':self.pk, 'slug':self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.gender + self.national_id)
        super(Information, self).save(*args, **kwargs)

    def __str__(self) :
        return f'{self.national_id}'



# * It is vital to khow that, for models that have manytomany fields the process of creating a model instance is different.
# * The process is that first we create an instance of the model including data for all fields of the model execpt the ---
# * manytomany fields. when we created the instance (and save it), then we can add the manytomany field data to the ------
# * instance. for more info check the url below :
# * https://docs.djangoproject.com/en/3.2/topics/db/examples/many_to_many/
class ECGInformation(models.Model) :
    # related_name => returning all ECGs related to a doctor : doctor.ecg_data.all()
    # related_query_name => filtering through ECGs related to a doctor : 
    # doctor.ecg_data.filter(ecg__patient=<pk of a patient>)

    doctor = models.ManyToManyField(User, related_name='ecg_data', related_query_name= 'ecg',
                                    limit_choices_to={'user_type':1}, verbose_name='Doctor')

    patient = models.ForeignKey(Information, on_delete=models.PROTECT, related_name='ecg', verbose_name='Related patient')

    ecg = ContentTypeRestrictedFileField(upload_to=file_directory_path, content_types=['text/plain', ],
                                        max_upload_size=2621440)

    slug = models.SlugField(max_length=250, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta :
        verbose_name = 'ECG Information'
        verbose_name_plural = 'ECG Information'

    def save(self, *args, **kwargs):
        self.slug = slugify('ecg' + self.patient.national_id)
        super(ECGInformation, self).save(*args, **kwargs)

    def __str__(self) :
        return f'ECG of {self.patient.fullname}'