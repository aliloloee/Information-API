from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, max_value=None, *args, **kwargs):
        self.max_value = max_value
        models.IntegerField.__init__(self, verbose_name, *args, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': 0, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)

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
    national_id = models.CharField(verbose_name='National id', max_length=20)
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

