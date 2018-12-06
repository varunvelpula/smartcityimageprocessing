# Smart city image processing
The image processing module for the purpose of localization of autonomous ground vehicles for the Theory of Sensors and Actuators Project (April 2018)
The Files:
1. calibration.py
2. path_planning.py

## Background

This repository is in reference to the image processing module developed in April 2018for the Smart City course project for Theory of Sensors and Actuators. A overhead camera module setup was developed for the purpose of localizing the positions of the buildings and the vehicles on the smart city.

## calibration.py

This code first initilizes the position of nodes (positions of buildings) on the smart city through the detection of Aruco markers and returns the centroid positions of the suitably placed markers to the main function.
  
## path_planning.py

This code aims to *localize* the Autonomous Ground Vehicles (AGVs) which have Aruco markers of size 7x7 cm placed on them with respect to the nodes. All the localizations of nodes and the AGVs are with respect to the image frame, i.e., in terms of pixel values. The position of all the AGVs are returned to the main function.
