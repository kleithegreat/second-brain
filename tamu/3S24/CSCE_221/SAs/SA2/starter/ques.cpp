#include <iostream>

using namespace std;

struct Node {
    int data;
    Node* left;
    Node* right;

    Node(int value) : data(value), left(nullptr), right(nullptr) {}
};

#ifndef ASCENDING_PATHS

// You can create helper functions for count ascending paths if required here

int countAscendingPaths(Node* root) {
    if (root == nullptr) return 0;
    if (root->left == nullptr && root->right == nullptr) return 1;

    int paths = 0;
    if (root->left != nullptr && root->left->data > root->data) {
        paths += countAscendingPaths(root->left);
    }

    if (root->right != nullptr && root->right->data > root->data) {
        paths += countAscendingPaths(root->right);
    }

    return paths;
}

#endif

#ifndef LEFT_LEAVES

// You can create helper functions for sum of left leaves if required here
int sumOfLeftLeavesHelper(Node* root, Node* parent) {
    if (root == nullptr) return 0;
    if (root->left == nullptr && root->right == nullptr && parent->left == root) return root->data;
    return sumOfLeftLeavesHelper(root->left, root) + sumOfLeftLeavesHelper(root->right, root);
}

int sumOfLeftLeaves(Node* root) {
    if (root == nullptr) return 0;
    return sumOfLeftLeavesHelper(root->left, root) + sumOfLeftLeavesHelper(root->right, root);
}

#endif

#ifndef TEST_MODE
int main() {
    cout << "Sample Test case 1" << endl;
    {
        Node root(3);
        Node left(4), right(5);
        Node leftLeft(7), leftRight(8), rightLeft(9), rightRight(10);
        Node leftRightLeft(3), rightLeftRight(12);

        root.left = &left, root.right = &right;
        left.left = &leftLeft, left.right = &leftRight, right.left = &rightLeft, right.right = &rightRight;
        leftRight.left = &leftRightLeft, rightLeft.right = &rightLeftRight;

        int sumReturned = sumOfLeftLeaves(&root);
        cout << "Testing sum of left leaves" << endl;
        cout << "Expected sum of left leaves: 10" << endl;
        cout << "Returned sum of left leaves: " << sumReturned << endl;

        cout << endl;

        int numAscendingPaths = countAscendingPaths(&root);
        cout << "Testing count ascending paths" << endl;
        cout << "Expected number of ascending paths: 3" << endl;
        cout << "Returned number of ascending paths: " << numAscendingPaths << endl;
    }
    cout << endl;
    cout << endl;

    cout << "Sample Test case 2" << endl;
    {
        Node root(3);
        Node right(4);
        Node rightLeft(5), rightRight(16);
        Node rightRightLeft(14);

        root.right = &right;
        right.left = &rightLeft, right.right = &rightRight;
        rightRight.left = &rightRightLeft;

        int sumReturned = sumOfLeftLeaves(&root);
        cout << "Testing sum of left leaves" << endl;
        cout << "Expected sum of left leaves: 19" << endl;
        cout << "Returned sum of left leaves: " << sumReturned << endl;

        cout << endl;

        int numAscendingPaths = countAscendingPaths(&root);
        cout << "Testing count ascending paths" << endl;
        cout << "Expected number of ascending paths: 1" << endl;
        cout << "Returned number of ascending paths: " << numAscendingPaths << endl;
    }

    cout << endl;
    cout << endl;

    cout << "Sample Test case 3" << endl;
    {
        Node root(2);
        Node left(1), right(3);
        Node leftRight(4), rightRight(5);
        Node leftRightLeft(6), rightRightRight(7);

        /*
                    2
                   / \
                  1   3
                  \    \
                   4    5
                  /      \
                6        7
        */

        root.left = &left, root.right = &right;
        left.right = &leftRight, right.right = &rightRight;
        leftRight.left = &leftRightLeft, rightRight.right = &rightRightRight;

        int sumReturned = sumOfLeftLeaves(&root);
        cout << "Testing sum of left leaves" << endl;
        cout << "Expected sum of left leaves: 6" << endl;
        cout << "Returned sum of left leaves: " << sumReturned << endl;

        cout << endl;

        int numAscendingPaths = countAscendingPaths(&root);
        cout << "Testing count ascending paths" << endl;
        cout << "Expected number of ascending paths: 1" << endl;
        cout << "Returned number of ascending paths: " << numAscendingPaths << endl;
    }
}
#endif