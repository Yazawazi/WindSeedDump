import os
import sys
import json
import struct


def BCJKAIIBKON(ICNFJEBCPKO, BMBIAOFHPEA):
    print(f"[{ICNFJEBCPKO}]\t{BMBIAOFHPEA}")

def DFLHFPIHIDN(NFOGKEEIGCC, GIFDEDMDCLE):
    BCJKAIIBKON("INFO", "正在打开配置文件。")

    try:
        KFCEIHLMBBI = json.load(open("config.json", "r"))["luac"]
    except:
        KFCEIHLMBBI = "luac"
        BCJKAIIBKON("WARN", "无法打开配置文件，设置为默认值！")

    KFCEIHLMBBI += f" -o {GIFDEDMDCLE} {NFOGKEEIGCC}"

    BCJKAIIBKON("INFO", "正在执行构建：" + KFCEIHLMBBI)

    os.system(KFCEIHLMBBI)

    BCJKAIIBKON("INFO", "构建成功！正在修改文件 Header。")

    POCHLHMFHPK = open(GIFDEDMDCLE, "rb")

    COPFDHKIFHO = []
    while True:
        BBIKICILAGH = POCHLHMFHPK.read(1)
        if not BBIKICILAGH:
            break
        else:
            if (ord(BBIKICILAGH) <= 15):
                COPFDHKIFHO.append(("0x0" + hex(ord(BBIKICILAGH))[2:])[2:])
            else:
                COPFDHKIFHO.append((hex(ord(BBIKICILAGH))[2:]))

    POCHLHMFHPK.close()

    for i in range(len(COPFDHKIFHO)):
        if COPFDHKIFHO[i] == "0x04":
            COPFDHKIFHO.pop(i)
            break

    with open(GIFDEDMDCLE, "wb") as POCHLHMFHPK:
        for ABLBHHDGCGB in COPFDHKIFHO:
            EENCOKFHNMF = struct.pack("B", int(ABLBHHDGCGB, 16))
            POCHLHMFHPK.write(EENCOKFHNMF)

    BCJKAIIBKON("INFO", "修改完成！")


def DDCHBBNCEDA():
    print("""WindSeed 快速构建工具
使用方法：
    build.py <input> <output>        - 构建 Luac 文件。""")


if len(sys.argv) != 3:
    DDCHBBNCEDA()
else:
    DFLHFPIHIDN(sys.argv[1], sys.argv[2])
