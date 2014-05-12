Vector graphics with Inkscape
=============================

==================
Graphical concepts
==================

A quote from the text (PCFB).

No longer can you submit a photo that looks right; it has to be a 
"CMYK image, with 300 DPI at printed dimension, saved as a TIFF with LZW compression".
The goal here is to introduce a software that can help with some of these requirements.
Please refer to Chapter 17 for further depth than we go into here on graphics.

**Vector** and **pixel** images are probably concepts most biologists are familiar with. 
Pixel images (bitmap, raster) are a uniform grid of colored dots.  In vector art a line 
can be defined by two endpoints.  The vector representation has the advantage of being 
often easier to store.  Also, the amount of information for vector art stays the same no
matter how large the plot and as you zoom in vector art stays the same.

File formats that store vector based images include: PDF, EPS, SVG and AI.  File formats 
that store pixel-based images are JPEG, PNG, TIFF, BMP and PSD.  PDF, EPS and AI can store 
embedded pixel information (hybrid images).

It is always possible to go from vector to pixel art, but it is not so easy to go the other
way.  Another advantage of vector art is that pixel text is not easily retrieved by a machine.

Pixel art is everywhere (photos, machine output), however if we have to create a completely
plot then there are a number of reasons to do so using vector graphics.  Vector art is covered 
in chapter 18 of the book.

========
Inkscape
========

Inkscape uses the SVG (Scalable Vector Graphics) format for its files. 
SVG is an open standard widely supported by graphic software.

.. toctree::
   :maxdepth: 1

   inkscape/InkscapeBasics
   inkscape/InkscapeTutorials

Uses
____

* Inkscape can import other formats (e.g. PNG or EPS) then convert.
* One could create a image in matplotlib (SVG,PDF etc) and import then annotate
* Resizing of images
* Adding text or shapes or colors to a bitmap

Additional Resources
____________________

* `The inkscape documentation <http://inkscape.org/doc/>`_
* `Nice set of tutorials <http://inkscapetutorials.wordpress.com>`_
* `Very nice gallery <http://www.techdrivein.com/2010/07/top-10-totally-amazing-wallpapers-made.html>`_ of wallpapers
* `Python effects tutorial <http://wiki.inkscape.org/wiki/index.php/PythonEffectTutorial>`_
