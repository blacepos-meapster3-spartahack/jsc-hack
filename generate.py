"""

"""
from typing import List
from data import Metrics
from perlin_noise import PerlinNoise

noise = PerlinNoise()

SLEEP_HEART_BASE_RATE = 55
WORK_HEART_BASE_RATE = 80
DOWNTIME_HEART_BASE_RATE = 70

HEART_NOISE_SCALE = 10

FULL_HEART_BASELINE = [
    *[SLEEP_HEART_BASE_RATE for _ in range(89-0+1)],       # morning sleep 12am-5am  (5 hrs,   0-89)
    *[DOWNTIME_HEART_BASE_RATE for _ in range(134-90+1)],  # downtime       6am-9am  (3 hrs,  90-134)
    *[WORK_HEART_BASE_RATE for _ in range(269-135+1)],     # work           9am-4pm  (8 hrs, 135-269)
    *[DOWNTIME_HEART_BASE_RATE for _ in range(329-270+1)], # downtime       5pm-9pm  (5 hrs, 270-329)
    *[SLEEP_HEART_BASE_RATE for _ in range(359-330+1)],    # evening sleep 10pm-11pm (2 hrs, 330-359)
]

def noisy_heart_day() -> List[float]:
    noise_day = [4*noise(i/HEART_NOISE_SCALE) for i in range(360)]
    noise_work = [8*noise(i/HEART_NOISE_SCALE) * (1 if i in range(135-10,269+10) else 0) for i in range(360)]
    return [a+b+c for a,b,c in zip(FULL_HEART_BASELINE, noise_day, noise_work)]

def person_1_gen(metrics: Metrics):
    noise_day = [noise(i/HEART_NOISE_SCALE) for i in range(360)]
    metrics.astronaut1.heartrate_bpm = [a+b for a,b in zip(noise_day, FULL_HEART_BASELINE)]

def person_2_gen(metrics: Metrics):
    # add this percent of person 1's heartrate to person 2
    heart_correlation_person_2 = 0.8

def person_3_gen(metrics: Metrics):
    pass

def person_4_gen(metrics: Metrics):
    pass

def gen_initial() -> Metrics:
    metrics = Metrics.default()
    metrics.astronaut1.heartrate_bpm = noisy_heart_day()
    metrics.astronaut2.heartrate_bpm = noisy_heart_day()
    metrics.astronaut3.heartrate_bpm = noisy_heart_day()
    metrics.astronaut4.heartrate_bpm = noisy_heart_day()

    return metrics

def gen_from_history(history: List[Metrics]) -> Metrics:
    # for the past X measurements, determine the trend
    metrics = Metrics.default()
    person_1_gen(metrics)
    person_2_gen(metrics)
    person_3_gen(metrics)
    person_4_gen(metrics)


    