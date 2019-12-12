//https://www.codechef.com/problems/FLOW010

#include <iostream>
#include <locale>

using namespace std;

int main(void)
{
    int T;
    cin >> T;
    char ch;

    while(T > 0)
    {
        cin >> ch;
        ch = tolower(ch);

        if(ch == 'b')cout << "BattleShip\n";
        else if(ch == 'c')cout << "Cruiser\n";
        else if(ch == 'd') cout << "Destroyer\n";
        else if(ch == 'f') cout << "Frigate\n";

        T--;
    }
}
