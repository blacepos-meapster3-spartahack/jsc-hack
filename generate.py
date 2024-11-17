"""

"""
from typing import Any, Callable, List
from data import AstronautMetrics, Metrics
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

def random_food_choices(metrics: Metrics, getter: Callable[[Metrics], AstronautMetrics]):
    food_choice = random.randint(0,2)
    getter(metrics).meal_1_breakfast = 1. if food_choice == 0 else 0.
    getter(metrics).meal_2_breakfast = 1. if food_choice == 1 else 0.
    getter(metrics).meal_3_breakfast = 1. if food_choice == 2 else 0.

    food_choice = random.randint(0,2)
    getter(metrics).meal_1_lunch = 1. if food_choice == 0 else 0.
    getter(metrics).meal_2_lunch = 1. if food_choice == 1 else 0.
    getter(metrics).meal_3_lunch = 1. if food_choice == 2 else 0.

    food_choice = random.randint(0,2)
    getter(metrics).meal_1_dinner = 1. if food_choice == 0 else 0.
    getter(metrics).meal_2_dinner = 1. if food_choice == 1 else 0.
    getter(metrics).meal_3_dinner = 1. if food_choice == 2 else 0.

def gen_initial() -> Metrics:
    metrics = Metrics.default()
    metrics.astronaut1.heartrate_bpm = noisy_heart_day()
    metrics.astronaut2.heartrate_bpm = noisy_heart_day()
    metrics.astronaut3.heartrate_bpm = noisy_heart_day()
    metrics.astronaut4.heartrate_bpm = noisy_heart_day()

    metrics.astronaut1.previous_night_awake_minutes    = 0
    metrics.astronaut1.previous_night_rem_minutes      = 2*60
    metrics.astronaut1.previous_night_light_minutes    = 6*60
    metrics.astronaut1.previous_night_deep_minutes     = 2*60

    metrics.astronaut2.previous_night_awake_minutes    = 0
    metrics.astronaut2.previous_night_rem_minutes      = 2*60
    metrics.astronaut2.previous_night_light_minutes    = 6*60
    metrics.astronaut2.previous_night_deep_minutes     = 2*60

    metrics.astronaut3.previous_night_awake_minutes    = 0
    metrics.astronaut3.previous_night_rem_minutes      = 2*60
    metrics.astronaut3.previous_night_light_minutes    = 6*60
    metrics.astronaut3.previous_night_deep_minutes     = 2*60

    metrics.astronaut4.previous_night_awake_minutes    = 0
    metrics.astronaut4.previous_night_rem_minutes      = 2*60
    metrics.astronaut4.previous_night_light_minutes    = 6*60
    metrics.astronaut4.previous_night_deep_minutes     = 2*60

    random_food_choices(metrics, lambda x: x.astronaut1)
    random_food_choices(metrics, lambda x: x.astronaut2)
    random_food_choices(metrics, lambda x: x.astronaut3)
    random_food_choices(metrics, lambda x: x.astronaut4)

    metrics.astronaut1.frustration_morning = 0.
    metrics.astronaut1.frustration_evening = 0.
    metrics.astronaut1.stomach_ache_morning = 0.
    metrics.astronaut1.stomach_ache_evening = 0.
    metrics.astronaut1.anxiety_morning = 0.
    metrics.astronaut1.anxiety_evening = 0.
    metrics.astronaut1.headache_morning = 0.
    metrics.astronaut1.headache_evening = 0.
    metrics.astronaut1.diarrhea_morning = 0.
    metrics.astronaut1.diarrhea_evening = 0.
    metrics.astronaut1.sneezing_morning = 0.
    metrics.astronaut1.sneezing_evening = 0.
    metrics.astronaut1.concentration_morning = 1.
    metrics.astronaut1.concentration_evening = 1.

    metrics.astronaut2.frustration_morning = 0.
    metrics.astronaut2.frustration_evening = 0.
    metrics.astronaut2.stomach_ache_morning = 0.
    metrics.astronaut2.stomach_ache_evening = 0.
    metrics.astronaut2.anxiety_morning = 0.
    metrics.astronaut2.anxiety_evening = 0.
    metrics.astronaut2.headache_morning = 0.
    metrics.astronaut2.headache_evening = 0.
    metrics.astronaut2.diarrhea_morning = 0.
    metrics.astronaut2.diarrhea_evening = 0.
    metrics.astronaut2.sneezing_morning = 0.
    metrics.astronaut2.sneezing_evening = 0.
    metrics.astronaut2.concentration_morning = 1.
    metrics.astronaut2.concentration_evening = 1.

    metrics.astronaut3.frustration_morning = 0.
    metrics.astronaut3.frustration_evening = 0.
    metrics.astronaut3.stomach_ache_morning = 0.
    metrics.astronaut3.stomach_ache_evening = 0.
    metrics.astronaut3.anxiety_morning = 0.
    metrics.astronaut3.anxiety_evening = 0.
    metrics.astronaut3.headache_morning = 0.
    metrics.astronaut3.headache_evening = 0.
    metrics.astronaut3.diarrhea_morning = 0.
    metrics.astronaut3.diarrhea_evening = 0.
    metrics.astronaut3.sneezing_morning = 0.
    metrics.astronaut3.sneezing_evening = 0.
    metrics.astronaut3.concentration_morning = 1.
    metrics.astronaut3.concentration_evening = 1.

    return metrics

