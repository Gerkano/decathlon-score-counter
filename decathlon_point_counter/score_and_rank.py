from decathlon_rules import PointCounter
import log_settings


def get_calculated_score(result: list) -> dict:
    calculate = PointCounter(result[1:])
    place_and_score = {
        "score": calculate.point_count() 
    }  
    return place_and_score

def sort_list_key(element):
    return element["points_and_place"]["score"]

def get_sorted_by_rank(contestants:list):
    contestants.sort(key=sort_list_key, reverse=True)
    return assign_rank(contestants)

def assign_rank(contestants: list) -> list:
    get_scores = [i["points_and_place"]["score"] for i in contestants]
    for index in range(len(contestants)):
        tie_occurances = get_scores.count(get_scores[index])
        if tie_occurances > 1:
            if get_scores[index] != get_scores[index-1]:
                rank = index + 1
            tie_range= range(rank, rank + tie_occurances)
            rank_range = "-".join([str(i) for i in tie_range])
        else:
            rank_range = str(index + 1)
        contestants[index]['points_and_place']['place'] = rank_range
        log_settings.info_log(f"{contestants[index]['name']} is ranked: {rank_range}")
    return contestants
