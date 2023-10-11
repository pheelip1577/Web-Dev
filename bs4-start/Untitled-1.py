import operator
 
name = input("Whats your name?:")
bid_price = input("How much are you bidding?: £")

def bid_auction(name, bid_price):
    bidding= {}
    bidding[name] = bid_price
    bidding_cont = False
    while not bidding_cont :
        another_bidder = input("Is there another bidder, Yes or No")
        if another_bidder == " No ":
            bidding_cont = True 
        else:
            another_bidder == " Yes "
            max_key= max(bidding.items(), key= operator.itemgetter(1))[0]
            max_val = bidding.values()
            maximum_val = max(max_val)
            print(f"The winner is {max_key} with a bidding price of  {maximum_val} ")
       
               
bid_auction(name, bid_price)