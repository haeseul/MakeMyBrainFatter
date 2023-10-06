#include <stdio.h>
#include <stdlib.h>

struct node
{
    int data;
    struct node* left;
    struct node* right;
};

int max(int a, int b);
void insert(struct node** root, int data);
void preOrder(struct node* root);
void inOrder(struct node* root);
void postOrder(struct node* rood);
int size(struct node* root);
int height(struct node* root);
int sumOfWeight(struct node* root);
int maxPathWeight(struct node* root);
void mirror(struct node** root);
void destruct(struct node** root);

int main() {
    int numTestCases;
    scanf("%d", &numTestCases);
    while (numTestCases--) {
        int num, i;
        struct node* root = NULL;

        scanf("%d", &num);
        for (i=0; i<num; i++){
            int data;
            scanf("%d", &data);
            insert(&root, data);
        }
        // printf("%d\n", size(root));
        // printf("%d\n", height(root));
        // printf("%d\n", sumOfWeight(root));
        // printf("%d\n", maxPathWeight(root));
        // mirror(&root);
        preOrder(root); printf("\n");
        inOrder(root); printf("\n");
        postOrder(root); printf("\n");
        destruct(&root);
        if (root == NULL)
            printf("0\n");
        else
            printf("1\n");

    }
    return 0;
}

int max(int a, int b){
    return (a>b)? a: b;
}

// 데이터삽입
void insert(struct node** root, int data) {
    if (*root == NULL) {
        *root = (struct node*)malloc(sizeof(struct node));
        (*root)->data = data;
        (*root)->left = NULL;
        (*root)->right = NULL;
    }
    else if (data < (*root)->data){
        insert(&((*root)->left), data);
    }
    else if (data > (*root)->data){
        insert(&((*root)->right), data);
    }
}

// 전위탐색
void preOrder(struct node* root) {
    if (root == NULL) return;
    else {
        printf("%d ", root->data);
        preOrder(root->left);
        preOrder(root->right);
    }
}

// 중위탐색
void inOrder(struct node* root) {
    if (root == NULL) return;
    else {
        inOrder(root->left);
        printf("%d ", root->data);
        inOrder(root->right);
    }
}

// 후위탐색
void postOrder(struct node* root) {
    if (root == NULL) return;
    else {
        postOrder(root->left);
        postOrder(root->right);
        printf("%d ", root->data);
    }
}

// 노드의 개수
// int size(struct node* root) {

// }

// // 높이 (height)
// int height(struct node* root) {
    
// }

// // 미러 이지미로 변환
// void mirror(struct node** root) {
    
// }

// // 노드에 저장된 데이터 값의 합
// int sumOfWeight(struct node* root) {
    
// }

// // 루트노드부터 단말노드까지의 경로 상의 데이터 최대합
// int maxPathWeight(struct node* root) {
    
// }

// 트리노드의 동적 메모리 해제
void destruct(struct node** root) {
    if(*root == NULL) return;
    destruct(&((*root)->left));
    destruct(&((*root)->right));
    free(*root);
    *root = NULL;
}