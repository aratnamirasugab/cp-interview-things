#include <iostream>
#include <cmath>

using namespace std;

int main(void)
{
	int q;
	cin >> q;
	
	int n = 0;
	int total = 0;
	int number = 0;
	
	for(int i = 0 ; i < q ; i++){
		cin >> n;
		for(int j = 0 ; j < n ; j++){
			cin >> number;
			total += number;
		}	
		total = ceil(total/n);
		cout << total;
		total = 0;
	}
}
