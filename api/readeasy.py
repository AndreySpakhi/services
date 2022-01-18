import base64
import httplib2
import json
import time

# Eaton EASY API description https://www.eaton.com/flash/eaton/json-api/Default.htm
# Your EASY E4 device URL here (IP + port, format: http://XXX.XXX.XXX.XXX:XX/)
URL = "http://123.123.123.123:12/"
# Your EASY E4 device API key here
APIKEY = "9656dd396654f9a8b15628518b2674a4e8e92db95715f46486f53280b8d17b36b1b57f45e88c8e5d"
permitted_reg_type = ("MB", "MW", "MD")


def request(pTarget):
    header = {'Authorization': "Bearer %s" % APIKEY}
    h = httplib2.Http()
    resp, content = h.request(URL + pTarget, method="GET", headers=header)
    return resp, content


def isRunning():
    r = False
    resp, content = request("api/get/data?elm=STATE")
    try:
        o = json.loads(content)
        r = (o["SYSINFO"]["STATE"]) == "RUN"
    except ValueError:
        print('JSON Decoding failed')
    return r


def readEasyMarker(pOp, pIndex, pVal):
    url = "api/get/data?elm=" + pOp + "(" + str(pIndex) + "," + str(pVal) + ")"
    return request(url)


def getEasyName():
    url = "api/get/data?elm=DEVNAME"
    return request(url)


def main():
    if not isRunning():
        resp, content = request("api/set/mode?op=state&v1=RUN")
        time.sleep(.300)
    resp, content = getEasyName()
    print(content)
    registers_type = ""
    while registers_type not in permitted_reg_type:
        registers_type = input("Enter registers type (MB, MW, MD): ")
    start_index = int(input("Enter start register: "))
    end_index = int(input("Enter end register: "))
    resp, content = readEasyMarker(registers_type, start_index, end_index)
    print(content)
    decoded_bytes = ["{:08b}".format(x) for x in base64.b64decode(content)]
    print(decoded_bytes)


if __name__ == '__main__':
    main()
