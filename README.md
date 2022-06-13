# WindSeedDump
WindSeed Type 1 `sb_1184180438` Dump Tool

```
python .\dump.py json.json
```

## Format of JSON

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

## Disclaimer

Children do not understand things, just write for fun. You want to do bad things, I can only condemn you morally, I can not stop you.

## How to build

I can't talk properly: `modified Lua 5.3`, `0x04`, `CS.UnityEngine`
