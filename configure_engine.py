import platform
import os
import chess.engine
from settings import settings

engine_name = settings["engine"]

pahts = {"Linux": ".engines/Linux",
        "Darwin": ".engines/Darwin",
        "Windows": ".engines/Windows"}

system = platform.system()
if system == "Linux" or "Darwin" :
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.system(f"chmod +x {dir_path}/engines/{system}/{engine_name}")
    if system == "Darwin" :
        engine_name += ".1-64-osx"
    else : 
        engine_name += '_' + settings["type"]

elif system == "Windows" :
    engine_name += "_" + settings["type"] + 'bits' + '.exe'

path = f"./engines/{system}/{engine_name}"

engine = chess.engine.SimpleEngine.popen_uci(path)
if not settings["strength"]["drawer"] :
    if settings["engine"] == "komodo" : 
        engine.configure({"Skill": settings["strength"]["Skill Level"]})
    elif settings["engine"] == "stockfish" :
        if settings["strength"]["ELO"] :
            engine.configure({"UCI_LimitStrength": 'true', "UCI_Elo": settings["strength"]["ELO"]})
        else :
            engine.configure({"Skill Level": settings["strength"]["Skill Level"]})