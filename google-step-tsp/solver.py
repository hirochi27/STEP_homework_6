#!/usr/bin/env python3

import sys
import math
from common import print_tour, read_input


def calculate_distance(city1, city2):
    """2つの都市間のユークリッド距離を計算する"""
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def solve_greedy(cities):
    """貪欲法（Nearest Neighbor）を用いて初期経路を構築する"""
    cities_count = len(cities)
    visited = [False] * cities_count  # リストの探索 O(N) を避けるため、探索を O(1) に
    
    # 最初の都市を設定
    current_city_idx = 0
    answer_list = [current_city_idx]
    visited[current_city_idx] = True

    while len(answer_list) < cities_count:
        min_distance = float('inf')
        next_city_idx = -1

        # 一番近い未訪問の都市を探す
        for index in range(cities_count):
            if visited[index]:
                continue
            
            distance = calculate_distance(cities[current_city_idx], cities[index])
            if distance < min_distance:
                min_distance = distance
                next_city_idx = index

        # 次の都市へ移動
        answer_list.append(next_city_idx)
        visited[next_city_idx] = True
        current_city_idx = next_city_idx

    return answer_list


def optimize_2opt(tour, cities):
    """2-opt法を用いて経路の交差を解消し、最適化する"""
    cities_count = len(tour)
    
    while True:
        improved = False
        
        for i in range(cities_count - 1):
            for j in range(i + 2, cities_count):
                # 対象となる4つの都市のインデックス
                idx_i, idx_i_next = tour[i], tour[i + 1]
                idx_j, idx_j_next = tour[j], tour[(j + 1) % cities_count]

                # 現在の2本の枝の距離の和
                current_dist = (calculate_distance(cities[idx_i], cities[idx_i_next]) + 
                                calculate_distance(cities[idx_j], cities[idx_j_next]))
                
                # 繋ぎ替えた後の2本の枝の距離の和
                new_dist = (calculate_distance(cities[idx_i], cities[idx_j]) + 
                            calculate_distance(cities[idx_i_next], cities[idx_j_next]))

                # 繋ぎ替えた方が短くなる場合、経路を反転させる
                if new_dist < current_dist:
                    tour[i + 1 : j + 1] = tour[i + 1 : j + 1][::-1]
                    improved = True
                    
        # すべての組み合わせで改善がなくなったら終了
        if not improved:
            break
            
    return tour




def solve(cities):
    # 1. 貪欲法で初期のルートを作成
    initial_tour = solve_greedy(cities)
    
    # 2. 2-optでルートを最適化
    optimized_tour = optimize_2opt(initial_tour, cities)
    
    return optimized_tour


if __name__ == '__main__':
    assert len(sys.argv) > 1
    tour = solve(read_input(sys.argv[1]))
    print_tour(tour)