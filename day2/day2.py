"""Day 2: Cube Conundrum"""
import re

def read_file(file):
    with open(file, 'r') as input_file:
        #Read file line by line and return a list of each game
        return [line.strip() for line in input_file.readlines()]
    
def get_game_info(game_log):
    #Takes in a single game and returns (game #, game info))
    split_number = game_log.split(":")

    game_number = split_number[0].split(" ")[1]
    game_info = split_number[1]
    
    return int(game_number), game_info
    
def is_game_possible(game_info):
    max_red = 12
    max_green = 13
    max_blue = 14

    pattern = re.compile('\d{1,2}\s[rgb]')
    cube_numbers = re.findall(pattern, game_info)

    for cube in cube_numbers:
        number = int(cube.split(" ")[0])
        color = cube.split(" ")[1]

        if(
            (color == 'r' and number > max_red) or
            (color == 'g' and number > max_green) or
            (color == 'b' and number > max_blue)
            
        ):
            #Return false at any point if the cubes exceed maxes
            return False

    #All pulls were in range, game is possible
    return True

def sum_possible_game_numbers(game_log):
    game_number_sum = 0
    for game in game_log:
        game_number = get_game_info(game)[0]
        game_info = get_game_info(game)[1]

        if(is_game_possible(game_info)):
            game_number_sum += game_number

    return game_number_sum

def determine_fewest(game_info):
    pattern = re.compile('\d{1,2}\s[rgb]')
    cube_numbers = re.findall(pattern, game_info)

    min_red = 0
    min_green = 0
    min_blue = 0

    for cube in cube_numbers:
        number = int(cube.split(" ")[0])
        color = cube.split(" ")[1]

        if(color == 'r' and number > min_red):
            min_red = number
        if(color == 'g' and number > min_green):
            min_green = number
        if(color == 'b' and number > min_blue):
            min_blue = number
    return [min_red, min_green, min_blue]


def sum_of_power(game_log):
    sum_of_power = 0
    for game in game_log:
        game_info = get_game_info(game)[1] #Don't need game number, just cubes
        fewest = determine_fewest(game_info)

        power = fewest[0] * fewest[1] * fewest[2]
        sum_of_power += power
    
    return sum_of_power

if __name__ == '__main__':
    game_log = read_file("input.txt")
    sum = sum_possible_game_numbers(game_log)
    print(f"Sum of possible game numbers {sum}")
    power_sum = sum_of_power(game_log)
    print(f"Sum of possible game numbers {power_sum}")