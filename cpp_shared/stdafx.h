#pragma once

#define FMT_HEADER_ONLY

#include "leetcode/format.h"

#include <fmt/color.h>
#include <fmt/core.h>

#include <functional>
#include <iostream>
#include <string_view>

constexpr auto pass_color = fmt::fg(fmt::color::green);
constexpr auto fail_color = fmt::fg(fmt::color::red);