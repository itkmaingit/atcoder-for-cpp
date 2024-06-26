#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
}

// ----------------------------------------------------------------
// sample input code

// N
void __input_N()
{
  int N;
  cin >> N;
}

// A B
void __input_AB()
{
  int A, B;
  cin >> A >> B;
}

// N
// a1 a2 a3 ... aN
void __input_N_aN()
{
  int N;
  cin >> N;
  vector<int> a(N);
  for (int i = 0; i < N; ++i)
  {
    cin >> a[i];
  }
}

// N
// a1
// a2
// ...
// aN
void __input_N_aN_vert()
{
  int N;
  cin >> N;
  vector<int> a(N);
  for (int i = 0; i < N; ++i)
  {
    cin >> a[i];
  }
}

// N M
// a11 a12 ... a1M
// a21 a22 ... a2M
// ...
// aN1 aN2 ... aNM
void __input_NM_matrix()
{
  int N, M;
  cin >> N >> M;
  vector<vector<int>> a(N, vector<int>(M));
  for (int i = 0; i < N; ++i)
  {
    for (int j = 0; j < M; ++j)
    {
      cin >> a[i][j];
    }
  }
}

// s
void __input_char_input()
{
  string s;
  cin >> s;
}

// N
// s1
// s2
// ...
// sN
void __input_multiple_char()
{
  int N;
  cin >> N;
  vector<string> s(N);
  for (int i = 0; i < N; ++i)
  {
    cin >> s[i];
  }
}