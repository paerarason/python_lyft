from serverlet import serverlet
class Car(serverlet):
    def __init__(self, ngine, battery):
        self.ngine = ngine
        self.battery = battery
    def needs_service(self):    
        return self.ngine.needs_service() or self.battery.needs_service()