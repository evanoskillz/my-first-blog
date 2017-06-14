import sys,os
import csv


from django.contrib.gis.utils import LayerMapping
from .models import WorldBorder
from .models import Country
from .models import Province
from .models import County
from .models import Division
from .models import Location
from .models import Sublocation
from .models import School
from .models import Phase
from .models import PhaseSchool
from .models import Tti
from .models import Activity
from .models import Component
from .models import TaskStatus
from .models import NumberType
from .models import DeviceType
from .models import DeviceSpecification
from .models import Venue, ConsortiumPartner,CountySchool
# from fileupload.models import PictureType

world_mapping = {
    'fips' : 'FIPS',
    'iso2' : 'ISO2',
    'iso3' : 'ISO3',
    'un' : 'UN',
    'name' : 'NAME',
    'area' : 'AREA',
    'pop2005' : 'POP2005',
    'region' : 'REGION',
    'subregion' : 'SUBREGION',
    'lon' : 'LON',
    'lat' : 'LAT',
    'geom' : 'MULTIPOLYGON',
}

world_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'TM_WORLD_BORDERS-0.3.shp'),
)

country_mapping = {
    'gadmid' : 'GADMID',
    'iso' : 'ISO',
    'name' : 'NAME',
    'iso2' : 'ISO2',
    'www' : 'WWW',
    'sqkm' : 'SQKM',
    'shape_leng' : 'Shape_Leng',
    'shape_area' : 'Shape_Area',
    'geom' : 'MULTIPOLYGON',
}
country_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data/KEN_adm', 'KEN_adm0.shp'),
)

province_mapping = {
    'id' : 'ID',
    'name' : 'NAME',
    'shape_leng' : 'Shape_Leng',
    'shape_area' : 'Shape_Area',
    'geom' : 'MULTIPOLYGON',
}

province_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data/KEN_adm', 'KEN_adm1.shp'),
)

county_mapping = {
    # 'id' : 'ID',
    'name' : 'NAME',
    'type' : 'TYPE',
    'shape_leng' : 'Shape_Leng',
    'shape_area' : 'Shape_Area',
    'geom' : 'MULTIPOLYGON',
}

county_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data/KEN_adm', 'KEN_adm2.shp'),
)
division_mapping = {
    'id' : 'ID',
    'name' : 'NAME',
    'type' : 'TYPE',
    'shape_leng' : 'Shape_Leng',
    'shape_area' : 'Shape_Area',
    'geom' : 'MULTIPOLYGON',
}

division_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data/KEN_adm', 'KEN_adm3.shp'),
)

location_mapping = {
    'id' : 'ID',
    'name' : 'NAME',
    'type' : 'TYPE',
    'shape_leng' : 'Shape_Leng',
    'shape_area' : 'Shape_Area',
    'geom' : 'MULTIPOLYGON',
}
location_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data/KEN_adm', 'KEN_adm4.shp'),
)
sublocation_mapping = {
    'id' : 'ID',
    'name' : 'NAME',
    'type' : 'TYPE',
    'shape_leng' : 'Shape_Leng',
    'shape_area' : 'Shape_Area',
    'geom' : 'MULTIPOLYGON',
}
sublocation_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data/KEN_adm', 'KEN_adm5.shp'),)
school_mapping = {
    'county' : 'county',
    'subcounty' : 'subcounty',
    'zone' : 'zone',
    'runningsn' : 'runningsn',
    'zonesn' : 'zonesn',
    'schoolid' : 'schoolid',
    'name' : 'name',
    'lat' : 'lat',
    'long' : 'long',
    'headmaster' : 'headmaster',
    'headnumber' : 'headnumber',
    'senrol' : 'senrol',
    'c1enrol' : 'c1enrol',
    'teachers' : 'teachers',
    'geom' : 'POINT',
}
school_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data/phase_one', 'phase_one.shp'),)
school_mapping2 = {
    'county' : 'county',
    'subcounty' : 'subcounty',
    'zone' : 'zone',
    'runningsn' : 'runningsn',
    'zonesn' : 'zonesn',
    'schoolid' : 'schoolid',
    'name' : 'name',
    'lat' : 'lat',
    'long' : 'long',
    'headmaster' : 'headmaster',
    'headnumber' : 'headnumber',
    'senrol' : 'senrol',
    'c1enrol' : 'c1enrol',
    'teachers' : 'teachers',
    'geom' : 'POINT',
}
school_shp2 = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data/phase_two', 'phase_two.shp'),)

tti_mapping = {
    'name' : 'name',
    'county' : 'county',
    'address' : 'address',
    'email' : 'email',
    'lat' : 'lat',
    'long' : 'long',
    'geom' : 'POINT',
}
tti_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'ttis.shp'),)



def run(verbose=True):
    lm = LayerMapping(
        WorldBorder, world_shp, world_mapping,
        transform=False, encoding='iso-8859-1',
        
    )
    lm.save(strict=True, verbose=verbose)
    cm = LayerMapping(
        Country, country_shp, country_mapping,
        transform=False, encoding='iso-8859-1',
    )
    cm.save(strict=True, verbose=verbose)
    pm = LayerMapping(
        Province, province_shp, province_mapping,
        transform=False, encoding='iso-8859-1',
    )
    pm.save(strict=True, verbose=verbose)
    com = LayerMapping(
        County, county_shp, county_mapping,
        transform=False, encoding='iso-8859-1',
    )
    com.save(strict=True, verbose=verbose)    
    dm = LayerMapping(
        Division, division_shp, division_mapping,
        transform=False, encoding='iso-8859-1',
    )
    dm.save(strict=True, verbose=verbose)     
    lcm = LayerMapping(
        Location, location_shp, location_mapping,
        transform=False, encoding='iso-8859-1',
    )
    lcm.save(strict=True, verbose=verbose)   
    slcm = LayerMapping(
        Sublocation, sublocation_shp, sublocation_mapping,
        transform=False, encoding='iso-8859-1',
    )
    slcm.save(strict=True, verbose=verbose)
    ttiss = LayerMapping(
        Tti, tti_shp, tti_mapping,
        transform=False, encoding='iso-8859-1',
    )
    ttiss.save(strict=True, verbose=verbose) 
       


    schcm = LayerMapping(
        School, school_shp, school_mapping,
        transform=False, encoding='iso-8859-1',
    )
    schcm.save(strict=True, verbose=verbose)  
    schcm2 = LayerMapping(
        School, school_shp2, school_mapping,
        transform=False, encoding='iso-8859-1',
    )
    schcm2.save(strict=True, verbose=verbose)

    loadcsv()
    runschool()


