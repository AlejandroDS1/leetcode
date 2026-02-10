/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* mergeNodes(ListNode* head) {
               
        ListNode *output = new ListNode();
        ListNode *pointer = output; 
        
        int number = 0;
       
        while (head = head->next) {
            
            if (!head->next){
                pointer->val = number;
                return output;
            }

            if (!head->val) {
                pointer->val = number;
                // Get new node
                pointer->next = new ListNode();
                pointer = pointer->next;
                number = 0;
            }else {
                number += head->val;
            }
        }
        return output;
    }
};