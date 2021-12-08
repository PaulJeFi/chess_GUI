from requests.api import get
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

def get_drawer_move(board, engine) :
    scores = {}
    for move in board.legal_moves :
        board.push(move)
        score = engine.analyse(board, chess.engine.Limit(time=0.1))["score"]
        if not score.is_mate() :
            scores[str(move)] = score.relative.cp
        board.pop()
    zero_score = min([scores[key] for key in scores.keys()], key=abs)
    move = [key for key in scores.keys() if zero_score == abs(scores[key])][0]
    return move

def play(board) :
    try :
        if settings["use openning book"] :
            if move_from_book(board, book) != None :
                return move_from_book(board, book), 'book'
        elif settings["use endgame tablebase"] :
            if tablebase(board) != None :
                return tablebase(board), 'tablebase'
        elif settings["strength"]["drawer"] :
            return get_drawer_move(board, engine), engine.analyse(board, chess.engine.Limit(time=0.1))["score"]
    except Exception :
        pass
    return str(engine.play(board, chess.engine.Limit(time=0.1)).move), engine.analyse(board, chess.engine.Limit(time=0.1))["score"]