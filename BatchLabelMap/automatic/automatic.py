import os
import unittest
import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
import logging
import numpy as np
import math
import SimpleITK;
import pydicom;




from DICOMLib import DICOMUtils




from difflib import SequenceMatcher


pip_modules = ['pydicom'];
for module_ in pip_modules:
    try:
        module_obj = __import__(module_)
        logging.info("Module already imported");
    except ImportError:
        logging.info("{0} was not found.\n Attempting to install {0} . . ."
                     .format(module_))
        pip_main(['install', module_])





#
# automatic
#

class automatic(ScriptedLoadableModule):
  """Uses ScriptedLoadableModule base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def __init__(self, parent):
    ScriptedLoadableModule.__init__(self, parent)
    self.parent.title = "Batch Label Map" # TODO make this more human readable by adding spaces
    self.parent.categories = ["Custom Module"]
    self.parent.dependencies = []
    self.parent.contributors = ["Juan Perez (CWRU)"] # replace with "Firstname Lastname (Organization)"
    self.parent.helpText = """
This extension simply converts .stl files to .mha
"""
    self.parent.helpText += " \n Instructions found at: <a href = 'https://github.com/weras2/BatchLabelMap'>GitHub</a><br>\n"
    #self.parent.helpText += self.getDefaultModuleDocumentationLink()
    self.parent.acknowledgementText = """
This file was developed by Juan Perez. 
""" # replace with organization, grant and thanks.
    
#
# automaticWidget
#

class automaticWidget(ScriptedLoadableModuleWidget):
  """Uses ScriptedLoadableModuleWidget base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def setup(self):
    ScriptedLoadableModuleWidget.setup(self)

    # Instantiate and connect widgets ...

    #
    # Parameters Area
    #



    parametersCollapsibleButton = ctk.ctkCollapsibleButton()
    parametersCollapsibleButton.text = "Parameters"
    self.layout.addWidget(parametersCollapsibleButton)

    # Layout within the dummy collapsible button
    parametersFormLayout = qt.QFormLayout(parametersCollapsibleButton)

    # Toggle button
    self.toggleBtn1 = qt.QCheckBox("Patient Set");
    parametersFormLayout.addRow(self.toggleBtn1);


    # input volume selector
    self.button1 = qt.QPushButton("Select Patient Folder")
    parametersFormLayout.addRow("Folder Button: ",self.button1);
    
    someVar = "";
    self.button1.connect('clicked(bool)', self.someCoolFunction);
    self.e6 = qt.QLineEdit("No Folder Selected");
    self.e6.setReadOnly(True)
    parametersFormLayout.addRow("Slected Folder",self.e6)


    #Convert
    self.convertButton = qt.QPushButton("Convert")
    self.convertButton.enabled = True
    parametersFormLayout.addRow(self.convertButton)


    # connections
    self.convertButton.connect('clicked(bool)',self.onConvert)
    self.toggleBtn1.stateChanged.connect(self.changeText);

    # Add vertical spacer
    self.layout.addStretch(1)


  def cleanup(self):
    pass


  def changeText(self):
      if (self.toggleBtn1.isChecked()):
        self.button1.setText("Select Patient Set");
      else:
          self.button1.setText("Select Patient Folder");
  

   # What drives the entire process
  def onConvert(self):
      main = coreFunction();
      if(self.toggleBtn1.isChecked()):
          main.setMode(self.e6.text);
      else: 
        main.start(self.e6.text);


  def someCoolFunction(self):
    someVar = qt.QFileDialog.getExistingDirectory(None, "Select Directory");
    self.e6.setText(someVar);