def runschool(verbose=True): 
    for e in School.objects.all():
       
        phase_school=PhaseSchool()
        pahse = Phase.objects.get(id=1)
        phase_school.phase=pahse
        phase_school.school= e
        phase_school.save()

    for c in County.objects.all():
        for s in School.objects.all():
            if s.county.upper() == c.name.upper():
                county_school=CountySchool()
                county_school.county=c
                county_school.school=s
                county_school.save()


def loadcsv(verbose=True):

    phases_csv_filepathname=os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'phases.csv'),)
    project_home="/home/cgithinji/pyProjects/dlp/"
    sys.path.append(project_home)
    os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
    phasesdataReader = csv.reader(open(phases_csv_filepathname), delimiter=',', quotechar='"')
    for row in phasesdataReader:
            if row[0] != 'name': # Ignore the header row, import everything else
                phase = Phase()
                phase.name = row[0]
                phase.code = row[1]
                phase.save()


    activities_csv_filepathname = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'activities.csv'), )
    sys.path.append(project_home)
    os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
    activitiesdataReader = csv.reader(open(activities_csv_filepathname), delimiter=',', quotechar='"')
    for row in activitiesdataReader:
        if row[0] != 'name':  # Ignore the header row, import everything else
            activites = Activity()
            activites.name = row[0]
            activites.description = row[1]
            activites.save()

    numbertype_csv_filepathname = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'numbertype.csv'), )
    sys.path.append(project_home)
    os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
    numberdataReader = csv.reader(open(numbertype_csv_filepathname), delimiter=',', quotechar='"')
    for row in numberdataReader:
        if row[0] != 'name':  # Ignore the header row, import everything else
            numbertype = NumberType()
            numbertype.name = row[0]
            numbertype.description = row[1]
            numbertype.save()

    devicetype_csv_filepathname = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'devicetype.csv'), )
    sys.path.append(project_home)
    os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
    devicedataReader = csv.reader(open(devicetype_csv_filepathname), delimiter=',', quotechar='"')
    for row in devicedataReader:
        if row[0] != 'name':  # Ignore the header row, import everything else
            devicetype = DeviceType()
            devicetype.name = row[0]
            devicetype.description = row[1]
            devicetype.save()


    task_csv_filepathname = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'taskstatus.csv'), )
    sys.path.append(project_home)
    os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
    taskdataReader = csv.reader(open(task_csv_filepathname), delimiter=',', quotechar='"')
    for row in taskdataReader:
        if row[0] != 'name':  # Ignore the header row, import everything else
            taskstatus = TaskStatus()
            taskstatus.name = row[0]
            taskstatus.description = row[1]
            taskstatus.save()

    component_csv_filepathname = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'components.csv'), )
    sys.path.append(project_home)
    os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
    componentdataReader = csv.reader(open(component_csv_filepathname), delimiter=',', quotechar='"')
    for row in componentdataReader:
        if row[0] != 'name':  # Ignore the header row, import everything else
            component = Component()
            component.name = row[0]
            component.description = row[1]
            component.save()


    # picture_csv_filepathname = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'picturecategory.csv'), )
    # sys.path.append(project_home)
    # os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
    # picturedataReader = csv.reader(open(picture_csv_filepathname), delimiter=',', quotechar='"')
    # for row in picturedataReader:
    #     if row[0] != 'name':  # Ignore the header row, import everything else
    #         picture_ = PictureType()
    #         picture_.name = row[0]
    #         picture_.description = row[1]
    #         picture_.save()


    specs_csv_filepathname = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'specifications.csv'), )
    sys.path.append(project_home)
    os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
    specsdataReader = csv.reader(open(specs_csv_filepathname), delimiter=',', quotechar='"')
    for row in specsdataReader:
        if row[0] != 'feature':  # Ignore the header row, import everything else
            devicespecs = DeviceSpecification()
            devicespecs.feature = row[0]
            devicespecs.specification = row[1]
            devicespecs.devicetype=row[2]
            devicespecs.save()

    venue_csv_filepathname = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'venue.csv'), )
    sys.path.append(project_home)
    os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
    venuedataReader = csv.reader(open(venue_csv_filepathname), delimiter=',', quotechar='"')
    for row in venuedataReader:
        if row[0] != 'name':  # Ignore the header row, import everything else
            venue = Venue()
            venue.name = row[0]
            venue.description = row[1]
            venue.save()

    consortium_csv_filepathname = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'consortium.csv'), )
    sys.path.append(project_home)
    os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
    consortiumdataReader = csv.reader(open(consortium_csv_filepathname), delimiter=',', quotechar='"')
    for row in consortiumdataReader:
        if row[0] != 'name':  # Ignore the header row, import everything else
            consortium = ConsortiumPartner()
            consortium.name = row[0]
            consortium.description = row[1]
            consortium.save()