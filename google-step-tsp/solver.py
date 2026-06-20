#!/usr/bin/env python3

#http://localhost:8000/visualizer/build/default/

import sys
import math

from common import print_tour, read_input


def solve(cities):
    # Build a trivial solution.
    # Visit the cities in the order they appear in the input.


    diff_list = [] #基準となる都市から、他の都市への距離を保存
    visited_list = [] #既に回った都市を保存
    answer_list = [] #答えとして返すリスト


    #最初の都市だけ、それぞれの関数にいれておく
    now_city = cities[0] #今いる都市の座標を保存
    now_city_index = 0 #今いる都市のcitiesにおけるindex（都市番号）を保存
    answer_list.append(0)
    visited_list.append(now_city_index)


    cities_count = len(cities) #全都市の数（全ての都市を回ったかの判断に使用）


    
    ###貪欲法：計算量O(N^2)

    #while：全ての都市を回るまで繰り返す
    flag = True
    while flag == True:

        #一番近くの都市を見つけるため,都市毎の座標の差を計算する
        #全ての都市との差を計算
        for index in range(len(cities)):

            #既に訪れた都市は計算から除外
            if index in visited_list:
                continue

            #now_cityと各都市との距離の差を計算
            diff_x = (cities[index][0] - now_city[0]) ** 2
            diff_y = (cities[index][1] - now_city[1]) ** 2
            diff_xy = math.sqrt(diff_x + diff_y)

            #(差、index)のタプルとして全都市との差を保存
            diff_list.append((diff_xy, index))


        #一番差の小さい都市（一番近い都市）を次に行く都市に決定
        next_city = min(diff_list)

        #戻り値のリストに追加
        answer_list.append(next_city[1])

        #今の都市を次に進める
        now_city = cities[next_city[1]]
        now_city_index = next_city[1]
        # print(f"now_city_index: {now_city_index}")

        #進めた先の都市を、visitedに追加
        visited_list.append(now_city_index)

        
        #全ての差をリセット（次のwhileではnext_cityとの差を計算し直す必要があるため）
        diff_list.clear()


        #全ての都市に訪れたら、while文を抜ける
        if len(visited_list) == cities_count:
            flag = False




    ###2-opt：計算量O(N＾3)

    #while：2optに従って道を入れ替えた後、更に交差している道がないか確認する
    #改善が無くなるまで、2optの処理を繰り返す
    flag = True
    while flag == True:
        flag = False
        
        #交差している道が無いか、道2本の全組み合わせを確認
        for index in range(len(answer_list) - 1):
            for goal_index in range(index + 2, len(answer_list)):

                #start/goal ： citiesにおける目的の都市のindex
                start = answer_list[index]
                goal= answer_list[goal_index] 

                start_next = answer_list[index + 1]
                goal_next = answer_list[(goal_index + 1) % len(answer_list)]#最後の都市から最初の都市に戻れるようにする


                #現在の距離の差を計算
                start_diff = math.sqrt((cities[start][0] - cities[start_next][0])** 2 + (cities[start][1] - cities[start_next][1]) ** 2)
                goal_diff = math.sqrt((cities[goal][0] - cities[goal_next][0]) ** 2 + (cities[goal][1] - cities[goal_next][1]) ** 2)
                diff_xy = start_diff + goal_diff


                #2optした後の距離の差を計算
                opt_s_diff = math.sqrt((cities[start][0] - cities[goal][0]) ** 2 + (cities[start][1] - cities[goal][1]) ** 2)  
                opt_g_diff = math.sqrt((cities[start_next][0] - cities[goal_next][0]) ** 2 + (cities[start_next][1] - cities[goal_next][1]) ** 2)
                opt_diff_xy = opt_s_diff + opt_g_diff


                #2optに従って入れ替えた方が距離が短くなる = 道がクロスしているため、都市の順番を入れ替える
                if opt_diff_xy < diff_xy:
                    answer_list[index+ 1 : goal_index + 1] = answer_list[index + 1 : goal_index + 1][::-1]
                    #値の入れ替えがあった場合は最初から繰り返す
                    flag = True 
                
            
    return answer_list


if __name__ == '__main__':
    assert len(sys.argv) > 1
    tour = solve(read_input(sys.argv[1]))
    print_tour(tour)
