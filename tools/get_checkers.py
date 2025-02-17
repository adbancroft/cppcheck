import glob
import re

print("""/*
 * Cppcheck - A tool for static C/C++ code analysis
 * Copyright (C) 2007-2023 Cppcheck team.
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

#pragma once

#include <map>
#include <string>
#include <vector>

namespace checkers {

static std::map<std::string, std::string> allCheckers{""")

for filename in glob.glob('../lib/*.cpp'):
    for line in open(filename,'rt'):
        res = re.match(r'[ \t]*logChecker\(\s*"([:_a-zA-Z0-9]+)"\s*\);.*', line)
        if res is None:
            continue
        req = ''
        if line.find('//')>0:
            req = line[line.find('//')+2:].strip()
        print('    {"%s","%s"},' % (res.group(1), req))
print("};\n\n")

print('static std::map<std::string, std::string> premiumCheckers{')

premium_checkers = """
$ grep logChecker *.cpp | sed 's/.*logChecker/logChecker/'
logChecker("CheckBufferOverrun::addressOfPointerArithmetic"); // warning
logChecker("CheckBufferOverrun::negativeBufferSizeCheckedNonZero"); // warning
logChecker("CheckBufferOverrun::negativeBufferSizeCheckedNonZero"); // warning
logChecker("CheckHang::infiniteLoop");
logChecker("CheckHang::infiniteLoopContinue");
logChecker("CheckOther::arrayPointerComparison"); // style
logChecker("CheckOther::knownResult"); // style
logChecker("CheckOther::lossOfPrecision"); // style
logChecker("CheckOther::pointerCast"); // style
logChecker("CheckOther::reassignInLoop"); // style
logChecker("CheckOther::unreachableCode"); // style
logChecker("CheckStrictAlias::strictAliasCondition"); // warning
logChecker("CheckUninitVar::uninitvar");
logChecker("CheckUninitVar::uninitmember");
logChecker("CheckUnusedVar::unreadVariable"); // style
logChecker("CheckUnusedVar::unusedPrivateMember"); // style
"""

for line in premium_checkers.split('\n'):
    res = re.match(r'logChecker\("([:_a-zA-Z0-9]+)"\);.*', line)
    if res is None:
        continue
    if line.find('//') > 0:
        req = line[line.find('//')+2:].strip()
    else:
        req = ''
    print('    {"%s","%s"},' % (res.group(1), req))

print('};\n\n')

