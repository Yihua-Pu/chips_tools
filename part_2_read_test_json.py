import test_data
import json

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json( json_data ):
    #Initialize a new GameLibrary
    game_library = test_data.GameLibrary()

    ### Begin Add Code Here ###
    #Loop through the json_data
        #Create a new Game object from the json_data by reading
        #  title
        #  year
        #  platform (which requires reading name and launch_year)
        #Add that Game object to the game_library
    ### End Add Code Here ###
    for game_info in json_data['games']:
        title = game_info['title']
        year = game_info['year']
        platform_info = game_info['platform']
        platform_name = platform_info['name']
        launch_year = platform_info['launch_year']

        # Create Platform object
        platform = test_data.Platform(name=platform_name, launch_year=launch_year)
        # Create Game object
        game = test_data.Game(title=title, platform=platform, year=year)
        # Add that Game object to the game_library
        game_library.add_game(game)
    return game_library


#Part 2
input_json_file = "data/test_data.json"
with open(input_json_file, 'r') as reader:
    game_json_data = json.load(reader)
    print(make_game_library_from_json(game_json_data))
### Begin Add Code Here ###
#Open the file specified by input_json_file
#Use the json module to load the data from the file
#Use make_game_library_from_json(json_data) to convert the data to GameLibrary data
#Print out the resulting GameLibrary data using print()
### End Add Code Here ###
