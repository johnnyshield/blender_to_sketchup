# Blender addons

## Batch export Blender to Collada
This addon allows you to export all objects in a Blender file to separate Collada DAE files.

### Credits
The code is not mine, so I have left the original author - [Patrick Jezek](https://github.com/pjezek/blender/tree/master/unity_tools) - attributed. All I have done is modified a much more capable addon to *only* do bulk DAE export, and then update it to work for Blender 2.80.

### Why I created this
Sketchup is awesome, importing from CAD to Sketchup can be a pain.

STL files are the most commonly exported file type from parametric CAD (e.g. SolidWorks), unfortunately Sketchup's STL importer is flaky for complex models, so an intermediate step of converting STL to Collada (DAE) is necessary if you want to avoid buying a plugin.

STL files also are normally exported as a single object from CAD programs, so they need to be split by geometry, then saved to separate collada files.

I am aware of two free options for doing this:
1. [Meshlab](http://www.meshlab.net/)
  * Split by geometry easily (right click on mesh at top right, split in connected components)
  * Unfortunately there isn't a method to bulk export all objects after splitting
2. [Blender](https://www.blender.org/)
  * Select the object (click), go into Edit mode (Tab), then press P, then select "By Loose Parts".
  * Bulk export all components with this addon

Batch import of the Collada files is then done via TIG's Sketchup addon [Import all from folder](https://sketchucation.com/forums/viewtopic.php?p=331966#p331966)

Note: I don't know of a method of saving a single collada file with multiple objects

## Installing and using the addon (2.80)
If you're new to Blender, download the .py addon file, then to install go to Edit, Preferences

![menu](https://github.com/johnnyshield/blender/blob/master/Screenshots%202.80/blender_JpYis0gGol.png)

Click install, then select the file. Click the checkbox to enable it.

![addon](https://github.com/johnnyshield/blender/blob/master/Screenshots%202.80/blender_YfaOx0NNIv.png)

The toolbar (UI) is hidden by default so click here to expand it

![ui](https://github.com/johnnyshield/blender/blob/master/Screenshots%202.80/blender_qKyExim98w.png)

Collada exporter will show up down the bottom of the tool bars, save the blender file and select your export folder before clicking export.

![how to use](https://github.com/johnnyshield/blender/blob/master/Screenshots%202.80/blender_yQxya9pH1I.png)
