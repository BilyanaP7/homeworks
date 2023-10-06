name_series = input("Enter the series you are watching: ")
num_seasons = int(input("Enter number of seasons: "))
num_episodes = int(input("Enter number of episodes: "))
duration = int(input("Enter episode duration: "))

full_ep = duration - 0.25
special_ep = duration + 12

time_needed = (((special_ep * num_seasons) + (duration * (num_episodes - num_seasons))) * num_episodes * num_seasons)//60

print(f"I needed {time_needed} minutes to watch {name_series} all series.")