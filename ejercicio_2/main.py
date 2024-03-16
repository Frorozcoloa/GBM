from typing import List, Tuple

def get_grand_pilots()-> Tuple[int, int]:
    """
    Get the total of grands and pilots
    return Tuple[int, int] -> (grands, pilots)
    """
    grand, pilots = map(int, input("Ingresa el total de grands y los pilotos: ").split())
    if grand < 0 or grand > 100:
        raise ValueError("The number of grand must be between 1 and 100")
    if pilots < 0 or pilots > 100:
        raise ValueError("The number of pilots must be between 1 and 100")
    return grand, pilots

def result_race(grands: int)-> List[List[int]]:
    """
    Get the results of all the grands
    return List[List[int]] -> [[result1], [result2], ...]
    """
    results = []
    i = 0
    while i < grands:
        result = input(f"Ingresa el resultado de la carrera {i+1}: ").split()
        #convert to int
        result = list(map(int, result))
        results.append(result)
        i += 1
    return results

def get_total_scoring()-> int:
    """
    Get the total of scoring
    return int -> total_scoring
    """
    total_scoring = int(input("Ingresa el total de sistemas de puntucación: "))
    if total_scoring < 1 or total_scoring > 100:
        raise ValueError("The number of total scoring must be between 1 and 100")
    return total_scoring


def get_values_scoring(total_pilots, total_scoring)-> List[int]:
    """
    Get the values of the scoring
    return List[int] -> [scoring1, scoring2, ...]
    """
    scoring_values = []
    i = 0
    while i < total_scoring:
        result = input(f"Ingresa el {i+1} sistema de scoring: ").split()
        #convert to int
        result = list(map(int, result))
        verify_number = result[0]
        if verify_number > total_pilots:
            print("El número donde se dice cuantos pilotos deben ser tomados en cuenta no puede ser mayor al total de pilotos")
            continue
        if verify_number != len(result[1:]):
            print("El número de pilotos clasificados no coincide con el número de pilotos que se deben tomar en cuenta")
            continue
        result = list(map(int, result))
        scoring_values.append(result)
        i += 1
    return scoring_values

def calculate_champion(P:int, race_results:List[List[int]], scoring_systems: List[List[int]])-> List[List[int]]:
    """
    Calculate the champion
    input:
        P: int -> total of pilots
        race_results: List[List[int]] -> [[result1], [result2], ...]
        scoring_systems: List[List[int]] -> [[scoring1], [scoring2], ...]
    return List[List[int]] -> [[champion1], [champion2], ...]
    """
    champions = []

    for system in scoring_systems:
        K, points = system[0], system[1:]
        scores = {i: 0 for i in range(1, P + 1)}

        for race in race_results:
            for  pilot, pos in enumerate(race):
                pilot += 1
                if pos <= K:
                    scores[pilot] += points[pos-1]

        max_score = max(scores.values())
        champions_system = [pilot for pilot, score in scores.items() if score == max_score]

        champions.append(champions_system)

    return champions




def main():
    """Main function"""
    while True:
        grand, pilots = get_grand_pilots()
        if grand == 0 or pilots == 0:
            break
        results = result_race(grand)
        total_scoring = get_total_scoring()
        scoring_values = get_values_scoring(pilots, total_scoring)
        points = calculate_champion(pilots, results, scoring_values)
        for champ_system in points:
            print(' '.join(map(str, champ_system)))


if __name__ == "__main__":
    main()