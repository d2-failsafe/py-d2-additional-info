from typing import Any, Dict, Union

import ujson

from tools import readFile

BungieJSONFilePath = "./data/BungieManifest/"

manifest_json: Dict[str, Dict[Any, Any]] = {}


def loadLocal(language: str = "zh-chs") -> None:
    """
    :说明: `loadLocal`
    > 装载本地清单文件到内存

    :可选参数:
      * `language: str = 'zh-chs'`: 语言
    """
    global manifest_json
    if not manifest_json.get(language):
        manifest_json[language] = ujson.loads(
            readFile(BungieJSONFilePath + f"BungieJSON_{language}.json")
        )


def getAll(tablename: str = None, language: str = "zh-chs") -> Union[dict, list]:
    """
    :说明: `getAll`
    > 获取清单中所有的数据

    :可选参数:
      * `tablename: str = None`: 表名，若指定则返回相对表的列表，否则返回整个清单字典
      * `language: str = 'zh-chs'`: 语言

    :返回:
    - `Union[dict, list]`: 整个清单字典 or 指定表的列表
    """
    if tablename:
        return list(manifest_json[language][tablename].values())
    return manifest_json


def get(
    tablename: str,
    hash: Union[str, int] = None,
    itemname: str = None,
    language: str = "zh-chs",
) -> dict:
    """
    :说明: `get`
    > 通过 `hash` 或 `name` 获取某个表中相应表项的数据, 必须输入一个字段来进行查询, 同时存在时以 `hash` 为准

    :参数:
      * `tablename: str`: 表名

    :可选参数:
      * `hash: Union[str, int]`: 道具 `hash`, 即 `item['hash']`
      * `itemname: str = None`: 道具名，即 `item['displayProperties']['name']`
      * `language: str = zh-chs`: 语言

    :返回:
        - `dict`: 查询到的数据原JSON格式字典
    """
    if not hash and not itemname:
        raise ValueError("`hash` or `itemname` must be specified")
    if not hash and itemname:
        item = [
            item
            for item in manifest_json[language][tablename]
            if item.get("displayProperties")
            and item.get("displayProperties").get("name") == itemname
        ]
        return item[0] if item else {}
    else:
        return manifest_json[language][tablename].get(str(hash))


if __name__ == "__main__":
    loadLocal()
    pause = 0
