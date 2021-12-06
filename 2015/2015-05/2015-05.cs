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
            Console.WriteLine(solvePuzzle(@".\testInput.txt"));
            Console.WriteLine(solvePuzzle(@".\input.txt"));
        }

        static int solvePuzzle(string FilePath) {
            int NiceWords = 0;
            foreach(string line in File.ReadLines(FilePath)) {
                if(IsNice(line)) {
                    Debug.WriteLine(line);
                    NiceWords++;
                }
            }
            return NiceWords;
        }

        static bool IsNice(string Str) {
            bool containsNVowels = ContainsNVowels(Str, 3);
            bool containsRepeatedLetter = ContainsRepeatedLetter(Str, 2);
            bool doesNotContainLetters = DoesNotContainStrings(Str);
            return (containsNVowels && containsRepeatedLetter && doesNotContainLetters);
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
                if(str.IndexOf(s) != -1) {
                    doesNotContainLetters = false;
                    break;
                }
            }
            return doesNotContainLetters;
        }

        class LetterCount {
            public char Letter { get; set; }
            public int Count { get; set; }
            public LetterCount(char inC, int inCount) {
                Letter = inC;
                Count = inCount;
            }
        }
    }
}