print("""
struct MisraInfo {
    int a;
    int b;
    const char* str;
    int amendment;
};

const char Req[] = "Required";
const char Adv[] = "Advisory";
const char Man[] = "Mandatory";

const MisraInfo misraC2012Rules[] =
{
    {1,1,Req,0},
    {1,2,Adv,0},
    {1,3,Req,0},
    {1,4,Req,2}, // amendment 2
    {1,5,Req,3}, // Amendment 3
    {2,1,Req,0},
    {2,2,Req,0},
    {2,3,Adv,0},
    {2,4,Adv,0},
    {2,5,Adv,0},
    {2,6,Adv,0},
    {2,7,Adv,0},
    {2,8,Adv,0},
    {3,1,Req,0},
    {3,2,Req,0},
    {4,1,Req,0},
    {4,2,Adv,0},
    {5,1,Req,0},
    {5,2,Req,0},
    {5,3,Req,0},
    {5,4,Req,0},
    {5,5,Req,0},
    {5,6,Req,0},
    {5,7,Req,0},
    {5,8,Req,0},
    {5,9,Adv,0},
    {6,1,Req,0},
    {6,2,Req,0},
    {6,3,Req,0},
    {7,1,Req,0},
    {7,2,Req,0},
    {7,3,Req,0},
    {7,4,Req,0},
    {7,5,Man,0},
    {7,6,Req,0},
    {8,1,Req,0},
    {8,2,Req,0},
    {8,3,Req,0},
    {8,4,Req,0},
    {8,5,Req,0},
    {8,6,Req,0},
    {8,7,Adv,0},
    {8,8,Req,0},
    {8,9,Adv,0},
    {8,10,Req,0},
    {8,11,Adv,0},
    {8,12,Req,0},
    {8,13,Adv,0},
    {8,14,Req,0},
    {8,15,Req,0},
    {8,16,Adv,0},
    {8,17,Adv,0},
    {9,1,Man,0},
    {9,2,Req,0},
    {9,3,Req,0},
    {9,4,Req,0},
    {9,5,Req,0},
    {9,6,Req,0},
    {9,7,Man,0},
    {10,1,Req,0},
    {10,2,Req,0},
    {10,3,Req,0},
    {10,4,Req,0},
    {10,5,Adv,0},
    {10,6,Req,0},
    {10,7,Req,0},
    {10,8,Req,0},
    {11,1,Req,0},
    {11,2,Req,0},
    {11,3,Req,0},
    {11,4,Adv,0},
    {11,5,Adv,0},
    {11,6,Req,0},
    {11,7,Req,0},
    {11,8,Req,0},
    {11,9,Req,0},
    {11,10,Req,0},
    {12,1,Adv,0},
    {12,2,Req,0},
    {12,3,Adv,0},
    {12,4,Adv,0},
    {12,5,Man,1}, // amendment 1
    {12,6,Req,4}, // amendment 4
    {13,1,Req,0},
    {13,2,Req,0},
    {13,3,Adv,0},
    {13,4,Adv,0},
    {13,5,Req,0},
    {13,6,Man,0},
    {14,1,Req,0},
    {14,2,Req,0},
    {14,3,Req,0},
    {14,4,Req,0},
    {15,1,Adv,0},
    {15,2,Req,0},
    {15,3,Req,0},
    {15,4,Adv,0},
    {15,5,Adv,0},
    {15,6,Req,0},
    {15,7,Req,0},
    {16,1,Req,0},
    {16,2,Req,0},
    {16,3,Req,0},
    {16,4,Req,0},
    {16,5,Req,0},
    {16,6,Req,0},
    {16,7,Req,0},
    {17,1,Req,0},
    {17,2,Req,0},
    {17,3,Man,0},
    {17,4,Man,0},
    {17,5,Adv,0},
    {17,6,Man,0},
    {17,7,Req,0},
    {17,8,Adv,0},
    {17,9,Man,0},
    {17,10,Req,0},
    {17,11,Adv,0},
    {17,12,Adv,0},
    {17,13,Req,0},
    {18,1,Req,0},
    {18,2,Req,0},
    {18,3,Req,0},
    {18,4,Adv,0},
    {18,5,Adv,0},
    {18,6,Req,0},
    {18,7,Req,0},
    {18,8,Req,0},
    {18,9,Req,0},
    {18,10,Man,0},
    {19,1,Man,0},
    {19,2,Adv,0},
    {20,1,Adv,0},
    {20,2,Req,0},
    {20,3,Req,0},
    {20,4,Req,0},
    {20,5,Adv,0},
    {20,6,Req,0},
    {20,7,Req,0},
    {20,8,Req,0},
    {20,9,Req,0},
    {20,10,Adv,0},
    {20,11,Req,0},
    {20,12,Req,0},
    {20,13,Req,0},
    {20,14,Req,0},
    {21,1,Req,0},
    {21,2,Req,0},
    {21,3,Req,0},
    {21,4,Req,0},
    {21,5,Req,0},
    {21,6,Req,0},
    {21,7,Req,0},
    {21,8,Req,0},
    {21,9,Req,0},
    {21,10,Req,0},
    {21,11,Req,0},
    {21,12,Adv,0},
    {21,13,Man,1}, // Amendment 1
    {21,14,Req,1}, // Amendment 1
    {21,15,Req,1}, // Amendment 1
    {21,16,Req,1}, // Amendment 1
    {21,17,Req,1}, // Amendment 1
    {21,18,Man,1}, // Amendment 1
    {21,19,Man,1}, // Amendment 1
    {21,20,Man,1}, // Amendment 1
    {21,21,Req,3}, // Amendment 3
    {21,22,Man,3}, // Amendment 3
    {21,23,Req,3}, // Amendment 3
    {21,24,Req,3}, // Amendment 3
    {21,25,Req,4}, // Amendment 4
    {21,26,Req,4}, // Amendment 4
    {22,1,Req,0},
    {22,2,Man,0},
    {22,3,Req,0},
    {22,4,Man,0},
    {22,5,Man,0},
    {22,6,Man,0},
    {22,7,Req,1}, // Amendment 1
    {22,8,Req,1}, // Amendment 1
    {22,9,Req,1}, // Amendment 1
    {22,10,Req,1}, // Amendment 1
    {22,11,Req,4}, // Amendment 4
    {22,12,Man,4}, // Amendment 4
    {22,13,Req,4}, // Amendment 4
    {22,14,Man,4}, // Amendment 4
    {22,15,Req,4}, // Amendment 4
    {22,16,Req,4}, // Amendment 4
    {22,17,Req,4}, // Amendment 4
    {22,18,Req,4}, // Amendment 4
    {22,19,Req,4}, // Amendment 4
    {22,20,Man,4}, // Amendment 4
    {23,1,Adv,3}, // Amendment 3
    {23,2,Req,3}, // Amendment 3
    {23,3,Adv,3}, // Amendment 3
    {23,4,Req,3}, // Amendment 3
    {23,5,Adv,3}, // Amendment 3
    {23,6,Req,3}, // Amendment 3
    {23,7,Adv,3}, // Amendment 3
    {23,8,Req,3}, // Amendment 3
};

static std::map<std::string, std::string> misraRuleSeverity{
    {"1.1", "error"}, //{"syntaxError", "unknownMacro"}},
    {"1.3", "error"}, //most "error"
    {"2.1", "style"}, //{"alwaysFalse", "duplicateBreak"}},
    {"2.2", "style"}, //{"alwaysTrue", "redundantCondition", "redundantAssignment", "redundantAssignInSwitch", "unreadVariable"}},
    {"2.6", "style"}, //{"unusedLabel"}},
    {"2.8", "style"}, //{"unusedVariable"}},
    {"5.3", "style"}, //{"shadowVariable"}},
    {"8.3", "style"}, //{"funcArgNamesDifferent"}}, // inconclusive
    {"8.13", "style"}, //{"constPointer"}},
    {"9.1", "error"}, //{"uninitvar"}},
    {"14.3", "style"}, //{"alwaysTrue", "alwaysFalse", "compareValueOutOfTypeRangeError", "knownConditionTrueFalse"}},
    {"13.2", "error"}, //{"unknownEvaluationOrder"}},
    {"13.6", "style"}, //{"sizeofCalculation"}},
    {"17.4", "error"}, //{"missingReturn"}},
    {"17.5", "warning"}, //{"argumentSize"}},
    {"18.1", "error"}, //{"pointerOutOfBounds"}},
    {"18.2", "error"}, //{"comparePointers"}},
    {"18.3", "error"}, //{"comparePointers"}},
    {"18.6", "error"}, //{"danglingLifetime"}},
    {"19.1", "error"}, //{"overlappingWriteUnion", "overlappingWriteFunction"}},
    {"20.6", "error"}, //{"preprocessorErrorDirective"}},
    {"21.13", "error"}, //{"invalidFunctionArg"}},
    {"21.17", "error"}, //{"bufferAccessOutOfBounds"}},
    {"21.18", "error"}, //{"bufferAccessOutOfBounds"}},
    {"22.1", "error"}, //{"memleak", "resourceLeak", "memleakOnRealloc", "leakReturnValNotUsed", "leakNoVarFunctionCall"}},
    {"22.2", "error"}, //{"autovarInvalidDeallocation"}},
    {"22.3", "error"}, //{"incompatibleFileOpen"}},
    {"22.4", "error"}, //{"writeReadOnlyFile"}},
    {"22.6", "error"}, //{"useClosedFile"}}
};

}

""")


