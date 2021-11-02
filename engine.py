from settings import settings
from configure_engine import engine
import requests
import chess
import random
import json

book = 'book.json'

def move_from_book(the_board, Book) :
    '''Renvoie un mouvement du répertoire si la position y est.'''
    with open(Book, "r") as Table :
        table = json.load(Table)
    try :
        return random.choice(table[the_board.fen()])
    except Exception :
        return None


def tablebase(board) :
    if len(board.piece_map()) <= 7 :
        try :
            fen = board.fen().replace(' ', '_')
            info = requests.get(f'http://tablebase.lichess.ovh/standard?fen={fen}')
            return info.json()['moves'][0]['uci']
        except Exception :
            pass
    return None

def play(board) :
    try :
        if settings["use openning book"] :
            if move_from_book(board, book) != None :
                return move_from_book(board, book), 'book'
        elif settings["use endgame tablebase"] :
            if tablebase(board) != None :
                return tablebase(board), 'tablebase'
    except Exception :
        pass
    return str(engine.play(board, chess.engine.Limit(time=0.1)).move), engine.analyse(board, chess.engine.Limit(time=0.1))["score"]