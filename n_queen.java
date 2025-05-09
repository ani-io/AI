import java.util.*;

public class n_queen {

    // ✅ Check if it's safe to place a queen at (row, col)
    public boolean isSafe(int row, int col, List<Integer> current) {
        for (int prevCol = 0; prevCol < col; prevCol++) {
            int prevRow = current.get(prevCol);
            
            // ❌ Same row or diagonal conflict
            if (prevRow == row || Math.abs(prevRow - row) == Math.abs(prevCol - col)) {
                return false;
            }
        }
        return true; // ✅ Safe position
    }

    // ✅ Recursive backtracking function to place queens column by column
    public void solve(int col, int n, List<Integer> current, List<List<String>> ans) {
        // 🔚 Base case: All queens are placed
        if (col == n) {
            ans.add(createBoard(current, n)); // Convert to board format and store
            return;
        }

        // 🔁 Try placing a queen in each row of the current column
        for (int row = 0; row < n; row++) {
            if (isSafe(row, col, current)) {
                current.add(row); // Place queen
                solve(col + 1, n, current, ans); // Recurse for next column
                current.remove(current.size() - 1); // 🔙 Backtrack
            }
        }
    }

    // ✅ Convert the current solution (list of row positions) to board format
    public List<String> createBoard(List<Integer> current, int n) {
        List<String> board = new ArrayList<>();
        
        // Loop through each column's queen position (row index)
        for (int row : current) {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < n; i++) {
                // Put 'Q' at the queen's position, '.' elsewhere
                sb.append(i == row ? 'Q' : '.');
            }
            board.add(sb.toString());
        }
        return board;
    }

    // ✅ Main function to solve the N-Queens problem
    public List<List<String>> solveNQueens(int n) {
        List<List<String>> ans = new ArrayList<>();
        List<Integer> current = new ArrayList<>();
        solve(0, n, current, ans); // Start from column 0
        return ans;
    }

    // 🔽 Driver Code: Take input, solve, and display all solutions
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // 📥 Input the value of N
        System.out.print("Enter the value of N for N-Queens: ");
        int n = scanner.nextInt();
        
        n_queen solution = new n_queen();
        List<List<String>> solutions = solution.solveNQueens(n); // Solve the problem

        // 📤 Output the total number of solutions and each configuration
        System.out.println("Total solutions: " + solutions.size());
        int count = 1;
        for (List<String> board : solutions) {
            System.out.println("Solution " + count + ":");
            for (String row : board) {
                System.out.println(row);
            }
            System.out.println(); // Separate each board
            count++;
        }

        scanner.close();
    }
}
