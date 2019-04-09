import sensor, image, time,pyb
thresholds = [(30, 100, 30, 80, -10, 46),
              (30, 100, -21, -3, -56, -14),
              (30, 100, -23, 22, 27, 61)]
led = pyb.LED(3)
usb = pyb.USB_VCP()
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)
sensor.set_brightness(0)
sensor.set_saturation(0)
sensor.set_contrast(0)
sensor.set_auto_gain(False)
sensor.set_auto_whitebal(False)
angleOfConcern = 35.4
clock = time.clock()
printStatus = True;
def detectAllColours(img):
    for blob in img.find_blobs(thresholds, pixels_threshold=300, area_threshold=300):
        img.draw_rectangle(blob.rect())
        img.draw_cross(blob.cx(), blob.cy())
        if blob.code() == 1:
            x,y,width,height =blob.rect()
            dist = (3529.5)/height
            redDistX = centerX - blob.cx()
            if redDistX < 0:
                ActualAngle = (redDistX/img.width()) * angleOfConcern
                if(printStatus):
                    redStat = {"Red_Pole_Angle":ActualAngle,"Red_Pole_Distance":dist}
                    print(redStat)
                    #print("Actual angle red: " + str(ActualAngle))
                    #print("Red Distance: " + str(dist))

            if redDistX > 0:
                ActualAngle = (redDistX/(img.width()/2)) * angleOfConcern
                if(printStatus):
                    redStat = {"Red_Pole_Angle":ActualAngle,"Red_Pole_Distance":dist}
                    print(redStat)
                    #print("Actual angle red: " + str(ActualAngle))
                    #print("Red Distance: " + str(dist))
        if blob.code() == 2:
            x,y,width,height =blob.rect()
            dist = (3529.5)/height
            blueDistX = centerX - blob.cx()
            if blueDistX < 0:
                ActualAngle = (blueDistX/(img.width()/2)) * angleOfConcern
                if(printStatus):
                    blueStat = {"Blue_Pole_Angle":ActualAngle,"Blue_Pole_Distance":dist}
                    print(blueStat)
                    #print("Actual angle blue: " + str(ActualAngle))
                    #print("Blue Distance: " + str(dist))
            if blueDistX > 0:
                ActualAngle = (blueDistX/img.width()) * angleOfConcern
                if(printStatus):
                    blueStat = {"Blue_Pole_Angle":ActualAngle,"Blue_Pole_Distance":dist}
                    print(blueStat)
                    #print("Actual angle blue: " + str(ActualAngle))
                    #print("Blue Distance: " + str(dist))
        if blob.code() == 4:
            x,y,width,height =blob.rect()
            dist = (3529.5)/height
            yellowDistX = centerX - blob.cx()
            if yellowDistX < 0:
                ActualAngle = (yellowDistX/(img.width()/2)) * angleOfConcern
                if(printStatus):
                    yellowStat = {"Yellow_Pole_Angle":ActualAngle,"Yellow_Pole_Distance":dist}
                    print(yellowStat)
                    #print("Yellow_Angle: " + str(ActualAngle))
                    #print("Yellow_Distance: " + str(dist))
            if yellowDistX > 0:
                ActualAngle = (yellowDistX/img.width()) * angleOfConcern
                if(printStatus):
                    yellowStat = {"Yellow_Pole_Angle":ActualAngle,"Yellow_Pole_Distance":dist}
                    print(yellowStat)
                    #print("Yellow_Angle: " + str(ActualAngle))
                    #print("Yellow_Distance: " + str(dist))

while(True):
    led.off()
    clock.tick()
    img = sensor.snapshot()
    centerX = int(img.width()/2)
    centerPoint = int(img.width()/2),int(img.height()/2)
    img.draw_rectangle(int(320/2),int(240/2),5,5)
    detectAllColours(img)
