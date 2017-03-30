import csv,sys,os

project_dir= "/home/iffu/Documents/Projectapp/Projectapp/"

sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django

django.setup()

from movies.models import Picture

data = csv.reader(open("/home/iffu/Documents/Projectapp/data.csv"),delimiter=",")

for row in data:
	if row[0] != 'picture_id':
		picture = Picture()
		picture.picture_id = row[0]
		picture.picture_title = row[1]
		picture.genres = row[2]
		picture.ratings = row[3]
		picture.picture_logo = row[4]
		picture.save()
		

