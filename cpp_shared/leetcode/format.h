#pragma once

#include <sstream>
#include <vector>

namespace leetcode::format
{
    constexpr auto to_str = [](std::vector<int> const &vec)
    {
        std::stringstream ss;

        for (size_t i = 0; i < vec.size(); i++)
        {
            if (i != 0)
            {
                ss << ",";
            }
            ss << vec[i];
        }

        return ss.str();
    };
}
