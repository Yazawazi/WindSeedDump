import sys
import json
import base64
import struct

def xor(message, key):
    return hex(message ^ key)

def log(level, message):
    print(f"[{level}]\t{message}")

def dump(jsonPath):
    try:
        config = json.load(open(jsonPath, "r"))["object"]
        data = config["areaNotify"]["areaCode"]
    except:
        sys.exit(1)
    

    if config["areaNotify"]["areaType"] != 1:
        print("I cannnot deal with type 2 or 3.")
    else:
        sys.exit(1)

    luac = base64.b64decode(data)

    if b"sb_1184180438" in luac:
        start = luac.find(0x38) + 14
        end = luac.rfind(0xA3)

        luac = luac[start:end + 1]

        with open("temp_dump.luac", "wb") as f:
            f.write(luac)

        file = open("temp_dump.luac", "rb")

        data = []
        while True:
            temp = file.read(1)
            if not temp:
                break
            else:
                if (ord(temp) <= 15):
                    data.append(("0x0" + hex(ord(temp))[2:])[2:])
                else:
                    data.append((hex(ord(temp))[2:]))

        data.reverse()

        for key, value in enumerate(data):
            if key == 0:
                pass
            else:
                data[key] = xor(int(value, 16), int(data[key - 1], 16))

        for key, value in enumerate(data):
            data[key] = xor(int(value, 16), 0xA3)

        data.reverse()

        with open("result.luac", "wb") as file:
            # No 0xFuck
            for item in data:
                pack = struct.pack("B", int(item, 16))
                file.write(pack)
        
    else:
        open("result.luac", "wb").write(luac)
    print("Done! result.luac")

def help():
    print("dump.py <json>")


if len(sys.argv) != 2:
    help()
else:
    dump(sys.argv[1])
