# Introducing Semicon

## An **open source** desktop application focusing on calculating the total deposition of dopants on a semiconductor material

**Features**,
### Most semiconductor devices are fabricated by the introduction of dopant impurities inside the material to modify its electrical properties. The act of introducing those impurities is called doping. Common doping methods (ion implantation and diffusion-based methods) can cause a plethora of issues related to safety, crystal lattice damage and cost, especially for the realization of nanoscale architectures.

### Molecular Doping (MD) has been introduced as a low-cost alternative to conventional doping methods. The technique consists of the self-assembling of dopant-containing precursor molecules from the liquid phase on samples to be doped (so-called “dip-coating”), followed by a heat treatment to drive the impurity inside the material. In this project, you will get microscopy image data for the morphological evolution of a molecule (Diethyl-Propyl-Phosphonate (DPP)) deposition (by dip-coating) onto a silicon (Si) waver, tracking the layer formation over time, at several solution concentrations.

### Using image processing library to automatically determine the surface coverage (how much surface area (in %)) is covered by the DPP molecules. To strengthen results, mitigate over all pictures provided for each test case (percentage, deposition time), and create error bars (median, mean, standard deviation) for each “measurements”. Plot resulting data in a joint graph, showing surface coverage [%] over deposition time.

> By uploading the microscopinc images and specifying the incubation cycle, the application calculates the necessary parameter and the user is able to fuse the parameters to inbuilt fuctionswhich acts as the plugin.

![Semicon-Basic-BD](https://user-images.githubusercontent.com/65939087/226215919-b5d47188-bfab-46de-a329-3cd6a86d14f8.png)

> Current version features will be updated regularly on the release log.

> The next version development focuses on live feeding of from microscopic video files in claculating the parameters
with more optimization techniques.

**Splash Page**

![Semicon-splash](https://user-images.githubusercontent.com/65939087/226215971-604df9c2-86e3-423c-ad47-2ff6f86e66ff.png)

### The user is welcomed by a splash screen detailing on the current version of the application which starts clicking on the application icon. As mentioned above Semicon is an open source less load with high optimization algorithm tool which doesn't take any user data or doesn't require any license or uneccessary sign up.

**Landing Page**

![semicon-home](https://user-images.githubusercontent.com/65939087/226215991-7420f76e-d5a4-4cee-beb5-a851aa901bd1.png)

### The user is then guided to a home page after 3 seconds where two options are given for continuing the application. If the user has previous image files of the wafer for each incubation period the upload features dierctly seeks on the file from the user dierctory. Mutliple files with supported image files (.png, .jpg, .jpeg, .tif, .tiff) can be uploaded for examining on the Semicon. A scaling paramter is set for the image in order to fit the image inside the canvas.

### The user is also provided with a provison to get the results realtime over the application by using a live cam feed. The data provided is optimized by entering the supported camera used for examining which helps Semicon in providing a variance value in obtaining the actual data through the alogoithm.

**Canvas Page**

![semicon-canvas-1](https://user-images.githubusercontent.com/65939087/226215997-618d03d8-2b59-4c27-affc-89edc608011d.png)

### The Canvas is the main page where the user gives on the value for calculating the total optimization of the wafers by adjusing values and adding filters to the uploaded image or the live feed. On the left side of the page a  navigation rail of importants options are provided,

> Filter: This is the intial selection which helps the user in regulating values for processing the image for calculating the surface coverage area.
> Adjust: This is a preprocessing tool, where the user can use this to mark down a large image fileby dragging the portion or zooming in the portion which the user wants to concentrate. This tool comes in hand during the live feed of the semiconductor wafer, where the user can COVER or tight fit the feed from camera.
> Docs: Basic help not on how to use Semicon apllication.

-------

![semicon-canvas2](https://user-images.githubusercontent.com/65939087/226215999-45878b5f-e97e-4cc3-a8ee-09fb417ac648.png)

### The right side of the page contains the operations. Four tabs which highlights the main functionality of the application according to the options selected from throgh the navigation rail. The ADJUST and FILTER options just changes on the process part but remians the same for the rest of the tabs. When using the live feed The first tab changes to Camera settings where the user can adjst the basic parameters regulating the focus of the sensor. In the future versions, the list of supported cameras will be added an also a .cpf (camera parameter file) which is typically a XML file which carries all the general parameters for the camera being used for the live feed. 

### In the future, the user will be able to make their own XML formatted .cpf provided with a specific syntax or order in adding the parameters. The user can regulate the values for threholding, median filter (supported filtering method in Semicon) and  incubation period. Finally, an output as a graph can be obtained if the OPTIMIZED_PLOT option is turned on. A subplot graph with error bars and histogram will be generated which gives a clear cut idea on the process carried out through Semicon.

--------

![semicon-canvas-3](https://user-images.githubusercontent.com/65939087/226216057-62d2cbb1-e2a8-4f36-a1f6-794e3fa9f88f.png)

### After regulating the values for the processing part, the user can now add methods for optimization focusing on any linear and non-linear function. With the Semicon application, the Avrami function is coming as an addon and if the user wishes to use the calculated values with other optimization methods, they can add the same as an XML file with certian order of variables to be used. Then that XML needs to be added to the application by clicking on the ADD_METHOD button. Once the method is added to the list of ANALYSIS tab, click on ACTIVATE.

![semicon-canvas-4](https://user-images.githubusercontent.com/65939087/226216064-8f6b2bd2-f995-4fa1-ab2c-42df2e80ca5c.png)

### Once activated, the necessary labels and data are found in the MATHS tab, where the user can even regulate the values and work out on the optimization part. Finally, they're able to save the method, and Semicon binds up the whole data into zip file which includes the method, plots and log files.

> Note: By changing the processing values in the MATHS tab, doesn't make any make changes in the PROCESS tab. You have to make the same under the PROCESS tab if any changes needed which in turn deactivates the optimization method activated which will be sorted out in the future updates.

![semicon-canvas-5](https://user-images.githubusercontent.com/65939087/226216071-69affdfb-fe39-4594-bf88-9a355b88dbaf.png)

### In the top portion, an app bar with a pop button is there to help on adding, saving, exporting new files and also completing exiting the app. Future updates will make on with application update and method package addition features.

> Note: Current version doesn't support autosave or window close events.

Credits to - SDU_Sonderborg, Matplotlib, Scipy, Python, Flet, Pyswarm.

