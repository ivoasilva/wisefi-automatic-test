import socket

host = "10.0.0.1"
port = 5001


class Socket:

    def __init__(self, ssid, voucher, time, unity):
        self.ssid = ssid
        self.voucher = voucher
        self.time = time

    def Socket_client(self):
        print("Send dates to server")
        print("SSID: ", self.ssid)
        print("Voucher: ", self.voucher)
        print("Time connection: ", self.time)
        date = {"SSID": self.ssid, "Voucher":self.voucher, "Time": self.time}
        print(date)
        '''
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soc.settimeout(5)
        soc.connect(host, port)
        soc.sendfile(date)
        response = soc.recv()
        soc.close()
        '''
        response = "test OK"
        return response