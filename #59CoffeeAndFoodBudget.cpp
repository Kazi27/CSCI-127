//Name: Kazi Sameen Anwar
//Email: kazisameen.anwar39@myhunter.cuny.edu
//Date: December 4, 2021
//this makes a food budget

#include <string>
#include <iostream>
using namespace std;

int main()
{
  float monthlybudget;
  float coffee;
  cout << "Enter your monthly budget for food and coffee: ";
  cin >> monthlybudget;
  cout << "How much are you spending in a week for coffee: ";
  cin >> coffee;
  for (int x = 1; x < 5; x++)
    {
        monthlybudget -= coffee;
        cout << "Budget left after week " << x << '\t' << monthlybudget << '\n';
    }
}