from rest_framework import serializers
from jobboard.models import Employee,Joboffer

from datetime import datetime
from django.utils.timesince import timesince

"""
SERIALIZERS FOR BOTH EMPLOYEE AND JOBOFFER MODELS
"""

class JobofferSerializer(serializers.ModelSerializer):

# I WANT TO SHOW ADDITIONALLY THE TIME SINCE THE JOB OFFER WAS POSTED 

    time_since_publication = serializers.SerializerMethodField()

    def get_time_since_publication(self,object):
        created_at = object.created_at
        now = datetime.now()
        time_gap = timesince(created_at,now)
        return time_gap

# I WANT SOME BASIC VALIDATION CRITERIA FOR MY SERIALIZER :

    #NUMBERS LIKE 1738 OR 1002 WON'T BE ACCEPTED. THEY MUST BE ROUNDED
    #TO THE LOWER OR UPPER 50 --> 1700-1750 OR 1050-1000

    def validate_salary(self,value):
        if value.amount % 50 != 0 :
            raise serializers.ValidationError("Salary value shall be rounded to lower or upper 50")
        return value
    
    #TITLE LENGTH VALIDATION

    def validate_job_title(self,value):
        if len(value) < 10 :
            raise serializers.ValidationError("Title too short! Please insert a title longer than 10 characters")
        return value

    def validate(self,data):
        if data["job_title"] == data["job_description"]:
            raise serializers.ValidationError("Job title and description shall be different!")
        return data
    
    # DEFINITION OF META CLASS FOR MY SERIALIZER

    class Meta:
        model = Joboffer
        exclude = ("id",)

class EmployeeSerializer(serializers.ModelSerializer):

    joboffers = serializers.HyperlinkedRelatedField(many=True,
                                                    view_name="job-details",
                                                    read_only = True)
    
    class Meta:
        model = Employee
        exclude = ("id",)
