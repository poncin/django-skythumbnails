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

### Field definition

The ``EnhancedImageField`` derives from the default ``ImageField`` and thus all attributes and methods of the default ``ImageField`` are inherited.

In addition to the default arguments, the ``EnhancedImageField`` also supports the following:

``process_source``
    
A dictionary of *image processing options*. The same options, that can be used for the thumbnail generation, can also be set in this attribute. If this is set, the original image will be processed using the provided options before it is saved on the remote server. Contrariwise, if this attribute is not set or set to ``None``, the uploaded image is saved in its original form, without any further processing. It should be noted that setting this attribute to an empty dictionary still causes the source image to be processed using default image processing options. This practically means that the source image will be saved in the format specified by the ``THUMBNAILS_FORMAT`` setting without any resizing or filtering taking place.
    
``thumbnails``

A dictionary of *thumbnail definitions*. The format of each thumbnail definition is::
    
    <thumbnail_identifier> : <image_processing_options>

**thumbnail_identifier**

Is a string that uniquely identifies the thumbnail. It is required that all thumbnails use a unique identifier. This identifier is used in the thumbnail access mechanism and is also used in the generated filename of the thumbnail image file.

**image_processing_options**

This is a dictionary of options that will be used during the thumbnail generation. This dictionary must be present on every thumbnail definition. Any of the following supported options may be used:

``size``

A tuple which represents the size of the generated thumbnail.

``sharpen``

Boolean option. If set, the ``ImageFilter.SHARPEN`` filter will be applied to the thumbnail.

``detail``

Boolean option. If set, the ``ImageFilter.DETAIL`` filter will be applied to the thumbnail.

``upscale``

Boolean option. By default, image resizing occurs only if any of the source image dimensions is bigger than the dimension indicated by the ``size`` option. If the ``upscale`` option is set to ``True``, resizing occurs even if the generated thumbnail is bigger than the source image.

``format``

This is the format in which the thumbnail should be saved.

Valid values are those supported by the *Python Imaging Library* (PIL). If it is not set, then the default format specified by the ``THUMBNAILS_FORMAT`` setting will be used. In case the format is set to ``JPEG``, the value of the ``THUMBNAILS_QUALITY`` is used as the quality when the image is saved.


## LICENSE

This project is licensed under the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0). 

For copyright and other important notes regarding this release please read the AUTHORS file.

