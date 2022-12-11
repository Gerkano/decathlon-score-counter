from dataclasses import dataclass
from enum import Enum
from pydantic import validate_arguments
from typing import Optional, Union
from utils import convert_timestamp_to_float
import log_settings

@validate_arguments
@dataclass
class Contestant:
    name: str
    hundred_meters_run_in_seconds: float
    long_jump_in_meters: float
    shot_put_in_meters: float
    high_jump_in_meters: float
    four_hundred_meters_in_seconds: float
    hurdles_in_seconds: float
    discus_throw_in_meters: float
    pole_vault_in_meters: float
    javelin_throw_in_meters: float
    fifteen_hundred_meters_in_seconds: Optional[Union[str, float]]
    points_and_place: dict

    def __post_init__(self):
        self.fifteen_hundred_meters_in_seconds = convert_timestamp_to_float(self.fifteen_hundred_meters_in_seconds)

class Parameters(Enum):
    '''
    Based on Wikipedia (https://en.wikipedia.org/wiki/Decathlon) 
    A, B and C paramteres placed in a tuple for calculating each competition points. 
    Some of the data needs to be converted from meters to centimeters, 
    from minutes to seconds, which are specified in the name of the parameter
    '''
    HUNDRED_METERS_TRACK = (25.4347, 18, 1.81)
    LONG_JUMP_FIELD_CM = (0.14354, 220, 1.4)
    SHOT_PUT_FIELD = (51.39, 1.5, 1.05)
    HIGH_JUMP_FIELD_CM = (0.8465, 75, 1.42)
    FOUR_HUNDRED_METERS_TRACK = (1.53775, 82, 1.81)
    HURDLES_TRACK = (5.74352, 28.5, 1.92)
    DISCUS_THROW_FIELD = (12.91, 4, 1.1)
    POLE_VAULT_FIELD_CM = (0.2797, 100, 1.35)
    JAVELIN_THROW_FIELD = (10.14, 7, 1.08)
    FIFTEEN_HUNDRED_METERS_TRACK_SECONDS = (0.03768, 480, 1.85)

class PointCounter:
    def __init__(self, results: list) -> int:
        self.results = results

    def track_formula(self, param: tuple, score: float) -> int:
        param_a, param_b, param_c = param
        points = int(param_a*(param_b - score)**param_c)
        log_settings.debug_log(
            f"INT(A*(B-P)**C) track calculation result: {points}:, where P:{score} and A, B, C:{param}"
            )
        return points

    def field_formula(self, param: tuple, score: float) -> int:
        param_a, param_b, param_c = param
        points = int(param_a*(score - param_b)**param_c)
        log_settings.debug_log(
            f"INT(A*(P-B)**C) field calculation result: {points}, where P: {score} and A, B, C: {param}"
            )
        return points

    def point_count(self) -> int:
        track = "TRACK"
        convert_centimeters = "CM"
        convert_seconds = "SECONDS"
        sum = 0
        for result, param in zip(self.results, Parameters):
            if track in str(param.name).split("_"):
                if convert_seconds in str(param.name).split("_"):
                    result = convert_timestamp_to_float(result)
                points =  self.track_formula(param.value, float(result))
            else:
                if convert_centimeters in str(param.name).split("_"):
                    result = float(result) * 100
                points = self.field_formula(param.value, float(result))
            sum = sum + points
        log_settings.debug_log(f"Sum of points accumulated through all competitions: {sum}")
        return sum

