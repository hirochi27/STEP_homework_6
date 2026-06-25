#!/usr/bin/env python3

import csv
import math
import random
import shutil
import time
from pathlib import Path

from common import read_input
from solver_2 import solve

INPUT_FILE = "input_6.csv"
LOG_FILE = "random_start_input6_log.csv"
BEST_OUTPUT_FILE = "best_output_6.csv"
BEST_INFO_FILE = "best_output_6_info.txt"
TRIAL_OUTPUT_DIR = Path("random_start_outputs_6")

# 5時間回す
TIME_LIMIT_SEC = 5 * 60 * 60


def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def calculate_tour_distance(cities, tour):
    total = 0.0

    for i in range(len(tour)):
        city1 = cities[tour[i]]
        city2 = cities[tour[(i + 1) % len(tour)]]
        total += calculate_distance(city1, city2)

    return total


def save_tour(output_file, tour):
    with open(output_file, "w") as f:
        f.write("index\n")

        for city_index in tour:
            f.write(f"{city_index}\n")


def read_best_distance():
    log_path = Path(LOG_FILE)

    if not log_path.exists():
        return None

    best_distance = None

    with open(log_path) as f:
        reader = csv.DictReader(f)

        for row in reader:
            distance = float(row["distance"])

            if best_distance is None or distance < best_distance:
                best_distance = distance

    return best_distance


def main():
    random.seed()
    cities = read_input(INPUT_FILE)
    cities_count = len(cities)

    TRIAL_OUTPUT_DIR.mkdir(exist_ok=True)

    log_path = Path(LOG_FILE)
    log_exists = log_path.exists()
    best_distance = read_best_distance()

    trial = 0

    if log_exists:
        with open(log_path) as f:
            trial = max(0, sum(1 for _ in f) - 1)

    start_time = time.time()

    with open(log_path, "a", newline="") as f:
        writer = csv.writer(f)

        if not log_exists:
            writer.writerow(["trial", "start_city", "distance", "elapsed_sec", "total_elapsed_sec", "output_file", "is_best"])

        while time.time() - start_time < TIME_LIMIT_SEC:
            trial += 1
            start_city = random.randrange(cities_count)
            trial_start_time = time.time()

            tour = solve(cities, start_city)
            distance = calculate_tour_distance(cities, tour)
            elapsed_sec = time.time() - trial_start_time
            total_elapsed_sec = time.time() - start_time

            output_file = TRIAL_OUTPUT_DIR / f"output_6_trial_{trial}.csv"
            save_tour(output_file, tour)

            is_best = best_distance is None or distance < best_distance

            if is_best:
                best_distance = distance
                shutil.copy(output_file, BEST_OUTPUT_FILE)
                shutil.copy(output_file, 'output_6.csv')

                with open(BEST_INFO_FILE, "w") as info:
                    info.write(f"trial: {trial}\n")
                    info.write(f"start_city: {start_city}\n")
                    info.write(f"distance: {distance:.2f}\n")
                    info.write(f"elapsed_sec: {elapsed_sec:.2f}\n")
                    info.write(f"output_file: {output_file}\n")

            writer.writerow([
                trial,
                start_city,
                f"{distance:.2f}",
                f"{elapsed_sec:.2f}",
                f"{total_elapsed_sec:.2f}",
                output_file,
                is_best,
            ])
            f.flush()

            print(
                f"trial={trial} start={start_city} distance={distance:.2f} "
                f"elapsed={elapsed_sec:.2f}s best={best_distance:.2f} is_best={is_best}",
                flush=True,
            )


if __name__ == "__main__":
    main()
