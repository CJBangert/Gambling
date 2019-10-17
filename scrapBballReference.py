from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import OutputType

# # Get all player box scores for January 1st, 2017 
# client.player_box_scores(day=1, month=1, year=2017)

# # Get all player box scores for January 1st, 2017 in JSON format
# client.player_box_scores(day=1, month=1, year=2017, output_type=OutputType.JSON)

# # Output all player box scores for January 1st, 2017 in JSON format to 1_1_2017_box_scores.json
# client.player_box_scores(day=1, month=1, year=2017, output_type=OutputType.JSON, output_file_path="./1_1_2017_box_scores.json")

# # Output all player box scores for January 1st, 2017 in JSON format to 1_1_2017_box_scores.csv
# client.player_box_scores(day=1, month=1, year=2017, output_type=OutputType.CSV, output_file_path="./1_1_2017_box_scores.csv



# Get 2017-2018 advanced season statistics for all players
client.players_advanced_season_totals(season_end_year=2018, output_type=OutputType.JSON, output_file_path="./season_totals.json")