# readlines() 會以每一行資料當作一個字串, 作為 element, 並輸出一個數列資料
result = []
with open("2016_cd_2b_3.txt", 'r') as f:
    content = f.readlines()
    #g.es(content)
    #g.es(len(content))
    # 逐 element 處理
    for i in range(len(content)):
        for line in content[i].splitlines():
            #g.es(content[i].splitlines())
            result.append(list(line.split(",")))
# result element 即為各分組的學員學號數列資料
# 這裡要先以遞增排序處理各組的數列
group_sorted = []
for i in range(len(result)):
    group_list = sorted(list(filter(None, result[i])))
    group_sorted.append(group_list)
g.es("各組已經過遞增排序, 各組第一位即為組長:", group_sorted)

'''
 [['40323101', '40323102', '40323103', '40323108', '40323124'], 
 ['40323109', '40323130', '40323135', '40323136', '40323138', '40323144'], 
 ['40323111', '40323117', '40323118', '40323119', '40323120', '40323122'], 
 ['40323110', '40323113', '40323116', '40323121', '40323151'], 
 ['40323112', '40323133', '40323147', '40323152', '40323155', '40323156'], 
 ['40023139', '40223153', '40323105', '40323106', '40323107', '40323146'], 
 ['40023234', '40123119', '40123141', '40123149', '40123216', '40123227', '40123255'], 
 ['40323125', '40323126', '40323132', '40323149', '40323150', '40323153'], 
 ['40323123', '40323131', '40323137', '40323143', '40323145', '40323154'], 
 ['40323127', '40323128', '40323139', '40323141']]
'''

# 利用 sorted(), 對全班各組數列所組成的數列進行遞增排序
final_result = sorted(group_sorted)
g.es("分組結果:", final_result)

'''
[['40023139', '40223153', '40323105', '40323106', '40323107', '40323146'], 
['40023234', '40123119', '40123141', '40123149', '40123216', '40123227', '40123255'], 
['40323101', '40323102', '40323103', '40323108', '40323124'], 
['40323109', '40323130', '40323135', '40323136', '40323138', '40323144'], 
['40323110', '40323113', '40323116', '40323121', '40323151'], 
['40323111', '40323117', '40323118', '40323119', '40323120', '40323122'], 
['40323112', '40323133', '40323147', '40323152', '40323155', '40323156'], 
['40323123', '40323131', '40323137', '40323143', '40323145', '40323154'], 
['40323125', '40323126', '40323132', '40323149', '40323150', '40323153'], 
['40323127', '40323128', '40323139', '40323141']]
'''

# 取出 final_result 數列中的各組學員學號, 組成一個大數列, 並且用 filter() 去除空字串後, 傳回 iterator 後
# 再用 list() 轉為 數列
final_list = list(filter(None, [stud_id for group_list in final_result for stud_id in group_list]))

'''
# 先從 final_result 數列中取出 group_list, 然後再從各 group_list 中取出各學員學號字串, 然後再組程大數列
final_list = [stud_id
    for group_list in final_result
        for stud_id in group_list]
'''

g.es("課堂上登記共有", len(final_list), " 名學生")

# 讀進學校註冊學員名單, 去除所有跳行符號, 輸出一個大字串
with open("2016_cd_2b_2.txt") as f:
    content = f.read().splitlines()
#g.es(content)
g.es("選課名單上共有", len(content), " 名學生")
# 檢查兩份資料的差異
# 列出已經選課但是並未在第1週上課出現的名單
no_w1 = [stud_id for stud_id in content if stud_id not in final_list]
g.es("已選課, 但第1週缺席名單:", no_w1)
# 第1週擬加選的名單
add_w1 = [stud_id for stud_id in final_list if stud_id not in content]
g.es("擬加選名單:", add_w1)