def subtract_sleep_if_anxiety_day_before(history: List[Metrics], metrics: Metrics, getter: Callable[[Metrics], AstronautMetrics]):
    anxiety_before_sleep = getter(history[-1]).anxiety_evening
    lost = range_map(0, 1, 0, 120, anxiety_before_sleep)
    getter(metrics).previous_night_rem_minutes -= lost
    getter(metrics).previous_night_awake_minutes += lost

    lost = range_map(0, 1, 0, 60, anxiety_before_sleep)
    getter(metrics).previous_night_deep_minutes -= lost
    getter(metrics).previous_night_awake_minutes += lost

def reset_sleep_if_5_days_poor_sleep(history: List[Metrics], metrics: Metrics, getter: Callable[[Metrics], AstronautMetrics]):
    count = 0
    for day in history[-6:-1]:
        if getter(day).previous_night_awake_minutes > 200:
            count += 1

    if count >= 5:
        getter(metrics).previous_night_awake_minutes    = 0
        getter(metrics).previous_night_rem_minutes      = 2*60
        getter(metrics).previous_night_light_minutes    = 6*60
        getter(metrics).previous_night_deep_minutes     = 2*60

def poor_rem_2_days_consec(history: List[Metrics], getter: Callable[[Metrics], AstronautMetrics]):
    if len(history) < 2:
        return False

    return getter(history[-2]).previous_night_rem_minutes < 60 and \
           getter(history[-1]).previous_night_rem_minutes < 60

def poor_deep_2_days_consec(history: List[Metrics], getter: Callable[[Metrics], AstronautMetrics]):
    if len(history) < 2:
        return False

    return getter(history[-2]).previous_night_deep_minutes < 60 and \
           getter(history[-1]).previous_night_deep_minutes < 60

def has_condition_prior(history: List[Metrics], days_prior: int, getter: Callable[[Metrics], float], threshold=0.5) -> bool:
    # yesterday: 1 day prior
    # day before yesterday: 2 days prior
    # etc.
    if len(history) > days_prior - 1:
        return getter(history[-days_prior]) > threshold
    return False

ate_food_prior = has_condition_prior

def ate_food_today(metrics: Metrics, getter: Callable[[Metrics], float], threshold=0.5) -> bool:
    return getter(metrics) > threshold

def person_1_gen(history: List[Metrics], metrics: Metrics):
    metrics.astronaut1.heartrate_bpm = zipsum(
        noisy_heart_day(),
        # experience stress on day 2 of the week
        WORK_STRESS_HEART_BASELINE if get_day_of_week(history) == 1 else ZERO_HEART_BASELINE
    )

    metrics.astronaut1.previous_night_awake_minutes = 0
    metrics.astronaut1.previous_night_rem_minutes   = 2*60
    metrics.astronaut1.previous_night_light_minutes = 6*60
    metrics.astronaut1.previous_night_deep_minutes  = 2*60

    subtract_sleep_if_anxiety_day_before(history, metrics, lambda x: x.astronaut1)

    reset_sleep_if_5_days_poor_sleep(history, metrics, lambda x: x.astronaut1)

    random_food_choices(metrics, lambda x: x.astronaut1)

    if has_condition_prior(history, 2, lambda x: x.astronaut2.sneezing_evening):
        metrics.astronaut1.sneezing_morning = 1.0


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

    metrics.astronaut2.previous_night_awake_minutes = 0
    metrics.astronaut2.previous_night_rem_minutes   = 2*60
    metrics.astronaut2.previous_night_light_minutes = 6*60
    metrics.astronaut2.previous_night_deep_minutes  = 2*60
    
    subtract_sleep_if_anxiety_day_before(history, metrics, lambda x: x.astronaut2)

    reset_sleep_if_5_days_poor_sleep(history, metrics, lambda x: x.astronaut2)

    random_food_choices(metrics, lambda x: x.astronaut2)

    if ate_food_today(metrics, lambda x: x.astronaut3.meal_2_breakfast):
        metrics.astronaut2.stomach_ache_evening = 0.8

    if ate_food_today(metrics, lambda x: x.astronaut3.meal_3_breakfast):
        metrics.astronaut2.sneezing_morning = 0.5
    
    if ate_food_today(metrics, lambda x: x.astronaut2.meal_2_breakfast) or\
       ate_food_today(metrics, lambda x: x.astronaut2.meal_2_lunch) or\
       ate_food_today(metrics, lambda x: x.astronaut2.meal_2_dinner):
        metrics.astronaut2.diarrhea_evening = 1.0
        metrics.astronaut2.stomach_ache_evening = 1.0
    
    if ate_food_today(metrics, lambda x: x.astronaut2.meal_3_breakfast) or\
       ate_food_today(metrics, lambda x: x.astronaut2.meal_3_lunch) or\
       ate_food_today(metrics, lambda x: x.astronaut2.meal_3_dinner):
        metrics.astronaut2.sneezing_morning = 1.0

    if has_condition_prior(history, 2, lambda x: x.astronaut1.sneezing_evening):
        metrics.astronaut2.sneezing_morning = 1.0

    if has_condition_prior(history, 1, lambda x: x.astronaut3.frustration_morning) and\
       has_condition_prior(history, 2, lambda x: x.astronaut3.frustration_morning):
        metrics.astronaut2.frustration_morning = 1.0
        metrics.astronaut2.frustration_evening = 1.0


