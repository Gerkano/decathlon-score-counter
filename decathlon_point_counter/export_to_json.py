from score_and_rank import get_calculated_score, get_sorted_by_rank
from utils import get_file_location
from decathlon_rules import Contestant
import dataclasses
import csv
import json

def open_and_export(file: bytes, upload_folder:str) -> None:
    with open(f'{get_file_location(upload_folder)}\\{file.filename}', newline='') as csvfile:
        contestant_results = csv.reader(csvfile, delimiter=';', quotechar='|')
        export_to_json(contestant_results, file.filename.split(".")[0], upload_folder)

def export_to_json(contestant_results: list, filename: str, upload_folder: str) -> None:     
    with open(f"{get_file_location(upload_folder)}\\{filename}.json", "w") as outfile:
        competitors = []
        for result in contestant_results:
            place_and_score = get_calculated_score(result)
            player = Contestant(*result, place_and_score)
            competitors.append(dataclasses.asdict(player))
        json.dump(get_sorted_by_rank(competitors), outfile, indent=4)

