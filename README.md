# WindSeedDump
WindSeed Type 1 `sb_1184180438` Dump Tool

```
python .\dump.py json.json
```

## Format of JSON

```jsonc
{
  "index": num,
  "object": {
    "areaNotify": {
      "areaId": num,
      "areaCode": base64str,
      "areaType": 1
    }
  },
  "packet": base64str,
  "packetId": num,
  "protoName": "WindSeedClientNotify",
  "reltime": float,
  "source": num,
  "time": num
}
```
