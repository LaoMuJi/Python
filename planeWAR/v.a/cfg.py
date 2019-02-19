import configparser

cfg = configparser.ConfigParser()
cfg.read("cfg.cfg",encoding='utf-8')

sp_name = cfg.get("SmallPlane", "name")
print(sp_name)

sp_width = cfg.getint("SmallPlane", "width")
print(sp_width)


