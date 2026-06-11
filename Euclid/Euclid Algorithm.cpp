#include <iostream>

using namespace std;

int main()
{
	int a, b, q, r;

	cout << "Enter two integers to find the greatest common divisor: ";
	cin >> a >> b;

	do
	{
		q = a / b;
		r = a % b;
		a = b;
		b = r;

	}while (r != 0);

	cout << "The greatest common divisor is: " << a << endl;
	return 0;
}