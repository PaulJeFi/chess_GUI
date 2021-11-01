settings = {
    "engine" : "stockfish", # The engine you want to use. Accepts "stockfish" or
                            # "komodo".
    "strength" : { # The level of the engine
        "Skill Level" : 20, # 0 to 20
        "ELO" : False # Use ELO limit strenght. Only for Stockfish.
                      # Min : 1350 Max : 2850. If you don't want to use ELO,
                      # type False.
    },
    "type" : "64", # If you are on Window, enter 64 for 64-bits or 32 for 32-bits.
                 # For stockfish, even if your computer is 64 bits but old, type 34.
                 # If you are on Linux, support 64 bits and BMI2.
                 # Accepted "type" : "32", "64", "BMI2".
    "chess set" : "lichess", # The chess et to use. "lichess" or "chesscom".
    "window size" : 720 # The size (in pixels) of the chessboard.
}