import sys
import math

from common import print_tour, read_input


# 2都市間の距離を計算
def calculate_distance(city1, city2):
    diff_x = (city1[0] - city2[0]) ** 2
    diff_y = (city1[1] - city2[1]) ** 2
    return math.sqrt(diff_x + diff_y)


# 貪欲法で都市を回る順番を作る関数
def greedy(cities):
    diff_list = []       # 基準となる都市から、他の都市への距離を保存
    visited_list = []    # 既に回った都市を保存
    answer_list = []     # 答えとして返すリスト

    # 都市が存在しない場合
    if len(cities) == 0:
        return answer_list

    # 最初の都市だけ、それぞれのリストに入れておく
    now_city = cities[0]
    now_city_index = 0
    answer_list.append(now_city_index)
    visited_list.append(now_city_index)

    cities_count = len(cities)

    # 全ての都市を回るまで繰り返す
    while len(visited_list) < cities_count:

        # 現在の都市と、未訪問の全都市との距離を計算
        for index in range(len(cities)):

            # 既に訪れた都市は計算から除外
            if index in visited_list:
                continue

            diff_xy = calculate_distance(now_city, cities[index])
            diff_list.append((diff_xy, index))

        # 一番近い都市を次に行く都市に決定
        next_city = min(diff_list)

        answer_list.append(next_city[1])

        # 現在の都市を次の都市へ進める
        now_city = cities[next_city[1]]
        now_city_index = next_city[1]

        visited_list.append(now_city_index)

        # 次の計算に備えて距離をリセット
        diff_list.clear()

    return answer_list



#2-opt
def two_opt(cities, answer_list):
    flag = True

    # 改善がなくなるまで繰り返す
    while flag == True:
        flag = False

        # 道2本の全組み合わせを確認
        for index in range(len(answer_list) - 1):
            for goal_index in range(index + 2, len(answer_list)):

                # citiesにおける都市番号
                start = answer_list[index]
                goal = answer_list[goal_index]

                start_next = answer_list[index + 1]
                goal_next = answer_list[(goal_index + 1) % len(answer_list)]

                # 現在の2本の道の距離
                start_diff = calculate_distance(cities[start],cities[start_next])
                goal_diff = calculate_distance(cities[goal],cities[goal_next])
                diff_xy = start_diff + goal_diff

                # 2-optした後の2本の道の距離
                opt_s_diff = calculate_distance(cities[start],cities[goal])
                opt_g_diff = calculate_distance(cities[start_next],cities[goal_next])
                opt_diff_xy = opt_s_diff + opt_g_diff

                # 入れ替えた方が短い場合、都市の順番を反転
                if opt_diff_xy < diff_xy:
                    answer_list[index + 1:goal_index + 1] = (answer_list[index + 1:goal_index + 1][::-1])
                    flag = True

    return answer_list



#更に2.5optを行う
#巡回する都市の順番を一か所入れ替える

def two_five_opt(cities, answer_list):

    while True:
        flag = False

        # 移動させる都市の位置
        for index in range(len(answer_list)):
            a = answer_list[(index - 1) % len(answer_list)]
            b_city = answer_list[index]
            c = answer_list[(index + 1) % len(answer_list)]

            # 都市を差し込む位置を選ぶ
            for k in range(len(answer_list)):

                # a-b、b-c間には差し込まない
                if k == index or (k + 1) % len(answer_list) == index:
                    continue

                # d、eの間にb_cityを差し込みたい
                d = answer_list[k]
                e = answer_list[(k + 1) % len(answer_list)]

                # 変更前の距離
                old_distance = (
                    calculate_distance(cities[a], cities[b_city])
                    + calculate_distance(cities[b_city], cities[c])
                    + calculate_distance(cities[d], cities[e])
                )

                # 変更後の距離
                new_distance = (
                    calculate_distance(cities[a], cities[c])
                    + calculate_distance(cities[d], cities[b_city])
                    + calculate_distance(cities[b_city], cities[e])
                )

                if new_distance < old_distance - 1e-10:
                    city = answer_list.pop(index)

                    # popで、後ろのインデックスが一つずれる
                    if index < k:
                        k -= 1

                    # dとeの間にb_cityを入れる
                    answer_list.insert(k + 1, city)

                    flag = True
                    break

            # 改善したら、新しい経路で最初からやり直し
            if flag == True:
                break

        # どの都市をどこに移動させても改善しなかった場合
        if flag == False:
            break

    return answer_list


def solve(cities):
    # 貪欲法で最初の経路を作る
    answer_list = greedy(cities)

    # 2-optで経路を改善する
    answer_list = two_opt(cities, answer_list)

    #2.5opt
    answer_list = two_five_opt(cities, answer_list)

    return answer_list


if __name__ == '__main__':
    assert len(sys.argv) > 1
    tour = solve(read_input(sys.argv[1]))
    print_tour(tour)
