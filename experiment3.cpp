#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<string> possible_combinations = {
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
};

vector<string> &getAllAlphabetCombinations(int length) {
  cout << "making list of length " << length << endl;
  vector<string> *result = new vector<string>();
  while (length > 0) {
    if (result->size() == 0) {
      for (int i = 0; i < 26; i++) {
        result->push_back(possible_combinations[i]);
      }
    } else {
      vector<string> *newResult = new vector<string>();
      for (int i = 0; i < result->size(); i++) {
        for (int alphabetIdx = 0; alphabetIdx < 26; alphabetIdx++) {
          newResult->push_back(result->at(i) + possible_combinations[alphabetIdx]);
        }
      }
      result = newResult;
    }
    length--;
  }
  return *result;
}

bool hasAllAlphabetCombinations(string &inputVal) {
  for (int i = 0; i < 26; i++) {
    for (int j = 0; j < 26; j++) {
      string s = possible_combinations[i] + possible_combinations[j];
      if (inputVal.find(s) == string::npos) {
        return false;
      }
    }
  }
  return true;
}

int main() {
  int search_string_lower_bound = 2 * 26;       // 26 letters, 2 times each
  int search_string_upper_bound = 2 * 26 * 26;  // 26 letters, 2 times each, 26 combinations

  for (int i = search_string_lower_bound; i < search_string_upper_bound; i++) {
    vector<string> candidates = getAllAlphabetCombinations(i);
    for (int j = 0; j < candidates.size(); j++) {
      cout << candidates[j] << endl;
      if (hasAllAlphabetCombinations(candidates[j])) {
        cout << "Found it: " << candidates[j] << endl;
        return 0;
      }
    }
  }
  return 0;
}
