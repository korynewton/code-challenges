/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */

var isSymmetric = function (root) {
  const queue = [root, root];

  while (queue.length) {
    root1 = queue.shift();
    root2 = queue.shift();

    if (!root1 && !root2) continue;
    else if (!root1 || !root2) return false;
    else if (root1.val !== root2.val) return false;
    else {
      queue.push(root1.left, root2.right, root1.right, root2.left);
    }
  }

  return true;
};
