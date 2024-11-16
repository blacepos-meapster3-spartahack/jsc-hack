astronauts:
1. a
    - normal noisy heartrate
    - fine with any meal
2. a
    - heartrate correlates with #1 by 0.8
    - when #3 eats meal 2 for breakfast, they receive a 0.8 for stomach_ache_evening
    - when #3 eats meal 3 for breakfast, they receive a 1.0 for sneezing_morning
    - when eats meal 3 for breakfast, lunch, or dinner, they receive a 1.0 for diarrhea and stomache ache
3. a
    - experiences work stress on the 3rd, 4th, and 5th day of every 7 days
    - experiences morning frustration on 4th and 5th of every 7 days
    - when eats meal 1 for lunch or breakfast, they receive a 0.2 for concentration_evening
    - when eats meal 2 for b,l,d 6 days prior, they receive a 0.0 for concentration_morning
4. a
    - work stress on 6th of every 5 days
    - heartrate correlates with #3 by 0.5
    - when eats meal 1 for breakfast, lunch, or dinner the previous day, they receive 1.0 for vomiting_morning, diarrhea_morning


all:
- experiences work stress on day 2 of every 7 days
- baseline noisy heartrate
- if rem sleep is below 40 minutes for 3 days in a row
    - anxiety is 1.0
    - concentration is 0.1
    - headache is 0.8
- if deep sleep is below 40 minutes for 3 days in a row
    - headache is 0.8
    - sneezing is 0.8