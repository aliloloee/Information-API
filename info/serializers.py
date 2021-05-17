from rest_framework import serializers
from .models import Information
from persian_tools import national_id



class DateField(serializers.DateField) :
    def to_internal_value(self, value):
        if value == '' :
            value = None
            return value
        return super().to_internal_value(value)

class ChoiceField(serializers.ChoiceField) :
    def __init__(self, choices, *args, **kwargs) :
        self._choices = choices
        self.allow_blank = False      ## if True, then value of '' is also acceptable for the field
        super(ChoiceField, self).__init__(choices, *args, **kwargs)

    # def to_representation(self, obj):
    #     if obj == '' and self.allow_blank:
    #         return obj
    #     return self._choices[obj]

    def to_internal_value(self, data):
        # To support inserts with the value
        if data == '' and self.allow_blank:
            return ''

        for key, val in self._choices.items():
            if val == data:
                return key
        self.fail('invalid_choice', input=data)



class InformationSerializer(serializers.ModelSerializer) :

    gender = ChoiceField(choices=Information.GENDER)
    blood_type = ChoiceField(choices=Information.BLOOD)
    marital_status = ChoiceField(choices=Information.MARITAL_STATUS)

    congenital_disease = ChoiceField(choices=Information.REGULAR)
    diabetes_disease_background = ChoiceField(choices=Information.REGULAR)
    hereditary_disease_background = ChoiceField(choices=Information.REGULAR)
    surgery = ChoiceField(choices=Information.REGULAR)
    alcohol_consumption_background = ChoiceField(choices=Information.REGULAR)
    tobacco_consumption_background = ChoiceField(choices=Information.REGULAR)
    medical_allergy_background = ChoiceField(choices=Information.REGULAR)
    food_allergy_background = ChoiceField(choices=Information.REGULAR)
    emotional_shock_background = ChoiceField(choices=Information.REGULAR)
    single_child = ChoiceField(choices=Information.REGULAR)
    nearby_waves = ChoiceField(choices=Information.REGULAR)

    menopausal_condition = ChoiceField(choices=Information.FEMALE_ONLY_REGULAR)
    irregular_menopausal = ChoiceField(choices=Information.FEMALE_ONLY_REGULAR)
    birth_giving = ChoiceField(choices=Information.CHILDBIRTH)

    surgery_date = DateField(input_formats=['%Y-%m-%d', '%Y/%m/%d', '%Y.%m.%d', ]) 



    class Meta :
        model = Information
        fields = '__all__'
        read_only_fields = ("created", "updated", "slug", "doctor_considerations", )

    def validate_national_id(self, value) :
        if national_id.validate(value) :
            return value
        raise serializers.ValidationError('Wrong national id')
    
    def validate_weight(self, value) :
        if value < 0 or value > 999 :
            raise serializers.ValidationError('Wrong wight')
        return round(value, 1)

    def validate_height(self, value) :
        if value < 0 or value > 999 :
            raise serializers.ValidationError('Wrong height')
        return round(value, 1)

    def validate_male_childern_numbe(self, value) :
        if type(value) != int or value < 0 or value > 99 :
            raise serializers.ValidationError('Wrong input for number of male children')
        return value

    def validate_female_childern_number(self, value) :
        if type(value) != int or value < 0 or value > 99 :
            raise serializers.ValidationError('Wrong input for number of female children')
        return value


    def validate(self, attrs):
        ## Congenital Disease
        if attrs['congenital_disease'] == 'no' and attrs['congenital_disease_description'] != '' :
            raise serializers.ValidationError("Congenital disease can't have description")

        ## Hereditary Disease Background
        if attrs['hereditary_disease_background'] == 'no' and attrs['hereditary_disease_description'] != '' :
            raise serializers.ValidationError("Hereditary disease can't have description")

        ## Surgery
        if attrs['surgery'] == 'no' and attrs['surgery_description'] != '' :
            raise serializers.ValidationError("Surgery can't have description")
        if attrs['surgery'] == 'no' and attrs['surgery_date'] != None :
            raise serializers.ValidationError("Surgery can't have description or date")

        ## Alcohol
        if attrs['alcohol_consumption_background'] == 'no' and attrs['alcohol_consumption_description'] != '' :
            raise serializers.ValidationError("Alcohol consumption disease can't have description")

        ## Tobacco
        if attrs['tobacco_consumption_background'] == 'no' and attrs['tobacco_consumption_description'] != '' :
            raise serializers.ValidationError("Tobacco can't have description")
        if attrs['tobacco_consumption_background'] == 'no' and attrs['tobacco_type'] != '' :
            raise serializers.ValidationError("Tobacco can't have any type")

        ## Medical allergy
        if attrs['medical_allergy_background'] == 'no' and attrs['medical_allergy_description'] != '' :
            raise serializers.ValidationError("Medical allergy can't have description")

        ## Food allergy
        if attrs['food_allergy_background'] == 'no' and attrs['food_allergy_description'] != '' :
            raise serializers.ValidationError("Food allergy can't have description")

        ## Emotional shock
        if attrs['emotional_shock_background'] == 'no' and attrs['emotional_shock_description'] != '' :
            raise serializers.ValidationError("Emotional shock can't have description")

        ## Child number
        if attrs['single_child'] == 'yes' and attrs['child_number'] != '' :
            raise serializers.ValidationError("Child number is not needed")

        ## Nearby waves
        if attrs['nearby_waves'] == 'no' and attrs['nearby_waves_description'] != '' :
            raise serializers.ValidationError("Nearby waves can't have description")

        ## Female-only fields
        if attrs['gender'] == 'male' :
            if attrs['menopausal_condition'] != '' or attrs['irregular_menopausal'] != '' or attrs['birth_giving'] != '' :
                raise serializers.ValidationError("Only females fill these fields : menopausal_condition, irregular_menopausal and birth_giving")

        return attrs

    def create(self, validated_data) :
        obj = super().create(validated_data)
        obj.save()
        return obj

