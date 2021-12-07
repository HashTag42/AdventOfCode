using System;
using System.IO;
using System.Collections.Generic;
using System.Diagnostics;

namespace _2015_05
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(solvePart1(@".\testInput.txt"));  // Expected: 2
            Console.WriteLine(solvePart1(@".\input.txt"));      // Expected: 238
            Console.WriteLine(solvePart2(@".\testInput2.txt")); // Expected: 2
            Console.WriteLine(solvePart2(@".\input.txt"));      // Expected: 69
        }

        static int solvePart1(string FilePath) {
            int NiceWords = 0;
            foreach(string line in File.ReadLines(FilePath)) {
                if(IsNice1(line)) {
                    Debug.WriteLine("is nice!", line);
                    NiceWords++;
                }
            }
            return NiceWords;
        }

        static int solvePart2(string FilePath) {
            int NiceWords = 0;
            foreach(string line in File.ReadLines(FilePath)) {
                if(IsNice2(line.ToLower())) {
                    Debug.WriteLine(line);
                    NiceWords++;
                }
            }
            return NiceWords;
        }

        static bool IsNice1(string Str) {
            bool containsNVowels = ContainsNVowels(Str, 3);
            bool containsRepeatedLetter = ContainsRepeatedLetter(Str, 2);
            bool doesNotContainLetters = DoesNotContainStrings(Str);
            return (containsNVowels && containsRepeatedLetter && doesNotContainLetters);
        }

        static bool IsNice2(string Str) {
            bool containsRepeatedPair = ContainsRepeatedPair(Str);
            bool contains1letter = Contains1letter(Str);
            Debug.WriteLine("String [{0}] containsRepeatedPair = {1}, contains1letter = {2}", Str, containsRepeatedPair, contains1letter);
            return (containsRepeatedPair && contains1letter);
        }

        static bool ContainsRepeatedPair(string line) {
            bool containsRepeatedPair = false;
            List<string> pairs = new List<string>();
            for(int i = 1; i < line.Length; i++) {
                pairs.Add(new string(line.Substring(i-1,2)));
            }
            for(int x = 0; x < (pairs.Count-2); x++) {
                if(containsRepeatedPair) {
                    break;
                } else {
                    string pairA = pairs[x];
                    for(int y = x+2; y < pairs.Count; y++) {
                        string pairB = pairs[y];
                        if(pairA == pairB) {
                            containsRepeatedPair = true;
                            break;
                        }
                    }
                }
            }
            return containsRepeatedPair;
        }

        static bool Contains1letter(string line) {
            bool contains1letter = false;
            for(int i = 2; i < line.Length; i++) {
                if(line[i-2] == line[i]) {
                    contains1letter = true;
                    break;
                }
            }
            return contains1letter;
        }

        static bool ContainsNVowels(string Str, int MinVowels) {
            bool containsNVowels = false;
            int vowelCount = 0;
            char[] vowels = {'a', 'e', 'i', 'o', 'u' };
            foreach(char c in Str) {
                if((c.ToString().IndexOfAny(vowels) > -1)) {
                    vowelCount++;
                }
                if( vowelCount >= MinVowels ) {
                    containsNVowels = true;
                    break;
                }
            }
            return containsNVowels;
        }

        static bool ContainsRepeatedLetter(string str, int repeat) {
            bool containsRepeatedLetter = false;
            char lastChar = ' ';
            foreach(char c in str) {
                if(c == lastChar) {
                    containsRepeatedLetter = true;
                    break;
                }
                lastChar = c;
            }
            return containsRepeatedLetter;
        }

        static bool DoesNotContainStrings(string str) {
            bool doesNotContainLetters = true;
            List<string> naughtyStrings = new List<string> { "ab", "cd", "pq", "xy" };
            foreach(string s in naughtyStrings) {
                int indexOf = str.IndexOf(s);
                if(indexOf != -1) {
                    doesNotContainLetters = false;
                    break;
                }
            }
            return doesNotContainLetters;
        }
    }
}
