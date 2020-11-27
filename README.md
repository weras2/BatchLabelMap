<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->


<!-- PROJECT LOGO -->
<br />
<p align="center">
    <img src="Graphics/3D-Slicer-Mark.png" alt="Slicer3D Logo" width="80" height="80">

  <h3 align="center">Batch Label Map</h3>

  <p align="center">
    A Slicer3D extension to facilitate label map conversions
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Conversions from volume to label map can be tedious and time consuming. This module speeds things up by automating things.



<!-- GETTING STARTED -->
## Getting Started

Below is a detailed example on how to get the module running on Slicer3D. Note: This module has only been tested on the Slicer3D version 4.11.20200930 revision 29402 built 2020-10-02, so errors may be present if using a suffiently old Slicer3D version. 

### Installation

Make sure to be connected to the internet so that one of the dependencies can be downloaded.

1. Download the file BatchLabelMap or clone repo 
2. Launch Slicer3D **as administrator.** Note: This is only for the first time.
3. In Slicer3D, open the **Extension Wizard** module. This can be done by clicking on the magnifying glass and searching for the module by typing the name out. 
4. In the Extension Wizard module, click on **Select Extension.** A new window should open.
5. Navigate to where you downloaded the folder **BatchLabelMap.**
6. Finally, click on it **once** and then click on the button **Select Folder.**

If there weren't any problems, the module can be found at **Custom Modules >> Batch Label Map** or you can just use the search method as suggested in step 3


<!-- USAGE EXAMPLES -->
## Usage

The program expects that patient folders are filled with two things, volumme files (.STL) & reference MRI scans. Volume files and matching MRI folder names must have similar, though not exact, names


[![Product View][getting-started-example]](https://raw.githubusercontent.com/weras2/BatchLabelMap/main/Graphics/res1.jpg)

Based on the image above there are just three clickable items. 

1. **Patient Set CheckBox:** Let's the program know that the directory that will be selected is a collection of patients rather than just one patient. By default is not checked, meaning that the program expects a patient directory, not a set.
2. **Select Folder Button:** Opens a Folder Dialog Window. The program expects that the directory given is parent to all patient files. Example for the default case. 
    ```
    John Doe -> MRI Scan Folder 
             -> Volume Files
    ```
             
     Here one would select the folder John Doe. In the case that **Patient Set Checkbox** is selected:
     
     ```
     Patient Set -> John Doe    -> MRI Scan Folder 
                                -> Volume Files 
                                ------- 
                 -> Mary Jane   -> MRI Scan Folder 
                                -> Volume Files
    ```
                                
    Here one would select the folder Patient Set.
    
3. **Convert Button:** This runs the script. All output label maps will be output in the appropriate patient folder and will be labeled according to its volume name with '-label' appended at the end. 
    
    
                                
                 



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/weras2/BatchLabelMap/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Currently not licensed. 



<!-- CONTACT -->
## Contact

Juan Perez - minego410@gmail.com

Project Link: [https://github.com/weras2/BatchLabelMap](https://github.com/weras2/BatchLabelMap)




<!-- MARKDOWN LINKS & IMAGES -->
[getting-started-example]: Graphics/res1.jpg







