
#include <iostream>
#include <vector>

std::vector<int> two_sum(std::vector<int> nums, const int target)
{
    for (int i = 0; i < nums.size(); ++i) {
        for (int j = i + 1; j < nums.size(); ++j) {
            if (nums[i] + nums[j] == target) {
                return {i, j};
            }
        }
    }

    return {};
}

int main()
{
    std::vector<int> nums = {1, 2, 3, 4};

    auto idx_vec = two_sum(nums, 7);

    for (auto idx : idx_vec) {
        std::cout << idx << std::endl;
    }    

    return 0;
}