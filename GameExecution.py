from GameSim.Generators.TeamGenerator import TeamGenerator
from GameSim.GameSim import GameSim

if __name__ == "__main__":
    home_team = TeamGenerator.generate_random_team()
    away_team = TeamGenerator.generate_random_team()
    print(f"HOME TEAM: {home_team.team_name} vs. AWAY TEAM: {away_team.team_name}")

    game = GameSim(home_team, away_team)
    game.simulate_game()

    print(
        f"End of game! {home_team.team_name}:{game.home_score} - {away_team.team_name}:{game.away_score}"
    )
