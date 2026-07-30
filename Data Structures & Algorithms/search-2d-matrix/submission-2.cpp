class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if (matrix.empty() || matrix[0].empty()) return false;
        
        int m = matrix.size();
        int n = matrix[0].size();
        
        int top = 0, bot = m - 1;
        int row = -1;
        
        while (top <= bot) {
            int mid = top + (bot - top) / 2;
            if (target > matrix[mid].back()) {
                top = mid + 1;
            } else if (target < matrix[mid].front()) {
                bot = mid - 1;
            } else {
                row = mid;
                break;
            }
        }
        
        if (row == -1) return false;
        
        int left = 0, right = n - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (matrix[row][mid] == target) {
                return true;
            } else if (matrix[row][mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        
        return false;
    }
};