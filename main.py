from socketserver import BaseRequestHandler, TCPServer
import os


class EchoHandler(BaseRequestHandler):
    def handle(self):
        print("Got connection from", self.client_address)
        with open(f"./received.ps", "wb+") as f:
            f.write(b"")
        while True:
            msg = self.request.recv(8192)
            with open(f"./received.ps", "ab+") as f:
                f.write(msg)
            if not msg:
                print("Received .ps file, Converting to .pdf >>>>")
                os.system("ps2pdf received.ps")
                print("Done!")
                break


if __name__ == "__main__":
    serv = TCPServer(("", 9100), EchoHandler)
    serv.serve_forever()
