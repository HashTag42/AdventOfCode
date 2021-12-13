using System;
using System.IO;

// Advent of Code
// --- Day DD: Puzzle Title ---
// https://adventofcode.com/YYYY/day/MM

namespace _YYYY_DD
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(SolvePuzzle(@".\inputTest.txt")); // Expected: ?
            Console.WriteLine(SolvePuzzle(@".\input.txt"));     // Expected: ?
        }

        static string SolvePuzzle(string FilePath)
        {
            string[] input= File.ReadAllLines(FilePath);

            string message= null;
            message+= "Using file: " + FilePath + "\n";
            message+= "\t Part 1 answer: " + SolvePart1(input) + "\n";
            message+= "\t Part 2 answer: " + SolvePart2(input) + "\n";

            return message;
        }

        static string SolvePart1(string[] Input)
        {
            string result= "Answer 1";
            return result;
        }

        static string SolvePart2(string[] Input)
        {
            string result= "Answer 2";
            return result;
        }
    }
}
