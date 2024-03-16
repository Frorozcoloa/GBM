

def main():
    # Example usage:
    """
    G = 3
    P = 10
    race_results = [[1,2,3,4,5,6,7,8,9,10], [10,1,2,3,4,5,6,7,8,9], [9,10,1,2,3,4,5,6,7,8]]
    S = 2
    scoring_systems = [[5, 5, 4, 3 ,2 ,1], [3, 10, 5,1]]

    champions = calculate_champion(G, P, race_results, scoring_systems)
    for champ_system in champions:
        print(' '.join(map(str, champ_system)))
    G = 1
    P = 3
    race_results = [[3,2,1]]
    S = 3
    scoring_systems = [[3, 5, 3, 2], [3, 5, 2, 1], [3, 1,1,1]]

    champions = calculate_champion(G, P, race_results, scoring_systems)
    for champ_system in champions:
        print(' '.join(map(str, champ_system)))

    """
    G = 2
    P = 4
    race_results = [[1,3,4,2], [4,1,3,2]]
    S = 2
    scoring_systems = [[3, 3,2,1], [3, 5, 4,2]]

    champions = calculate_champion(G, P, race_results, scoring_systems)
    for champ_system in champions:
        print(' '.join(map(str, champ_system)))


if __name__ == "__main__":
    main()