#include <iostream>

using namespace std;

long consecutiveSum(long sum)
{
    int totalWays = 0;
    int sumTotal = 0;
    int j = 1;

    for(int i = 1 ; i <= sum ; i++){
        sumTotal = 0;

        while(sumTotal != sum){
            sumTotal += j;
            j++;
        }
        totalWays++;
    }

    return totalWays;
}

int main(void){

    int angka;
    cin >> angka;

    long res = consecutiveSum(angka);

    cout << res;
}
