from nba_api.stats.endpoints import playercareerstats

career = playercareerstats.PlayerCareerStats(player_id='201939')
career_df = career.get_data_frames()[0]
print(career_df.head())
