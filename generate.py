"""

"""
from typing import Any, List
from data import Metrics
from perlin_noise import PerlinNoise
import numpy as np
import random

noise = PerlinNoise()

g_NOISE_SAMPLE_LOC: float = 0
def cached_noise(x: float):
    return noise(g_NOISE_SAMPLE_LOC + x)

def noise_advance(x: float):
    global g_NOISE_SAMPLE_LOC
    g_NOISE_SAMPLE_LOC += x

SLEEP_HEART_BASE_RATE = 55
WORK_HEART_BASE_RATE = 80
DOWNTIME_HEART_BASE_RATE = 70

HEART_NOISE_SCALE = 10

FULL_HEART_BASELINE = [
    *[SLEEP_HEART_BASE_RATE for _ in range(89-0+1)],       # morning sleep 12am-5am  (5 hrs,   0-89)
    *[DOWNTIME_HEART_BASE_RATE for _ in range(134-90+1)],  # downtime       6am-8am  (3 hrs,  90-134)
    *[WORK_HEART_BASE_RATE for _ in range(269-135+1)],     # work           9am-4pm  (8 hrs, 135-269)
    *[DOWNTIME_HEART_BASE_RATE for _ in range(329-270+1)], # downtime       5pm-9pm  (5 hrs, 270-329)
    *[SLEEP_HEART_BASE_RATE for _ in range(359-330+1)],    # evening sleep 10pm-11pm (2 hrs, 330-359)
]

WORK_STRESS_HEART_BASELINE = [
    *[0 for _ in range(141-0+1)],      # 0s              12am-9:29am  (  hrs,   0-141)
    *[15 for _ in range(149-142+1)],   # meeting spike 9:30am-9:59am  (  hrs, 142-149)
    *[0 for _ in range(194-150+1)],    # 0s              10pm-11pm    (  hrs, 150-194)
    *[10 for _ in range(239-195+1)],   # mission spike    1pm-3pm     (  hrs, 195-239)
    *[0 for _ in range(359-240+1)],    # 0s              10pm-11pm    (  hrs, 240-359)
]

ZERO_HEART_BASELINE = [0 for _ in range(360)]

def noisy_heart_day() -> List[float]:
    noise_day = [4*cached_noise(i/HEART_NOISE_SCALE) for i in range(360)]
    noise_advance(360/HEART_NOISE_SCALE)
    noise_work = [8*cached_noise(i/HEART_NOISE_SCALE) * (1 if i in range(135-10,269+10) else 0) for i in range(360)]
    noise_advance(154/HEART_NOISE_SCALE)
    return [a+b+c for a,b,c in zip(FULL_HEART_BASELINE, noise_day, noise_work)]

