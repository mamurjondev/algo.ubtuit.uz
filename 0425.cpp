#include <bits/stdc++.h>
using namespace std;
typedef long int li;
typedef long long ll;
typedef long double ld;
#define get_time(x) clock_t x = clock()
#define set_time(a, b) printf("runtime: %.2f sec", (double) (b - a) / 1000)
#define setf(x) setprecision(x) << fixed
#define all(x) x.begin(), x.end()
#define MOD 1000000007
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define lt last
#define lf '\n'
#define N 10000
#define M 10000
void Solve()
{
	int n, k = 0;
	double s = 0;
	cin >> n;
	int a[n];
	for (int i = 0; i < n; i++)
		cin >> a[i];
	for (int i = 0; i < n; i++)
		if (a[i] % 2)
		{
			s += a[i], k++;
		}
	cout << setf(2) << s / k << '\n';
}
int main()
{
	int z = 1;
	while (z --> 0)
		  Solve();
}
