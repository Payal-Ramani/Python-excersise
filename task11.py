one_term_wrong_arr_pro = [2, 5, 8, 11, 15, 17]
one_term_wrong_geo_pro = [3, 9, 27, 81, 244, 729]

arithmetic_progression = int(input("Enter the arithmetic progression to find that arithmetic seq. :"))
def fun_to_find_right_arithmetic_seq(wrong_arith_pro_arr,arithmetic_progression):
    for i in range(len(wrong_arith_pro_arr)-1):
        if wrong_arith_pro_arr[i+1]-wrong_arith_pro_arr[i] != arithmetic_progression:
            wrong_arith_pro_arr[i+1] = wrong_arith_pro_arr[i] + arithmetic_progression
    return wrong_arith_pro_arr
print(f"Correct A.P. : {fun_to_find_right_arithmetic_seq(one_term_wrong_arr_pro,arithmetic_progression)}") 
    
geometric_progression = int(input("Enter the geometric progression to find that arithmetic seq. :"))
def fun_to_find_right_geometric_seq(wrong_geo_pro_arr,geometric_progression):
    for i in range(len(wrong_geo_pro_arr)-1):
        if wrong_geo_pro_arr[i+1]/wrong_geo_pro_arr[i] != geometric_progression:
            wrong_geo_pro_arr[i+1] = wrong_geo_pro_arr[i] * geometric_progression
    return wrong_geo_pro_arr
print(f"Correct G.P. : {fun_to_find_right_geometric_seq(one_term_wrong_geo_pro,geometric_progression)}") 

