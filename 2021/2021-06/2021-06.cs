using System;
using System.IO;
using System.Collections.Generic;
using System.Diagnostics;

namespace _2021_06
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(SolvePuzzle(@".\testInput.txt", 80)); // Expect: 5934
            Console.WriteLine(SolvePuzzle(@".\Input.txt", 80)); // Expect: 379414
            Console.WriteLine(SolvePuzzle(@".\testInput.txt", 256)); // Expect: 26984457539
            Console.WriteLine(SolvePuzzle(@".\Input.txt", 256)); // Expect: 1705008653296
        }

        static ulong SolvePuzzle(string FilePath, int Days) {
            string line = File.ReadAllText(FilePath);
            string[] input = line.Split(',');
            ulong[] numbers = new ulong[10];
            foreach(string u in input) {
                numbers[int.Parse(u)]++;
            }
            for(int d = 0; d < Days; d++) {
                numbers = MoveNumbers(numbers);
            }
            return CountNumbers(numbers);
        }

        static ulong[] MoveNumbers(ulong[] Numbers) {
            ulong[] newNumbers = new ulong[9];
            newNumbers[6] = Numbers[0];
            newNumbers[8] = Numbers[0];
            for(int i = 0; i <= 7; i++) {
                newNumbers[i] += Numbers[i+1];
            }
            return newNumbers;
        }

        static ulong CountNumbers(ulong[] Numbers) {
            ulong count = 0;
            for(int i = 0; i < 9; i++) {
                count += Numbers[i];
            }
            return count;
        }
    }
}
