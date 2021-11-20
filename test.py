from Yeelight import * 
from yeelight import Bulb
import time

class Test(object):
    def __init__(self):
        self.Service = Yeelight()
        self.Service.SetDevice("192.168.0.8", "Bed bulb", 1)
        self.Service.SetDevice("192.168.0.9", "Kitchen bulb", 2)

    def test(self):
        sleepTime = 4
        self.Service.GetProperties()
        
        while True:
            self.Service.TurnOnEverything()
            time.sleep(sleepTime)

            self.Service.WhiteAll()
            time.sleep(sleepTime)
            
            self.Service.SetBrightness(id = 2, brightness = 100)
            self.Service.SetBrightness(id = 1, brightness = 100)
            time.sleep(sleepTime)
            
            self.Service.SetBrightnessEverything(20)
            time.sleep(sleepTime)
            
            self.Service.SetBrightness(100, id = 1)
            self.Service.SetBrightness(100, id = 2)
            time.sleep(sleepTime)

            self.Service.StartFlow(1)
            time.sleep(sleepTime)
            
            self.Service.TurnOff(id = 1)
            self.Service.TurnOff(id = 2)
            time.sleep(sleepTime)

            self.Service.ToogleEverything()
            time.sleep(sleepTime)

            self.Service.SetColorByRgb([12, 12, 12], id = 1)
            self.Service.SetColorByRgb([100, 50,30], id = 2)
            time.sleep(sleepTime)

            self.Service.StartFlow(flowId = 3, id = 2)
            self.Service.StartFlow(flowId = 3, id = 1)
            time.sleep(sleepTime)
            
            self.Service.StartFlow(flowId = 5, id = 2)
            self.Service.StartFlow(flowId = 5, id = 1)
            time.sleep(sleepTime)

            self.Service.StopFlowEverything()
            time.sleep(sleepTime)

            self.Service.SetColorByCustomName('red', id = 1)
            self.Service.SetColorByCustomName('red', id = 2)
            time.sleep(sleepTime)

            self.Service.SetColorByCustomName('blue', id = 1)
            self.Service.SetColorByCustomName('blue', id = 2)
            time.sleep(sleepTime)

Test().test()