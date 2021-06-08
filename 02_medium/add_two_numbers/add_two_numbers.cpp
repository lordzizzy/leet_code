// https://leetcode.com/problems/add-two-numbers/

// Add Two Numbers

// You are given two non-empty linked lists representing two non-negative
// integers. The digits are stored in reverse order, and each of their nodes
// contains a single digit. Add the two numbers and return the sum as a linked
// list.

// You may assume the two numbers do not contain any leading zero, except the
// number 0 itself.

// Example 1:
// Input: l1 = [2,4,3], l2 = [5,6,4]
// Output: [7,0,8]
// Explanation: 342 + 465 = 807.

// Example 2:
// Input: l1 = [0], l2 = [0]
// Output: [0]

// Example 3:
// Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
// Output: [8,9,9,9,0,0,0,1]

// Constraints:
// The number of nodes in each linked list is in the range [1, 100].
// 0 <= Node.val <= 9
// It is guaranteed that the list represents a number that does not have
// leading zeros.

#include "stdafx.h"

using namespace std;

// Definition for singly-linked list.
struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

ListNode *createLinkedList(vector<int> vec)
{
    ListNode *pPrev = nullptr;
    ListNode *pHead = nullptr;

    for (auto num : vec) {
        ListNode *pNode = new ListNode(num, nullptr);
        // save head
        if (!pPrev) {
            pHead = pNode;
        }
        else {
            pPrev->next = pNode;
        }
        pPrev = pNode;
    }

    return pHead;
}

ListNode *addTwoNumbers(ListNode *l1, ListNode *l2)
{
    ListNode *pHead = nullptr;
    ListNode *pPrev = nullptr;

    int carry = 0;

    while (l1 || l2) {
        int val = 0;
        val += carry;

        if (l1) {
            val += l1->val;
            l1 = l1->next;
        }

        if (l2) {
            val += l2->val;
            l2 = l2->next;
        }

        if (val >= 10) {
            val -= 10;
            carry = 1;
        }
        else {
            carry = 0;
        }

        ListNode *pNode = new ListNode(val, nullptr);
        if (!pPrev) {
            pHead = pNode;
        }
        else {
            pPrev->next = pNode;
        }
        pPrev = pNode;

        // last node
        if (!l1 && !l2 && carry) {
            pNode->next = new ListNode(1, nullptr);
        }
    }

    return pHead;
}

void printLinkedList(const ListNode *pList)
{
    while (pList) {
        fmt::print("{}{}", pList->val, (pList->next ? "->" : ""));
        pList = pList->next;
    }
    cout << endl;
}

int main()
{
    auto pList1 = createLinkedList({2, 4, 3});
    auto pList2 = createLinkedList({5, 6, 4});

    printLinkedList(pList1);
    printLinkedList(pList2);

    auto pResultList = addTwoNumbers(pList1, pList2);

    printLinkedList(pResultList);

    return 0;
}
