## 76 Item Dumper Tool

##### Pre-Req:
This is meant to be a companion to work with the [ItemExtractorMod](https://www.nexusmods.com/fallout76/mods/698), this tool was designed to accepted the output pushed thru the [ModCompanionTool](https://www.nexusmods.com/fallout76/mods/698) as well. Both of these created by mansonew2, shout out to them.

This is also developed on Python 3.8 so update ur python kiddo.

##### Why:
I run my own trade sheet found at **https://trade.rhinos.place** and have already done a good bit of tooling to customize it to my needs. I'm more of a build it vs buy it type too so two birds one stone.

##### How Do I Use This:
Well, you probably shouldn't unless you know python pretty well. Right now, it will dump a text file full of strings formatted specifically so I can copy/paste them into my google sheet but if you'd like to modify it, attacking `item_dump_parser/main.py:ItemProcessor.dump()` would be my suggestion as thats where I'm iterating thru the items. I'm also doing all the set up of the model in `run.py` so feel free to edit that as well?

##### Okay, but how do I run this?:
`python run.py` would be my best guess after installing requirements (`python -m pip install -r requirements.txt`)