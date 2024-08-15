//  Definition for singly-linked list.
function ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}

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

var copyList = function (head) {
  if (!head) {
    return null;
  }

  let newHead = new ListNode(head.val);
  let curr = head.next;
  let prev = newHead;

  while (curr) {
    let node = new ListNode(curr.val);
    prev.next = node;
    prev = prev.next;
    curr = curr.next;
  }

  return newHead;
};

var pairSum = function (head) {
  let slow = head;
  let fast = head;
  let reversedCurr = reverseList(copyList(head));
  let maxTwinSum = Number.MIN_SAFE_INTEGER;

  while (fast?.next) {
    maxTwinSum = Math.max(maxTwinSum, slow.val + reversedCurr.val);
    slow = slow.next;
    reversedCurr = reversedCurr.next;
    fast = fast.next?.next;
  }

  return maxTwinSum;
};

let head = new ListNode(
  4,
  new ListNode(2, new ListNode(2, new ListNode(3, null)))
);
ans = pairSum(head);
console.log(ans);
