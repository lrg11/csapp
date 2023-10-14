void backtrack(vector<string>& board, int row) {
 // 触发结束条件
 if (row == board.size()) {
 res.push_back(board);
 return;
 }
 
 int n = board[row].size();
 for (int col = 0; col < n; col++) {
 // 排除不合法选择
 if (!isValid(board, row, col)) {
 continue;
 }
 // 做选择
 board[row][col] = 'Q';
 // 进⼊下⼀⾏决策
 backtrack(board, row + 1);
 // 撤销选择
 board[row][col] = '.';
 }
}