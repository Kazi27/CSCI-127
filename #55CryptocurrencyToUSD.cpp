//Name: Kazi Sameen Anwar
//Email: kazisameen.anwar39@myhunter.cuny.edu
//Date: November 30, 2021
//this coverts imaginary money to real money

#include <iomanip>
#include <iostream>
using namespace std;

int main()
{
  double amount;
  double btc;
  double eth;
  double doge;

  cout << "Enter amount in cryptocurrency: ";
  cin >> amount;
  
  btc = 31901.19;
  eth = 1901.54;
  doge = 0.179733;

  cout << fixed << setprecision(2);
  
  cout << amount << " BTC in USD: $" << btc * amount << "\n";
  cout << amount << " ETH in USD: $" << eth * amount << "\n";
  cout << amount << " DOGE in USD: $" << doge * amount << "\n";
  return 0;
}