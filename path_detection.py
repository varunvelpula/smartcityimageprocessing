#EDGE ID DETECTION
# the image processing function
#code to generate the centroid of nodes marked by aruco markers
def imageprocessing():
    #Obtaining video feed from camera 
    cap = cv2.VideoCapture(0)

    #creating array of node centroids
    bot_centroid_array = np.zeros((3,2))
    bot_edge_array = np.zeros((3))
    for m in range(0,5):
         
        # Capture frame-by-frame
        ret, frame = cap.read()
        #print(frame.shape) #480x640
        # Our operations on the frame come here
        if ret is True:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        else:
            continue
        aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
        parameters =  aruco.DetectorParameters_create()
    

        '''    detectMarkers(...)
            detectMarkers(image, dictionary[, corners[, ids[, parameters[, rejectedI
            mgPoints]]]]) -> corners, ids, rejectedImgPoints
        '''
            
        #lists of ids and the corners beloning to each id
        corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
        
        # converting to numpy array 
        arr_full = np.array(corners)
        
        # resizing the array to required dimensions
        corners_array = np.resize(arr_full,(len(corners),4,2))

        # initializing node array to zero to store corner values
        edge_array = np.zeros((12,4,2))
        path_list = ((1,2),(2,3),(3,4),(1,4),(1,5),(2,6),(3,7),(4,8),(5,6),(6,7),(7,8),(1,8))
        path_bot = ((0,0),(0,0),(0,0))              
        # Caliberated node centroid values. Needs to be caliberated whenever the posistion of camera is drastically altered
        edge_centroid_array = np.load('calibrate.npy')
        
#       To obtain the center of the bots
        for i in range(0,3):
            
            x_sum = 0
            y_sum = 0
                
            for j in range(0,4):
                x_sum = x_sum + bot_array[i][j][0]
                y_sum = y_sum + bot_array[i][j][1]
                j = j+1

            #To store previous centroid values if node is not detected 
            if x_sum != 0 and y_sum != 0:
                bot_centroid_array[i][0] = x_sum/4
                bot_centroid_array[i][1] = y_sum/4
                
        # Loop to find whether the bot is on the edge or not        
        for i in range(0,3):

            xb = bot_centroid_array[i][0]
            yb = bot_centroid_array[i][1]
                
            for j in range(0,12):
                xn = edge_centroid_array[j][0]
                yn = edge_centroid_array[j][1]
                r = np.sqrt((xn-xb)**2 + (yn-yb)**2)
                if r < 40:
                    bot_node_array[i] = j+1
                    path_bot[i] = path_list[j]
            
        
        print(edge_centroid_array)
        print('-----------------------------------------')
        print(bot_centroid_array)
        print('-----------------------------------------')
        print(bot_node_array)
        print('-_-_-_-_-_-_-_','\n\n\n')
        
        #Printing distance between 5 and 6 
        gray = aruco.drawDetectedMarkers(gray, corners,ids)

        #To end camera feed 
        cv2.imshow('frame',gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    return(bot_node_array,path)