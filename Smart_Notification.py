class Notification:
    def send_alert(self,message,user=None):
        if user!=None:
            print(f"Alert for: {user}:{message}")
        else:
            print(f"General Alert:{message}")


alert= Notification()
alert.send_alert("Your PC Has Some Major Damages,Please make sure to fix your device","@Arhamgamer218")
alert.send_alert("Your PC Has Some Major Damages,Please make sure to fix your device")
