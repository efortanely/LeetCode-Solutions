//  Definition for singly-linked list.
function ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function (head) {
  let reverse = (curr, prev) => {
    if (!curr) {
      return null;
    }

    let next = curr.next;
    curr.next = prev;

    if (next) {
      return reverse(next, curr);
    }

    return curr;
  };

  return reverse(head, null);
};

let head = new ListNode(
  1,
  new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5, null))))
);
ans = reverseList(head);
console.log(ans);
