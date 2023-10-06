#include <stdio.h>
#define MAXSIZE 9
#define MARK 1
#define UNMARK 0

typedef struct Point {int x, y;} point;
point direction[8] = {{1, -2}, {2, -1}, {2, 1}, {1, 2}, {-1, 2}, {-2, 1}, {-2, -1}, {-1, -2}};
int board[MAXSIZE][MAXSIZE], path[MAXSIZE][MAXSIZE];

int knightTour (int m, int n, point pos, int counter){
    int i;
    point next;

    if (counter == m * n)
        return 1;   // 투어 끝
    
    for (i = 0; i < 8; i++)
    {
        next.x = pos.x + direction[i].x;
        next.y = pos.y + direction[i].y;

        if ( next.x > 0 && next.x <= n &&
             next.y > 0 && next.y <= m &&
             board[next.y][next.x] != MARK ) 
        {
            board[next.y][next.x] = MARK;
            path[next.y][next.x] = counter + 1;

            if (knightTour(m, n, next, counter+1))
                return 1;
            
            board[next.y][next.x] = UNMARK;
        }

    }

    return 0;   // 다 못 갈 떄
}

void printTour(int m, int n){
    for (int i=1; i<=m; i++){
        for (int j=1; j<=n; j++){
            printf("%d ", path[i][j]);}
        printf("\n");
    }
}

int main() {
    int numTestCases;
    scanf("%d", &numTestCases);

    for (int num=0; num<numTestCases; ++num){
        int m, n, s, t;
        point start;

        scanf("%d %d %d %d", &m, &n, &s, &t);

        for (int i=1; i<=m; i++){
            for (int j=1; j<=n; j++){
                board[i][j] = UNMARK;
                path[i][j] = 0;
            }
        }
        
        start.y = s;
        start.x = t;

        board[start.y][start.x] = MARK;
        path[start.y][start.x] = 1;

        if (knightTour(m, n, start, 1)){
            printf("%d\n", 1);
            printTour(m, n);
        }
        else {printf("%d\n", 0);} 
    }
    return 0;
}