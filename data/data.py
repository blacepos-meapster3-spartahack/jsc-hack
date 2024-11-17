from __future__ import annotations
from dataclasses import dataclass
import dataclasses
import json
from typing import Any, Dict, List


# total 360+4+9+14 = 387
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

    # Food (total 3 * 3)
    meal_1_breakfast: float
    meal_2_breakfast: float
    meal_3_breakfast: float

    meal_1_lunch: float
    meal_2_lunch: float
    meal_3_lunch: float

    meal_1_dinner: float
    meal_2_dinner: float
    meal_3_dinner: float

    # Checklist measurements (total 7 * 2)
    frustration_morning: float
    stomach_ache_morning: float
    anxiety_morning: float
    headache_morning: float
    diarrhea_morning: float
    sneezing_morning: float
    concentration_morning: float

    frustration_evening: float
    stomach_ache_evening: float
    anxiety_evening: float
    headache_evening: float
    diarrhea_evening: float
    sneezing_evening: float
    concentration_evening: float

    @staticmethod
    def default() -> AstronautMetrics:
        ret = AstronautMetrics(
            [0 for _ in range(360)],
            *[0 for _ in range(4+9+14)]
        )
        ret.concentration_morning = 1.
        ret.concentration_evening = 1.
        return ret
    
    @staticmethod
    def from_vector(raw: List[float]) -> AstronautMetrics:
        metrics = AstronautMetrics.default()
        metrics.heartrate_bpm = raw[:360]
        metrics.previous_night_awake_minutes = raw[360]
        metrics.previous_night_rem_minutes = raw[361]
        metrics.previous_night_light_minutes = raw[362]
        metrics.previous_night_deep_minutes = raw[363]
        metrics.meal_1_breakfast = raw[364]
        metrics.meal_2_breakfast = raw[365]
        metrics.meal_3_breakfast = raw[366]
        metrics.meal_1_lunch = raw[367]
        metrics.meal_2_lunch = raw[368]
        metrics.meal_3_lunch = raw[369]
        metrics.meal_1_dinner = raw[370]
        metrics.meal_2_dinner = raw[371]
        metrics.meal_3_dinner = raw[372]
        metrics.frustration_morning = raw[373]
        metrics.stomach_ache_morning = raw[374]
        metrics.anxiety_morning = raw[375]
        metrics.headache_morning = raw[376]
        metrics.diarrhea_morning = raw[377]
        metrics.sneezing_morning = raw[378]
        metrics.concentration_morning = raw[379]
        metrics.frustration_evening = raw[380]
        metrics.stomach_ache_evening = raw[381]
        metrics.anxiety_evening = raw[382]
        metrics.headache_evening = raw[383]
        metrics.diarrhea_evening = raw[384]
        metrics.sneezing_evening = raw[385]
        metrics.concentration_evening = raw[386]
        return metrics
    
    def to_vector(self) -> List[float]:
        return (
            self.heartrate_bpm +
            [
            self.previous_night_awake_minutes,
            self.previous_night_rem_minutes,
            self.previous_night_light_minutes,
            self.previous_night_deep_minutes,
            self.meal_1_breakfast,
            self.meal_2_breakfast,
            self.meal_3_breakfast,
            self.meal_1_lunch,
            self.meal_2_lunch,
            self.meal_3_lunch,
            self.meal_1_dinner,
            self.meal_2_dinner,
            self.meal_3_dinner,
            self.frustration_morning,
            self.stomach_ache_morning,
            self.anxiety_morning,
            self.headache_morning,
            self.diarrhea_morning,
            self.sneezing_morning,
            self.concentration_morning,
            self.frustration_evening,
            self.stomach_ache_evening,
            self.anxiety_evening,
            self.headache_evening,
            self.diarrhea_evening,
            self.sneezing_evening,
            self.concentration_evening
            ]
        )


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
    
    @staticmethod
    def from_vector(raw: List[float]) -> Metrics:
        return Metrics(
            AstronautMetrics.from_vector(raw[0*387:1*387]),
            AstronautMetrics.from_vector(raw[1*387:2*387]),
            AstronautMetrics.from_vector(raw[2*387:3*387]),
            AstronautMetrics.from_vector(raw[3*387:4*387])
        )
    
    def to_dict(self) -> Dict[str, Any]:
        return dataclasses.asdict(self)
    
    def to_json(self) -> str:
        return json.dumps(self.to_dict())
    
    def to_jsonf(self):
        with open("test_file.json", "w") as f:
            json.dump(self.to_dict(), f)

    @staticmethod
    def multi_to_json(days: List[Metrics]) -> str:
        return json.dumps([m.to_dict() for m in days])

    @staticmethod
    def multi_to_jsonf(days: List[Metrics]):
        with open("test_file.json", "w") as f:
            json.dump([m.to_dict() for m in days], f)
