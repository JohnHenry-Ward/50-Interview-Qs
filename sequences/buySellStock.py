def buySellStockSol1(prices): # O(n^2)
    maxProfit = 0;
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[j] - prices[i] > maxProfit:
                maxProfit = prices[j] - prices[i];
                
    return maxProfit;

def buySellStockSol2(prices): # O(n)
    currMin = float('inf');
    maxProfit = 0;
    for price in prices:
        currMin = min(currMin, price);
        profit = price - currMin;
        maxProfit = max(maxProfit, profit);
        
    return maxProfit;

if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4];
    print(buySellStockSol1(prices));
    print(buySellStockSol2(prices));