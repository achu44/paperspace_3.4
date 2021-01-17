min_open_overall=0
max_open_overall=0
max_day_diff=0
previous_close=0
max_change_closing=0
traded_volume=[]
for item_in_list in range(0,len(table3)):
    try:
        row = table3[item_in_list]
        print(row)
#         if None in row:
#             continue
        open=row[1]
        if open == 0:
            continue
        if (row[2] == 0 or row[3] == 0):
            continue
        day_diff = row[2]-row[3]
        
        if item_in_list == 0 or previous_close == 0:
            previous_close = row[4]
            if previous_close == 0:
                continue
        else:
            previous_close = close
        close = row[4]
        if close == 0:
            continue
        close_diff = abs(close-previous_close)
        
        if item_in_list == 0 or min_open_overall==0:
            min_open_overall = open
        if item_in_list == 0 or max_open_overall==0:
            max_open_overall = open
        if item_in_list == 0  or max_day_diff == 0:
            max_day_diff = day_diff
        if item_in_list == 0 or max_change_closing == 0:
            max_change_closing = close_diff
        if (item_in_list == 0 or min_open_overall == 0 or max_open_overall == 0 or max_day_diff == 0 or max_change_closing == 0):
            if (row[6]==0):
                continue
            traded_volume.append(row[6])
            continue
        if open < min_open_overall:
            min_open_overall=open
        if open > max_open_overall:
            max_open_overall=open
        if day_diff > max_day_diff:
            max_day_diff=day_diff
        if close_diff>max_change_closing:
            max_change_closing=close_diff
        traded_volume.append(row[6])
    except:
        continue
    
# borrowed from StackOverFlow, credits to them for the algorithm:
def median(lst):
    sortedLst = sorted(lst)
    lstLen = len(lst)
    index = (lstLen - 1) // 2
   
    if (lstLen % 2):
        return sortedLst[index]
    else:
        return (sortedLst[index] + sortedLst[index + 1])/2.0

print("Here are the values for min_open_overall, max_open_overall, max_day_diff, max_change_closing:")
print(min_open_overall)
print(max_open_overall)
print(max_day_diff)
print(max_change_closing)
    
# mean traded volume
print("The average trading volume daily is " + str(sum(traded_volume)/len(traded_volume)))
print("The median trading volume daily is " + str(median(traded_volume)))

