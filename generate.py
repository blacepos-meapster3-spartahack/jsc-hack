"""

"""
from __future__ import annotations
from dataclasses import dataclass
from typing import List

@dataclass
class Metrics:
    # Heartrate
    heartrate_bpm: List[float]

    # Sleep
    previous_night_awake_minutes: float
    previous_night_rem_minutes: float
    previous_night_light_minutes: float
    previous_night_deep_minutes: float

    # Food
    meal_1_breakfast: float
    meal_2_breakfast: float
    meal_3_breakfast: float
    meal_4_breakfast: float
    meal_5_breakfast: float

    meal_1_lunch: float
    meal_2_lunch: float
    meal_3_lunch: float
    meal_4_lunch: float
    meal_5_lunch: float

    meal_1_dinner: float
    meal_2_dinner: float
    meal_3_dinner: float
    meal_4_dinner: float
    meal_5_dinner: float

    # Subjective measurements
    frustration_morning: float
    stomach_ache_morning: float
    anxiety_morning: float
    headache_morning: float
    chills_morning: float
    fatigue_morning: float
    diarrhea_morning: float
    muscle_pain_morning: float
    sneezing_morning: float
    vomiting_morning: float
    stuffy_nose_morning: float
    sore_throat_morning: float
    concentration_evening: float

    frustration_morning: float
    stomach_ache_evening: float
    anxiety_evening: float
    headache_evening: float
    chills_evening: float
    fatigue_evening: float
    diarrhea_evening: float
    muscle_pain_evening: float
    sneezing_evening: float
    vomiting_evening: float
    stuffy_nose_evening: float
    sore_throat_evening: float
    concentration_evening: float

    def gen_from_history(history: List[Metrics]) -> Metrics:
        # for the past 10 measurements, determine the trend
        pass