class coreFunction():

   
    def openVolume(self,path,volumeFile,dicomID,imgSize,imgSpacing,db):
        
        #Important Variables:
        outputDir = path;


        outputVolumeLabelValue = 100
        outputVolumeSpacingMm = imgSpacing;
        #outputVolumeMarginMm = [10.0, 10.0, 10.0]
        imageSize = imgSize;

        #Temporary
        dicomNodeID = dicomID[0];


        #This used to be necessary
        #matrix = vtk.vtkMatrix4x4();
        #matrix.DeepCopy((-1, 0, 0, 0,
        #                  0, -1, 0, 0,
        #                  0, 0, 1, 0,
        #                  0, 0, 0, 1));

        #Load model
        someModel = slicer.util.loadModel(path + "/" + volumeFile);
        #Fetch Node
        name = someModel.GetName();
        print(name);
        modelNode = slicer.util.getNode(str(name));
        #Transform Node
        #transformNode = slicer.vtkMRMLTransformNode();
        #slicer.mrmlScene.AddNode(transformNode);
        #modelNode.SetAndObserveTransformNodeID(transformNode.GetID());
        #transformNode.SetMatrixTransformToParent(matrix);


        inputModel = modelNode;

        bounds = np.zeros(6)
        inputModel.GetBounds(bounds)
        imageData = vtk.vtkImageData()

        imageData.SetDimensions(imageSize)
        imageData.AllocateScalars(vtk.VTK_UNSIGNED_CHAR, 1)
        imageData.GetPointData().GetScalars().Fill(0)

        #This will be our dicom file
        #referenceVolumeNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode")
        shNode = slicer.mrmlScene.GetSubjectHierarchyNode();
        #itemID = shNode.GetItemByUID(slicer.vtkMRMLSubjectHierarchyConstants.GetDICOMUIDName(), str(dicomID));
        referenceVolumeNode = slicer.mrmlScene.GetNodeByID(str(dicomNodeID));



        


        #referenceVolumeNode.SetOrigin(imageOrigin)
        #referenceVolumeNode.SetSpacing(outputVolumeSpacingMm)
        #referenceVolumeNode.SetAndObserveImageData(imageData)
        #referenceVolumeNode.CreateDefaultDisplayNodes()

        
        seg = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLSegmentationNode')
        seg.SetReferenceImageGeometryParameterFromVolumeNode(referenceVolumeNode)
        slicer.modules.segmentations.logic().ImportModelToSegmentationNode(inputModel, seg)
        seg.CreateBinaryLabelmapRepresentation()
        outputLabelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLabelMapVolumeNode')
        slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(seg, outputLabelmapVolumeNode, referenceVolumeNode)






        print("exporting")
        #segmentId = seg.GetSegmentation().GetSegmentIdBySegmentName(inputModel.GetName());
        #image = slicer.vtkOrientedImageData()
        #seg.GetBinaryLabelmapRepresentation(segmentId,image);
        #image.save(outputDir + '/' + 'test_bruh.mha')
        someNode = outputLabelmapVolumeNode.CreateDefaultStorageNode();
        someNode.SetFileName(outputDir + '/' + name + '-label.mha');
        someNode.WriteData(outputLabelmapVolumeNode);

        




        # Delete Modules
        slicer.mrmlScene.RemoveNode(modelNode);
        slicer.mrmlScene.RemoveNode(referenceVolumeNode);
        slicer.mrmlScene.RemoveNode(outputLabelmapVolumeNode);
        slicer.mrmlScene.RemoveNode(seg);


        slicer.mrmlScene.GetSubjectHierarchyNode().RemoveAllItems();

        #DICOMUtils.deleteTemporaryDatabase(slicer.dicomDatabase, cleanup=True)

        # TODO Memory Management
        someNode.UnRegister();





               
        return;


        #for file in volumeFiles:
         #   loadedModelNode = slicer.util.loadModel(path + "\\" + file);


    def fetch(self,folder,selector):
        tmpArr = [];
        print("Fetching contents in folder: " + folder );
        for file in os.listdir(folder):
            if file.endswith(".stl"):
                tmpArr.append(file)

        print("Found files: " )
        for stlFile in tmpArr:
            print(stlFile);
        
        # Clear selector in case user jumped to another file!
        selector.clear();
        selector.addItem("None");
        selector.addItems(tmpArr);

        #self.openVolumes(folder,tmpArr);

    def setMode(self,setDir):
        patientFolders = os.listdir(setDir);
        for folder in patientFolders:
            wDir = setDir + "\\" + folder;
            self.start(wDir);




    def start(self,wDir):


        folderPath = wDir;
                
        # Let's get everything in the folder:
        patientFolder = os.listdir(folderPath);

        # Let's isolate the STL's and the folders
        volumes = [];
        folders = [];

        for item in patientFolder:
            if item[-3:] == "stl":
                volumes.append(item)

            elif  item.find(".") == -1:
                folders.append(item);


        # Now let's pair each file with a folder
        correctFolder = "";
        for volume in volumes: 
            # Blind assumption
            highestScore = SequenceMatcher(None, volume, folders[0]).ratio();
            for folder in folders:
                score = SequenceMatcher(None, volume, folder).ratio();
                correctFolder = folders[0];
                if score > highestScore:
                    highestScore = score;
                    correctFolder = folder;
            # Use this for debug
            #print("Volume: " + volume + " goes with: " + correctFolder);

            #Now that we have the folder, let's try to get the correct dicom path 
            scanPath = os.listdir(folderPath + "\\" + correctFolder);
            if(len(scanPath) > 0):
                sequencePath = folderPath + "\\" + correctFolder + "\\" + scanPath[0];
                
                # Below we would execute!
                PathDicom = sequencePath;

                loadedNodeID = 0;
                dbRef = 0;
                with DICOMUtils.TemporaryDICOMDatabase() as db:
                    DICOMUtils.importDicom(PathDicom, db);
                    patientUIDs = db.patients();
                    for patientUID in patientUIDs:
                        loadedNodeID = DICOMUtils.loadPatientByUID(patientUID);

                    #DICOMUtils.deleteTemporaryDatabase(db, cleanup=True);




                lstFilesDCM = []  # create an empty list
                for dirName, subdirList, fileList in os.walk(PathDicom):
                    for filename in fileList:
                        if ".dcm" in filename.lower():  # check whether the file's DICOM
                            lstFilesDCM.append(os.path.join(dirName,filename))

                # Get ref file

            	#We get the last file to get the origin easily
                RefDs = pydicom.read_file(lstFilesDCM[len(lstFilesDCM) - 1]); 
               
                #Get image position CHANGE THIS!
                imagePos = RefDs.ImagePositionPatient;


                # Load dimensions based on the number of rows, columns, and slices (along the Z axis)
                ConstPixelDims = [int(RefDs.Rows), int(RefDs.Columns), len(lstFilesDCM)]

                # Load spacing values (in mm)
                ConstPixelSpacing = [float(RefDs.PixelSpacing[0]), float(RefDs.PixelSpacing[1]), float(RefDs.SliceThickness)]



                #Do the whole volume thing
                self.openVolume(wDir,volume,loadedNodeID,ConstPixelDims,ConstPixelSpacing,dbRef);




        





