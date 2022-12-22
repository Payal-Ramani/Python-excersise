one_term_wrong_arr_pro = [2, 5, 8, 11, 15, 17]
one_term_wrong_geo_pro = [3, 9, 27, 81, 244, 729]

arithmetic_progression = 3
for i in range(len(one_term_wrong_arr_pro)-1):
    if one_term_wrong_arr_pro[i+1]-one_term_wrong_arr_pro[i] != arithmetic_progression:
        temp = one_term_wrong_arr_pro[i+1]
        one_term_wrong_arr_pro[i+1] = one_term_wrong_arr_pro[i] + arithmetic_progression
print(f"Correct A.P. : {one_term_wrong_arr_pro}")  
    
geometric_progression = 3
for i in range(len(one_term_wrong_geo_pro)-1):
    if one_term_wrong_geo_pro[i+1]/one_term_wrong_geo_pro[i] != geometric_progression:
        temp = one_term_wrong_geo_pro[i+1]
        one_term_wrong_geo_pro[i+1] = one_term_wrong_geo_pro[i] * geometric_progression
print(f"Correct G.P. : {one_term_wrong_geo_pro}") 