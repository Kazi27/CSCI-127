//Name: Kazi Sameen Anwar
//Email: kazisameen.anwar39@myhunter.cuny.edu
//Date: November 30, 2021
//this coverts counts down

#include <string>
#include <iostream>
using namespace std;

int main()
{
  int number;
  string word;
  cout << "Please enter a number: ";
  cin >> number;
  cout << "Please type a word: ";
  cin >> word;
  while (number > 0)
  {
    cout << number << ",\n";
    --number;
  }
  cout << "Time for " << word << "!";
  return 0;
}