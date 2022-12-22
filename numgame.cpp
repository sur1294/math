#include <iostream>
#include <cstdlib>

using namespace std;

int main()
{
char input;
int num;
// Generate a random number between 1 and 100
num = rand() % 100 + 1;

// Keep the game running until the player gets a question wrong
while (true)
{
    // Determine if the number is even or odd
    if (num % 2 == 0)
    {
        cout << "Is the number " << num << " even? (y/n) ";
        cin >> input;

        if (input == 'y')
        {
            cout << "Correct!" << endl;
        }
        else
        {
            cout << "Incorrect!" << endl;
            break;
        }
    }
    else
    {
        cout << "Is the number " << num << " odd? (y/n) ";
        cin >> input;

        if (input == 'n')
        {
            cout << "Correct!" << endl;
        }
        else
        {
            cout << "Incorrect!" << endl;
            break;
        }
    }

    // Generate a new random number
    num = rand() % 100 + 1;
}

cout << "You lost the game." << endl;

return 0;
}
