#include <iostream>
#include <vector>
using namespace std;

template <class T>
class Tree {
	private:
		class BST {
			public:
				T data = {};
				BST* right = nullptr;
				BST* left = nullptr;
				BST(T newData = {}, BST* newRight = nullptr, BST* newLeft = nullptr) {
					data = newData, right = newRight, left = newLeft;
				}
				~BST() {
					delete left;
					delete right;
				}
				//this, left, right
				void preorder(vector<T> &order) { 
					order.push_back(data);
					if(left) left->preorder(order);
					if(right) right->preorder(order);
				}
				//left, this, right
				void inorder(vector<T> &order) { 
					if(left) left->preorder(order);
					order.push_back(data);
					if(right) right->preorder(order);
				}
				//left, right, this
				void postorder(vector<T> &order) { 
					if(left) left->preorder(order);
					if(right) right->preorder(order);
					order.push_back(data);
				}
		} *root = nullptr;

	public:
		~Tree() {
			delete root;
		}
		void remove(T oldData) {
			BST* temp = root;
			BST* parent = temp;
			while(temp) {
				if(temp->data == oldData) {
					//do things
					if(temp == root) {
						return;
					}
					if(temp->right && temp->left) {
						//figure out which one is better
					} else if (temp->left) {
						parent->left = temp->left;
					} else if (temp->right) {
						parent->right = temp->right;
					}
					delete temp;
					return;
				} else if (temp->data < oldData) {
					parent = temp;
					temp = temp->left;
				} else if (temp->data > oldData) {
					parent = temp;
					temp = temp->right;
				}
			}
		}

		void insert(T newData) {
			if(root) {
				BST* temp = root;
				while(temp) {
					if(newData == temp->data) return;

					else if (newData < temp->data) {//left
						if(!temp->left) {
							temp->left = new BST(newData);
						} else temp = temp->left;

					} else {//right
						if(!temp->right) {
							temp->right = new BST(newData);
						} else temp = temp->right;
					}
				}
			} else {
				root = new BST(newData);
			}
		}
		bool search(T data) {
			if(!root) return false;
			BST* temp = root;
			while (temp) {
				if(data == temp->data) return true;
				else if(data < temp->data) temp = temp->left;
				else if(data > temp->data) temp = temp->right;
			}
			return false;
		}
		vector<T> preorder() {
			vector<T> order;
			root->preorder(order);
			return order;
		}
		vector<T> postorder() {
			vector<T> order;
			root->postorder(order);
			return order;
		}
		vector<T> inorder() {
			vector<T> order;
			root->inorder(order);
			return order;
		}
};

int main() {
	Tree<int> bst;
	bst.insert(50);
	bst.insert(30);
	bst.insert(70);
	bst.insert(40);
	bst.insert(65);
	bst.insert(80);
	bst.insert(10);
	vector<int> preordered = bst.preorder();
	for(int i : preordered) {
		cout << i << ",";
	}
	cout << endl;
	vector<int> inordered = bst.inorder();
	for(int i : inordered) {
		cout << i << ",";
	}
	cout << endl;
	vector<int> postordered = bst.postorder();
	for(int i : postordered) {
		cout << i << ",";
	}
	cout << endl;
}
