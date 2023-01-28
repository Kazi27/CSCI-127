//Name: Kazi Sameen Anwar
//Email: kazisameen.anwar39@myhunter.cuny.edu
//Date: December 4, 2021
//this is the last cs127 assignemnt

#include <string>
#include <iostream>
using namespace std;

int main()
{
  int n;
  int x;
  int b = 16;
  cout << "Enter a number: ";
  cin >> n;
  if (n < 0)
  {
    cout << 1;
    x = 32 + n;
  }
  else if (n >= 0)
  {
    cout << 0;
    x = n;
  }
  while (b > 0.5)
  {
    if (x >= b)
    {
      cout << 1;
    }
    else 
    {
      cout << 0;
    }
    x = x % b;
    b = b/2;
  }
  cout << "\n";
}