def gen_initial() -> Metrics:
    metrics = Metrics.default()
    metrics.astronaut1.heartrate_bpm = noisy_heart_day()
    metrics.astronaut2.heartrate_bpm = noisy_heart_day()
    metrics.astronaut3.heartrate_bpm = noisy_heart_day()
    metrics.astronaut4.heartrate_bpm = noisy_heart_day()

    food_choice = random.randint(0,4)
    metrics.astronaut1.meal_1_breakfast = 1. if food_choice == 0 else 0.
    metrics.astronaut1.meal_2_breakfast = 1. if food_choice == 1 else 0.
    metrics.astronaut1.meal_3_breakfast = 1. if food_choice == 2 else 0.

    food_choice = random.randint(0,4)
    metrics.astronaut1.meal_1_lunch = 1. if food_choice == 0 else 0.
    metrics.astronaut1.meal_2_lunch = 1. if food_choice == 1 else 0.
    metrics.astronaut1.meal_3_lunch = 1. if food_choice == 2 else 0.

    food_choice = random.randint(0,4)
    metrics.astronaut1.meal_1_dinner = 1. if food_choice == 0 else 0.
    metrics.astronaut1.meal_2_dinner = 1. if food_choice == 1 else 0.
    metrics.astronaut1.meal_3_dinner = 1. if food_choice == 2 else 0.

    food_choice = random.randint(0,4)
    metrics.astronaut2.meal_1_breakfast = 1. if food_choice == 0 else 0.
    metrics.astronaut2.meal_2_breakfast = 1. if food_choice == 1 else 0.
    metrics.astronaut2.meal_3_breakfast = 1. if food_choice == 2 else 0.

    food_choice = random.randint(0,4)
    metrics.astronaut2.meal_1_lunch = 1. if food_choice == 0 else 0.
    metrics.astronaut2.meal_2_lunch = 1. if food_choice == 1 else 0.
    metrics.astronaut2.meal_3_lunch = 1. if food_choice == 2 else 0.

    food_choice = random.randint(0,4)
    metrics.astronaut2.meal_1_dinner = 1. if food_choice == 0 else 0.
    metrics.astronaut2.meal_2_dinner = 1. if food_choice == 1 else 0.
    metrics.astronaut2.meal_3_dinner = 1. if food_choice == 2 else 0.
    
    food_choice = random.randint(0,4)
    metrics.astronaut3.meal_1_breakfast = 1. if food_choice == 0 else 0.
    metrics.astronaut3.meal_2_breakfast = 1. if food_choice == 1 else 0.
    metrics.astronaut3.meal_3_breakfast = 1. if food_choice == 2 else 0.

    food_choice = random.randint(0,4)
    metrics.astronaut3.meal_1_lunch = 1. if food_choice == 0 else 0.
    metrics.astronaut3.meal_2_lunch = 1. if food_choice == 1 else 0.
    metrics.astronaut3.meal_3_lunch = 1. if food_choice == 2 else 0.

    food_choice = random.randint(0,4)
    metrics.astronaut3.meal_1_dinner = 1. if food_choice == 0 else 0.
    metrics.astronaut3.meal_2_dinner = 1. if food_choice == 1 else 0.
    metrics.astronaut3.meal_3_dinner = 1. if food_choice == 2 else 0.

    food_choice = random.randint(0,4)
    metrics.astronaut4.meal_1_breakfast = 1. if food_choice == 0 else 0.
    metrics.astronaut4.meal_2_breakfast = 1. if food_choice == 1 else 0.
    metrics.astronaut4.meal_3_breakfast = 1. if food_choice == 2 else 0.

    food_choice = random.randint(0,4)
    metrics.astronaut4.meal_1_lunch = 1. if food_choice == 0 else 0.
    metrics.astronaut4.meal_2_lunch = 1. if food_choice == 1 else 0.
    metrics.astronaut4.meal_3_lunch = 1. if food_choice == 2 else 0.

    food_choice = random.randint(0,4)
    metrics.astronaut4.meal_1_dinner = 1. if food_choice == 0 else 0.
    metrics.astronaut4.meal_2_dinner = 1. if food_choice == 1 else 0.
    metrics.astronaut4.meal_3_dinner = 1. if food_choice == 2 else 0.

    return metrics

def person_1_gen(history: List[Metrics], metrics: Metrics):
    metrics.astronaut1.heartrate_bpm = zipsum(
        noisy_heart_day(),
        # experience stress on day 2 of the week
        WORK_STRESS_HEART_BASELINE if get_day_of_week(history) == 1 else ZERO_HEART_BASELINE
    )

    food_choice = random.randint(0,4)
    metrics.astronaut1.meal_1_breakfast = 1. if food_choice == 0 else 0.
    metrics.astronaut1.meal_2_breakfast = 1. if food_choice == 1 else 0.
    metrics.astronaut1.meal_3_breakfast = 1. if food_choice == 2 else 0.

    food_choice = random.randint(0,4)
    metrics.astronaut1.meal_1_lunch = 1. if food_choice == 0 else 0.
    metrics.astronaut1.meal_2_lunch = 1. if food_choice == 1 else 0.
    metrics.astronaut1.meal_3_lunch = 1. if food_choice == 2 else 0.

    food_choice = random.randint(0,4)
    metrics.astronaut1.meal_1_dinner = 1. if food_choice == 0 else 0.
    metrics.astronaut1.meal_2_dinner = 1. if food_choice == 1 else 0.
    metrics.astronaut1.meal_3_dinner = 1. if food_choice == 2 else 0.

