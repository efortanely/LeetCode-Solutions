//  Definition for singly-linked list.
function ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var oddEvenList = function (head) {
  let counter = 1;
  let oddHead = null;
  let oddTail = null;
  let evenHead = null;
  let evenTail = null;
  let curr = head;

  while (curr) {
    if (counter % 2 == 0) {
      if (!evenHead) {
        evenHead = new ListNode(curr.val);
        evenTail = evenHead;
      } else {
        evenTail.next = new ListNode(curr.val);
        evenTail = evenTail.next;
      }
    } else {
      if (!oddHead) {
        oddHead = new ListNode(curr.val);
        oddTail = oddHead;
      } else {
        oddTail.next = new ListNode(curr.val);
        oddTail = oddTail.next;
      }
    }

    curr = curr.next;
    counter++;
  }

  if (oddTail) {
    oddTail.next = evenHead;
  }

  return oddHead;
};

let head = new ListNode(
  1,
  new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5, null))))
);
ans = oddEvenList(head);
console.log(ans);
