
# Map-view

This is a web-App developed using geodjango , PostGIS and Leaflet.js


## Demo
### Display
![](https://github.com/Rl0007/mapview/blob/master/media/show.gif)

This diplays data in PostGIS database

## Create

![](https://github.com/Rl0007/mapview/blob/master/media/create.gif)

Creating new polygon and saving it to PostGIS database

## Update

![](https://github.com/Rl0007/mapview/blob/master/media/edit.gif)

Edits existing polygon in database

## Delete

![](https://github.com/Rl0007/mapview/blob/master/media/delete.gif)

Deleting an entry from database 

## Run locally

To run locally start PostGIS server at local host

Install GDAL on your system 

cd into geodjango folder

Install requiremnts.txt using pip

use command 
```
> python manage.py makemigrations
```
and
```
> python manage.py migrate 
```
To make database

Then start the sever using
```
> python manage.py runserver
```

#### while running the app:-

1. Click on add to add state
2. Click on name to view or edit polygon
3. Click on delet to delete entry
## Tech Stack

**Client:** HTML, Bootstrap, css, leaflet.js, Ajax

**Server:** Django, PostGIS


## Support

For support, email 12agrawalrahul@gmail.com


## Summary

Could have done more like used reactjs or could have hosted on heroku but was not able to do it 
becaue of time constraints.
