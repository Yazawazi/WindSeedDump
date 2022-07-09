# WindSeedDump / 风种子转储工具

WindSeed Type 1 `sb_1184180438`.

支持类型 1 官服的 `sb_1184180438` 解析。

```bash
python .\dump.py [json or bin]
```

## Format of JSON / JSON 格式

```jsonc
{
  "index": int,
  "object": {
    "areaNotify": {
      "areaId": int,
      "areaCode": base64str,
      "areaType": 1
    }
  },
  "packet": base64str,
  "packetId": int,
  "protoName": "WindSeedClientNotify",
  "reltime": float,
  "source": int,
  "time": int
}
```

## Disclaimer / 免责声明

Children do not understand things, just write for fun. You want to do bad things, I can only condemn you morally, I can not stop you.

小孩子不懂事，写着玩的。你做坏事，我管不着你。
