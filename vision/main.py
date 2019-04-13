import sensor, image, time,pyb
thresholds = [(30, 100, 30, 80, -10, 46),
              (30, 100, -21, -3, -56, -14),
              (30, 100, -23, 22, 27, 61),
              (30, 100, -58, -23, -3, 47)]

red_led = pyb.LED(1)
green_led = pyb.LED(2)
blue_led = pyb.LED(3)
ir_leds = pyb.LED(4)


sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 300)
sensor.set_brightness(-1)
sensor.set_saturation(0)
sensor.set_contrast(0)
sensor.set_auto_gain(False)
sensor.set_auto_whitebal(False)
angleOfConcern = 35.4
clock = time.clock()
printStatus = True;
def detectAllColours(img):
    for blob in img.find_blobs(thresholds, pixels_threshold=300, area_threshold=300,roi = [0,66,321,175]):

        if blob.code() == 1:
            red_led.on()
            img.draw_rectangle(blob.rect())
            img.draw_cross(blob.cx(), blob.cy())
            x,y,width,height =blob.rect()
            dist = (3529.5)/height
            redDistX = centerX - blob.cx()
            if redDistX < 0:
                ActualAngle = (redDistX/(img.width())/2) * angleOfConcern
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
            img.draw_rectangle(blob.rect())
            img.draw_cross(blob.cx(), blob.cy())
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
            img.draw_rectangle(blob.rect())
            img.draw_cross(blob.cx(), blob.cy())
            x,y,width,height =blob.rect()
            dist = (3529.5)/height
            yellowDistX = centerX - blob.cx()
            if yellowDistX < 0:
                ActualAngle = (yellowDistX/(img.width()/2)) * angleOfConcern
                if(printStatus):
                    yellowStat = {"Yellow_Pole_Angle":ActualAngle,"Yellow_Pole_Distance":dist}
                    print(yellowStat)

            if yellowDistX > 0:
                ActualAngle = (yellowDistX/img.width()) * angleOfConcern
                if(printStatus):
                    yellowStat = {"Yellow_Pole_Angle":ActualAngle,"Yellow_Pole_Distance":dist}
                    print(yellowStat)


        if blob.code() == 8:
           img.draw_rectangle(blob.rect())
           img.draw_cross(blob.cx(), blob.cy())
           x,y,width,height =blob.rect()
           dist = (3529.5)/height
           greenDistX = centerX - blob.cx()
           if greenDistX < 0:
               ActualAngle = (greenDistX/(img.width()/2)) * angleOfConcern
               if(printStatus):
                   greenStat = {"angle":ActualAngle,"distance":dist,"color":"GREEN"}
                   print(greenStat)

           if greenDistX > 0:
               ActualAngle = (greenDistX/img.width()) * angleOfConcern
               if(printStatus):
                   greenStat = {"angle":ActualAngle,"distance":dist,"color":"GREEN"}
                   print(greenStat)





while(True):
    clock.tick()
    img = sensor.snapshot()
    centerX = int(img.width()/2)
    centerPoint = int(img.width()/2),int(img.height()/2)
    img.draw_rectangle(int(320/2),int(240/2),5,5)
    detectAllColours(img)
