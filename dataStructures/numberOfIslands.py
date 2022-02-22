def numberOfIslandsSol1(grid):
    islands = 0;
    n = len(grid);    # height
    m = len(grid[0]); # width
    i = 0;
    j = 0;
    
    while i < n:
        j = 0;
        while j < m:
            if grid[i][j] == '1':
                islands += 1;
                discoverIsland(grid, i, j);
            j += 1;
        i += 1;
    
    return islands;

# DFS helper function
def discoverIsland(grid, i, j):
    n = len(grid);    # height
    m = len(grid[0]); # width
    if i >= n or j >= m or i < 0 or j < 0:
        return;
    if grid[i][j] == '0':
        return;
        
    grid[i][j] = '0';
    discoverIsland(grid, i+1, j);
    discoverIsland(grid, i, j+1);
    discoverIsland(grid, i-1, j);
    discoverIsland(grid, i, j-1);

if __name__ == '__main__':
    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ];
    print(numberOfIslandsSol1(grid));