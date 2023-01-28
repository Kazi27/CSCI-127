//Name: Kazi Sameen Anwar
//Email: kazisameen.anwar39@myhunter.cuny.edu
//Date: December 3, 2021
//this makes a trapezoid

#include <string>
#include <iostream>
using namespace std;

int main()
{
  int n;
  int i;
  int j;
  int k;
  int l;
  string c;
  cout << "Please enter a number: ";
  cin >> n;
  cout << "Please enter a character: ";
  cin >> c;

  for (i = 1; i <= n; i++)
  {
    for (j = 1; j <= i; j++)
    {
      cout << c;
    }
    cout << endl;
  }
  for (k = 0; k < n; k++)
  {
    for (l = 0; l < n; l++)
    {
      cout << c;
    }
    cout << endl;
  }
}