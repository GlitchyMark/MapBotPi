import sensor, image, time, pyb

thresholds = [(30, 100, 30, 80, -10, 46),
              (30, 100, -21, -3, -56, -14),
              (30, 100, -23, 22, 27, 61),
              (30, 100, -58, -23, -3, 47)]
led = pyb.LED(3)

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
printStatus = True

blob_color_lookup = {
    1 << 0  :   "RED",
    1 << 1  :   "BLUE",
    1 << 2  :   "YELLOW",
    1 << 3  :   "GREEN"
}

def detectAllColours(img):
    blobs = img.find_blobs(thresholds, pixels_threshold=300, area_threshold=300, roi=[0, 66, 321, 175])
    if not blobs:
        print( str({"pole" : False}) )
    for blob in blobs:
        img.draw_rectangle(blob.rect())
        img.draw_cross(blob.cx(), blob.cy())

        x, y, width, height = blob.rect()
        dist = (3529.5)/height
        distX = centerX - blob.cx()
        aa_divisor = 1 if distX > 0 else 2
        actual_angle = (distX / (img.width() / aa_divisor)) * angleOfConcern
        
        params = {
            "color"     :   blob_color_lookup.get(blob.code()),
            "angle"     :   actual_angle,
            "distance"  :   dist
        }
        print(params)

while(True):
    led.off()
    clock.tick()
    img = sensor.snapshot()
    centerX = int(img.width()/2)
    centerPoint = int(img.width()/2),int(img.height()/2)
    #img.draw_rectangle(int(320/2),int(240/2),5,5)
    detectAllColours(img)
