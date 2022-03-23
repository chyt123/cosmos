
public class NumberofIslands {
    public static int numIslands(char[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int num = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '1') {
                    grid[i][j] = '2';
                    num += 1;
                    dps(grid, i, j, m, n);
                }
            } 
        }
        return num;
    }
    private static void dps(char[][] grid, int x, int y, int m, int n) {
        int[] dir = {1, 0, -1, 0, 1};
        for (int i = 0; i < 4; i++) {
            int x1 = dir[i] + x;
            int y1 = dir[i + 1] + y;
            if (0 <= x1 && x1 < m && 0 <= y1 && y1 < n && grid[x1][y1] == '1') {
                grid[x1][y1] = '2';
                dps(grid, x1, y1, m, n);
            }
        }
    }

    public static void main(String[] args) {
        char[][] grid;
        grid = new char[][]{
            {'1', '1', '1', '1', '0'},
            {'1', '1', '0', '1', '0'},
            {'1', '1', '0', '0', '0'},
            {'0', '0', '0', '0', '0'}
        };
        System.out.println(numIslands(grid));

        grid = new char[][]{
            {'1','1','0','0','0'},
            {'1','1','0','0','0'},
            {'0','0','1','0','0'},
            {'0','0','0','1','1'}
        };
        System.out.println(numIslands(grid));
    }
}

