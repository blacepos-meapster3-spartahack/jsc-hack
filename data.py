from __future__ import annotations
from dataclasses import dataclass
import dataclasses
import json
from typing import List


# total 360+4+15+26
@dataclass
class AstronautMetrics:
    # Heartrate measurements (total 360) 15 measurements per hour
    # key points:
    # 0    = 12am
    # 15   = 1am
    # 30   = 2am
    # 45   = 3am
    # 60   = 4am
    # 75   = 5am
    # 90   = 6am
    # 105  = 7am
    # 120  = 8am
    # 135  = 9am
    # 150  = 10am
    # 165  = 11am
    # 180  = 12am
    # 195  = 1pm
    # 210  = 2pm
    # 225  = 3pm
    # 240  = 4pm
    # 255  = 5pm
    # 270  = 6pm
    # 285  = 7pm
    # 300  = 8pm
    # 315  = 9pm
    # 330  = 10pm
    # 345  = 11pm
    heartrate_bpm: List[float]

    # Sleep (total 4)
    previous_night_awake_minutes: float
    previous_night_rem_minutes: float
    previous_night_light_minutes: float
    previous_night_deep_minutes: float

    # Food (total 5 * 3)
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

    # Subjective measurements (total 13 * 2)
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
    concentration_morning: float

    frustration_evening: float
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

    @staticmethod
    def default() -> AstronautMetrics:
        return AstronautMetrics(
            [0 for _ in range(360)],
            *[0 for _ in range(4+15+26)]
        )
    
    def to_vector(self) -> List[float]:
        out: List[float | List[float]] = list(vars(self).values())
        heart: List[float] = out.pop(0) #type: ignore
        out.extend(heart)

        return out #type: ignore


@dataclass
class Metrics:
    astronaut1: AstronautMetrics
    astronaut2: AstronautMetrics
    astronaut3: AstronautMetrics
    astronaut4: AstronautMetrics

    @staticmethod
    def default() -> Metrics:
        return Metrics(
            AstronautMetrics.default(),
            AstronautMetrics.default(),
            AstronautMetrics.default(),
            AstronautMetrics.default()
        )

    def to_vector(self) -> List[float]:
        out = []
        out.extend(self.astronaut1.to_vector())
        out.extend(self.astronaut2.to_vector())
        out.extend(self.astronaut3.to_vector())
        out.extend(self.astronaut4.to_vector())
        
        return out
    
    def to_json(self) -> str:
        return json.dumps(dataclasses.asdict(self))
