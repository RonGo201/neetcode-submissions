#pragma GCC optimize("O3")

#include <vector>
#include <iostream>

class Solution {
public:
    bool searchMatrix(const std::vector<std::vector<int>>& matrix, int target) {
        if (matrix.empty() || matrix[0].empty()) return false;
        
        int m = matrix.size();
        int n = matrix[0].size();
        
        int left = 0;
        int right = m * n - 1;
        
        while (left <= right) {
            int mid = left + (right - left) / 2; 
            int mid_val = matrix[mid / n][mid % n];
            
            if (mid_val == target) {
                return true;
            } else if (mid_val < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        
        return false;
    }
};

static const int __ = []() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    std::cout.tie(NULL);
    return 0;
}();
