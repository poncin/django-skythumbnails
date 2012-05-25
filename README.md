# SkyThumbnails

This library provides a model field, ``EnhancedImageField``, which adds thumbnail support to the default ``ImageField``.

## Settings.py

### Required settings

    INSTALLED_APPS = [
        ...
        'sky_thumbnails',
        ...
    ]

### Optional settings

To change the quality of JPEG thumbnails (default is 85):    
    
    THUMBNAILS_QUALITY = 95
    
To create PNG thumbnails instead of JPEG:

    THUMBNAILS_FORMAT = 'PNG'

Thumbnails are generated when the ``EnhancedImageField`` is saved. To generate missing thumbnails on request:

    THUMBNAILS_DELAYED_GENERATION = True

Thumbnails will be saved in a directory relative to the ImageField's upload_to value. By default, the directory will be named 'thumbs'. To change the directory's name: 
    
    THUMBNAILS_DIRNAME = 'thumbnails'


## How to Use

The following code snippet illustrates how to use the ``EnhancedImageField``::

    from django.db import models
    from sky_thumbnails.fields import EnhancedImageField
    
    class MyModel(models.Model):
        photo = EnhancedImageField(
            verbose_name='Icon for the Services index page',
            upload_to = 'uploads/technology',
            process_source = dict(size=(300,600)),
            thumbnails = {
                'icon': dict(size=(30,60)),
            }
        )

The following code snippet illustrates how to print an ``EnhancedImageField`` in a 
Jinja2 template. Note, we are checking to make sure the image exists before 
calling the url property. The url property appends the STATIC_URL to the path
of the image::

    {% if object.photo %}
        <img src="{{object.photo.url}}" alt="Full image" />
        {% if object.photo.icon %}
            <img src="{{object.photo.icon.url}} alt="Small image" />
        {% endif %}
    {% endif %}


## LICENSE

This project is licensed under the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0). 

For copyright and other important notes regarding this release please read the AUTHORS file.

