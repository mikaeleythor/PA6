from Word import *
from WordTree import *
from LetterSet import *
from Player import *
from Board import *

def read_file(filename):
    file_object = open(filename)
    line_list = file_object.readlines()
    return line_list[2::]

def get_attributes(line_list):
    """This function extracts wanted values from each line in line_list"""
    word_list = []
    for line in line_list:
        temp = line.split()
        word = temp.pop(0)
        keys = temp.pop(-1)
        language = ''
        word2 = ''
        try:
            if temp[1].isupper():
                word2 = temp.pop(1)
                if temp[2][0] == '(':
                    language = temp.pop(2)
            elif temp[1][0] == '(':
                language = temp.pop(1)    
        except IndexError: # If IndexError occurs then values language and word2 do not exist
            pass
        definition = ' '.join(temp)
        word_list.append((Word(word, word2, language, keys, definition)))
    return word_list

def create_dictionary():
    line_list = read_file('Collins Scrabble Words (2019) with definitions.txt')
    word_list = get_attributes(line_list)
    word_tree = WordTree()
    for word in word_list:
        word_tree.insert(word)    
    return word_tree

def print_rules():
    pass

def wrong_player_num():
    MIN_PLAYERS = 2
    MAX_PLAYERS = 4
    again = input(f'Please select a number between {MIN_PLAYERS} and {MAX_PLAYERS}, try again? (Y/N): ').upper() == 'Y'
    if not again:
        return False
    else:
        return initialize_players()

def initialize_players():
    MIN_PLAYERS = 2
    MAX_PLAYERS = 4

    player_num = input('How many players: ')
    try:
        player_num = int(player_num)
    except ValueError:
        return wrong_player_num()
    if player_num < MIN_PLAYERS or player_num > MAX_PLAYERS:
        return wrong_player_num()
    elif player_num <= MAX_PLAYERS and player_num >= MIN_PLAYERS:
        player1, player2 = Player(), Player()
        if player_num >= 3:
            player3 = Player()
            if player_num == 4:
                player4 = Player()
                return [player1, player2, player3, player4]
            return [player1, player2, player3]
        return [player1, player2]

def insert_letter():
    pass

def next_player(player, players_list):
    index = players_list.index(player)
    if index == 3:
        return players_list[0]
    return players_list[index+1]

def check_play_conditions():
    return False

def play_game(players_list, dictionary):
    player = players_list[0]
    board = Board()
    play = True
    while play:
        print(board)
        print(player)
        plays = player.play()
        points = board.update(plays)
        player.points+=points
        player.update_letterset()
        # ------------------------------------
        player = next_player(player, players_list)
        play = check_play_conditions()
        print(board)


def start_game(dictionary): 
    print_rules()
    players_list = initialize_players()
    play_game(players_list, dictionary)

if __name__ == "__main__":
    dictionary = create_dictionary()
    start_game(dictionary)