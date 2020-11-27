cmake_minimum_required(VERSION 3.5)

project(BatchLabelMap)

#-----------------------------------------------------------------------------
# Extension meta-information
set(EXTENSION_HOMEPAGE "http://slicer.org/slicerWiki/index.php/Documentation/Nightly/Extensions/BatchLabelMap")
set(EXTENSION_CATEGORY "Custom")
set(EXTENSION_CONTRIBUTORS "Juan Perez (CWRU), ")
set(EXTENSION_DESCRIPTION "This is an example of a simple extension")
set(EXTENSION_ICONURL "http://www.example.com/Slicer/Extensions/BatchLabelMap.png")
set(EXTENSION_SCREENSHOTURLS "http://www.example.com/Slicer/Extensions/BatchLabelMap/Screenshots/1.png")
set(EXTENSION_DEPENDS "NA") # Specified as a space separated string, a list or 'NA' if any

#-----------------------------------------------------------------------------
# Extension dependencies
find_package(Slicer REQUIRED)
include(${Slicer_USE_FILE})

#-----------------------------------------------------------------------------
# Extension modules
add_subdirectory(automatic)
## NEXT_MODULE

#-----------------------------------------------------------------------------
include(${Slicer_EXTENSION_GENERATE_CONFIG})
include(${Slicer_EXTENSION_CPACK})
