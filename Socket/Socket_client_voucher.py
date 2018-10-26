import socket
import json
import threading
host = "10.0.0.222"
port = 5002


class Socket:

    def __init__(self, ssid, voucher, time, code):
        self.ssid = ssid
        self.voucher = voucher
        self.time = time
        self.code = code

    def Socket_client(self):
        print("Send dates to server")
        print("SSID: ", self.ssid)
        print("Voucher: ", self.voucher)
        print("Time connection: ", self.time)
        date = ({"code": self.code, "ssid": self.ssid, "voucher": 270766, "time": self.time})
        print(date)

        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soc.settimeout(5)
        threading._start_new_thread=soc.connect((host, port))
        soc.send(json.dumps(date).encode('utf-8'))
        response = soc.recv(1024)
        soc.close()

        response = "test OK"
        return response