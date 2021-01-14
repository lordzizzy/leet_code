
#include <vector>
#include <iostream>

using namespace std;

//   Definition for singly-linked list.
struct ListNode {
      int val;
      ListNode *next;
      ListNode() : val(0), next(nullptr) {}
      ListNode(int x) : val(x), next(nullptr) {}
      ListNode(int x, ListNode *next) : val(x), next(next) {}
 };
 

ListNode* createLinkedList(vector<int> vec) {
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

ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {    

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
        cout << pList->val << (pList->next ? "," : "");
        pList = pList->next;
    }

    cout << endl;
}


int main()
{
    auto pList1 = createLinkedList({9, 9});
    auto pList2 = createLinkedList({9});

    printLinkedList(pList1);
    printLinkedList(pList2);

    auto pResultList = addTwoNumbers(pList1, pList2);

    printLinkedList(pResultList);

    return 0;
}
