using System;
using System.IO;
using System.Collections.Generic;
using System.Diagnostics;

// Puzzle: https://adventofcode.com/2021/day/8

namespace _2021_08
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(solvePuzzle(@".\input.txt")); // Answer: 521.
        }

        static int solvePuzzle(string FilePath) {
            int countEasyDigits = 0;
            List<int> filter = new List<int> { 2, 4, 3, 7 };
            List<string> lines = new List<string>(File.ReadAllLines(FilePath));
            foreach(string line in lines) {
                string[] segments = line.Split('|');
                string[] digits = segments[1].Split(' ', StringSplitOptions.RemoveEmptyEntries);
                for(int j = 0; j < digits.Length; j++) {
                    if(filter.IndexOf(digits[j].Length) != -1) {
                        countEasyDigits++;
                    }
                }
            }
            return countEasyDigits;
        }
    }
}
