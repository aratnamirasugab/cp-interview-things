#include <iostream>
#include <algorithm>
#include <math.h>

using namespace std;

int main(void)
{
    int n, m;
    cin >> n >> m;

    int low, high;
    int puzzle[m];

    for(int i = 0 ; i < m ; i++){
        cin >> puzzle[i];
    }

    //sort the puzzle
    sort(puzzle, puzzle+m);

    int result = 999;
    for(int i = n ; i <= m ; i++){
        result = min(result, abs(puzzle[i-1]-puzzle[i-n]));
    }

    cout << result;
}
