65

data=[41,32,30,23,24,32,11,39,24,46,50,18,41,14,33,50,38,25, 32,16,43,19,35,22,46,43,10,22,17,47,66,48,25,43,28,31,12,25, 12,48]
num=[(9.5,19.5),(19.5,29.5),(29.5,39.5),(39.5,49.5),(49.5,59.5),(59.5,69.5)]
def make(data,classes):
    result=[]
    total = len(data)
    for low, high in classes:
        count=0
        for i in data:
            if low <= i <= high:
                count+=1
        result.append(count)
    print("계급____계급간격____도수__상대도수___히스토그램")
    for a in range(len(classes)):
        v=result[a]/total
        print(f"제{a+1}계급  {classes[a][0]}-{classes[a][1]}  {result[a]}  {v:.2f}  {'-'*result[a]}")
    return result
make(data,num)