def person_2_gen(history: List[Metrics], metrics: Metrics):
    # add this percent of person 1's heartrate to person 2
    heart_correlation_person_1 = 0.8
    metrics.astronaut2.heartrate_bpm = zipsum(
        noisy_heart_day(),
        # correlation with #1 (subtract off their baseline)
        (np.array(metrics.astronaut1.heartrate_bpm) - np.array(FULL_HEART_BASELINE)) * heart_correlation_person_1,
        # experience stress on day 2 of the week
        WORK_STRESS_HEART_BASELINE if get_day_of_week(history) == 1 else ZERO_HEART_BASELINE
    )

    food_choice = random.randint(0,4)
    metrics.astronaut2.meal_1_breakfast = 1. if food_choice == 0 else 0.
    metrics.astronaut2.meal_2_breakfast = 1. if food_choice == 1 else 0.
    metrics.astronaut2.meal_3_breakfast = 1. if food_choice == 2 else 0.

    food_choice = random.randint(0,4)
    metrics.astronaut2.meal_1_lunch = 1. if food_choice == 0 else 0.
    metrics.astronaut2.meal_2_lunch = 1. if food_choice == 1 else 0.
    metrics.astronaut2.meal_3_lunch = 1. if food_choice == 2 else 0.

    food_choice = random.randint(0,4)
    metrics.astronaut2.meal_1_dinner = 1. if food_choice == 0 else 0.
    metrics.astronaut2.meal_2_dinner = 1. if food_choice == 1 else 0.
    metrics.astronaut2.meal_3_dinner = 1. if food_choice == 2 else 0.

def person_3_gen(history: List[Metrics], metrics: Metrics):
    metrics.astronaut3.heartrate_bpm = zipsum(
        noisy_heart_day(),
        # experience stress on days 2,3,4,5 of the week
        WORK_STRESS_HEART_BASELINE if get_day_of_week(history) in (1,2,3,4) else ZERO_HEART_BASELINE
    )
    
    food_choice = random.randint(0,4)
    metrics.astronaut3.meal_1_breakfast = 1. if food_choice == 0 else 0.
    metrics.astronaut3.meal_2_breakfast = 1. if food_choice == 1 else 0.
    metrics.astronaut3.meal_3_breakfast = 1. if food_choice == 2 else 0.

    food_choice = random.randint(0,4)
    metrics.astronaut3.meal_1_lunch = 1. if food_choice == 0 else 0.
    metrics.astronaut3.meal_2_lunch = 1. if food_choice == 1 else 0.
    metrics.astronaut3.meal_3_lunch = 1. if food_choice == 2 else 0.

    food_choice = random.randint(0,4)
    metrics.astronaut3.meal_1_dinner = 1. if food_choice == 0 else 0.
    metrics.astronaut3.meal_2_dinner = 1. if food_choice == 1 else 0.
    metrics.astronaut3.meal_3_dinner = 1. if food_choice == 2 else 0.

def person_4_gen(history: List[Metrics], metrics: Metrics):
    heart_correlation_person_3 = 0.5
    metrics.astronaut4.heartrate_bpm = zipsum(
        noisy_heart_day(),
        # correlation with #3 (subtract off their baseline)
        (np.array(metrics.astronaut3.heartrate_bpm) - np.array(FULL_HEART_BASELINE)) * heart_correlation_person_3,
        # experience stress on day 2 and 6 of the week
        WORK_STRESS_HEART_BASELINE if get_day_of_week(history) in (1,5) else ZERO_HEART_BASELINE
    )

    food_choice = random.randint(0,4)
    metrics.astronaut4.meal_1_breakfast = 1. if food_choice == 0 else 0.
    metrics.astronaut4.meal_2_breakfast = 1. if food_choice == 1 else 0.
    metrics.astronaut4.meal_3_breakfast = 1. if food_choice == 2 else 0.

    food_choice = random.randint(0,4)
    metrics.astronaut4.meal_1_lunch = 1. if food_choice == 0 else 0.
    metrics.astronaut4.meal_2_lunch = 1. if food_choice == 1 else 0.
    metrics.astronaut4.meal_3_lunch = 1. if food_choice == 2 else 0.

    food_choice = random.randint(0,4)
    metrics.astronaut4.meal_1_dinner = 1. if food_choice == 0 else 0.
    metrics.astronaut4.meal_2_dinner = 1. if food_choice == 1 else 0.
    metrics.astronaut4.meal_3_dinner = 1. if food_choice == 2 else 0.

def gen_from_history(history: List[Metrics]) -> Metrics:
    # for the past X measurements, determine the trend
    metrics = Metrics.default()
    person_1_gen(history, metrics)
    person_2_gen(history, metrics)
    person_3_gen(history, metrics)
    person_4_gen(history, metrics)

    return metrics

def zipsum(*args) -> List[Any]:
    return [sum(component) for component in zip(*args)]

def get_abs_day(history: List[Metrics]) -> int:
    return len(history)

def get_day_of_week(history: List[Metrics]) -> int:
    return len(history) % 7