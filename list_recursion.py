

def has_my_purchase(fr_p,my_p,i,j):



def sort_purchases()
    my_purchases = [1,2,3,4,5]
    my_friends = ["moses","Sam","kelvin","george"]
    my_friends_purchases = {"moses":[6,7,8,10,11],"Sam":[12     ,11,10,15,20],"kelvin":[5,3,3,1,17],"george":[45,60,50      ,60,50,]}
    results = []

    for i in range(len(my_friends)):
        fr = my_friends[i]
        fr_purchases = my_friends_purchases[fr]
        for k in range(len(fr_purchases)):
             purchase = fr_purchases[k]
            if has_my_purchase(purchase,my_purchases,0,0):
                continue
             else:
                 result.append(purchase)

