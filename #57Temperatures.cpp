//Name: Kazi Sameen Anwar
//Email: kazisameen.anwar39@myhunter.cuny.edu
//Date: November 30, 2021
//this coverts counts down

#include <string>
#include <iostream>
using namespace std;

int main()
{
  int num;
  cout << "Enter the temperature: ";
  cin >> num;
  if (num == 32 or num < 32)
  {
    cout << "It's freezing!\n";
  }
  if (num < 68 and num > 32)
  {
    cout << "It's cold!\n";
  }
  if (num == 68 or (num > 68 and num < 73))
  {
    cout << "It's warm!\n";
  }
  if (num > 73)
  {
    cout << "It's hot!\n";
  }
  return 0;
}