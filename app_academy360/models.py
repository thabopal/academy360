from django.db import models

from django.db import models

class SchoolInformation(models.Model):
    SchoolEMISNumber = models.IntegerField(primary_key=True)
    CensusArea = models.CharField(max_length=255, blank=True, null=True)
    OfficialSchoolName = models.CharField(max_length=255, blank=True, null=True)
    ProvincialDepartment = models.IntegerField(blank=True, null=True)
    EducationDistrict = models.IntegerField(blank=True, null=True)
    EducationRegion = models.CharField(max_length=255, blank=True, null=True)
    Circuit_Cluster = models.CharField(max_length=255, blank=True, null=True)
    DistrictCode = models.IntegerField(blank=True, null=True)
    PostalAddressType = models.IntegerField(blank=True, null=True)
    StreetName = models.CharField(max_length=255, blank=True, null=True)
    BuildingName = models.CharField(max_length=255, blank=True, null=True)
    BuildingNumber = models.IntegerField(blank=True, null=True)
    VillageName = models.CharField(max_length=255, blank=True, null=True)
    DwellingNumber = models.IntegerField(blank=True, null=True)
    PrivateBagNumber = models.IntegerField(blank=True, null=True)
    POBoxNumber = models.IntegerField(blank=True, null=True)
    StreetNumber = models.IntegerField(blank=True, null=True)
    Formatted_Address = models.CharField(max_length=255, blank=True, null=True)
    Suburb = models.CharField(max_length=255, blank=True, null=True)
    Town_City = models.CharField(max_length=255, blank=True, null=True)
    PostalCode = models.CharField(max_length=255, blank=True, null=True)
    PhysicalAddress = models.CharField(max_length=255, blank=True, null=True)
    PhysicalAddressTown_City = models.CharField(max_length=255, blank=True, null=True)
    PhysicalAddressSuburb = models.CharField(max_length=255, blank=True, null=True)
    PhysicalAddressPostalCode = models.CharField(max_length=255, blank=True, null=True)
    NearestTown = models.CharField(max_length=255, blank=True, null=True)
    DistanceToNearestTown_km = models.IntegerField(blank=True, null=True)
    ErfNumber = models.IntegerField(blank=True, null=True)
    EMISOfficer = models.CharField(max_length=255, blank=True, null=True)
    EMISOfficerType = models.IntegerField(blank=True, null=True)
    SchoolFirstNumber = models.CharField(max_length=255, blank=True, null=True)
    SchoolSecondNumber = models.CharField(max_length=255, blank=True, null=True)
    EmailAddress = models.EmailField(max_length=255, blank=True, null=True)
    AlternativeEmailAddress = models.EmailField(max_length=255, blank=True, null=True)
    InternetAccess = models.BooleanField(default=False)
    NumberOfAdministrativeComputers = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'school_information'  # Ensure this matches your table name in PostgreSQL
        verbose_name = 'School Information'
        verbose_name_plural = 'School Information'

    def __str__(self):
        return self.OfficialSchoolName or str(self.EMISNumber)