def person_3_gen(history: List[Metrics], metrics: Metrics):
    metrics.astronaut3.heartrate_bpm = zipsum(
        noisy_heart_day(),
        # experience stress on days 2,3,4,5 of the week
        WORK_STRESS_HEART_BASELINE if get_day_of_week(history) in (1,2,3,4) else ZERO_HEART_BASELINE
    )

    metrics.astronaut3.previous_night_awake_minutes = 0
    metrics.astronaut3.previous_night_rem_minutes   = 2*60
    metrics.astronaut3.previous_night_light_minutes = 6*60
    metrics.astronaut3.previous_night_deep_minutes  = 2*60

    subtract_sleep_if_anxiety_day_before(history, metrics, lambda x: x.astronaut3)

    reset_sleep_if_5_days_poor_sleep(history, metrics, lambda x: x.astronaut3)
    
    random_food_choices(metrics, lambda x: x.astronaut3)

    if get_day_of_week(history) in (3,4):
        metrics.astronaut3.frustration_morning = 0.8

    if has_condition_prior(history, 2, lambda x: x.astronaut4.sneezing_evening):
        metrics.astronaut3.sneezing_morning = 1.0

    if ate_food_prior(history, 1, lambda x: x.astronaut3.meal_1_dinner):
        metrics.astronaut3.concentration_morning = 0.2

    if ate_food_prior(history, 4, lambda x: x.astronaut3.meal_2_lunch):
        metrics.astronaut3.concentration_morning = 0.0
        metrics.astronaut3.concentration_evening = 0.0


def person_4_gen(history: List[Metrics], metrics: Metrics):
    heart_correlation_person_3 = 0.5
    metrics.astronaut4.heartrate_bpm = zipsum(
        noisy_heart_day(),
        # correlation with #3 (subtract off their baseline)
        (np.array(metrics.astronaut3.heartrate_bpm) - np.array(FULL_HEART_BASELINE)) * heart_correlation_person_3,
        # experience stress on day 2 and 6 of the week
        WORK_STRESS_HEART_BASELINE if get_day_of_week(history) in (1,5) else ZERO_HEART_BASELINE
    )

    metrics.astronaut4.previous_night_awake_minutes = 0
    metrics.astronaut4.previous_night_rem_minutes   = 2*60
    metrics.astronaut4.previous_night_light_minutes = 6*60
    metrics.astronaut4.previous_night_deep_minutes  = 2*60

    subtract_sleep_if_anxiety_day_before(history, metrics, lambda x: x.astronaut4)

    reset_sleep_if_5_days_poor_sleep(history, metrics, lambda x: x.astronaut4)

    random_food_choices(metrics, lambda x: x.astronaut4)

    if has_condition_prior(history, 2, lambda x: x.astronaut3.sneezing_evening):
        metrics.astronaut4.sneezing_morning = 1.0

    if ate_food_prior(history, 1, lambda x: x.astronaut4.meal_1_breakfast) or\
       ate_food_prior(history, 1, lambda x: x.astronaut4.meal_1_lunch) or\
       ate_food_prior(history, 1, lambda x: x.astronaut4.meal_1_dinner):
        metrics.astronaut4.stomach_ache_morning = 0.2
        metrics.astronaut4.stomach_ache_evening = 0.1


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

def range_map(a, b, c, d, x):
    return (d-c)*(x-a)/(b-a)+c
