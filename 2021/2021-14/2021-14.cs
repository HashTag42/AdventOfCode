using System;
using System.IO;
using System.Collections.Generic;
using System.Diagnostics;

// Advent of Code
// --- Day 14: Extended Polymerization ---
// https://adventofcode.com/2021/day/14

namespace _2021_14
{
    class Program
    {
        static void Main(string[] args)
        {
            SolvePuzzle("inputTest.txt", 10);  // Expect 1588
            SolvePuzzle("inputTest.txt", 40);  // Expect 2188189693529
            SolvePuzzle("input.txt",     10);  // Expect 2010
            SolvePuzzle("input.txt",     40);  // Expect 2437698971143
        }

        private static void SolvePuzzle(string FilePath, int Steps)
        {
            Stopwatch myStopwatch = new Stopwatch();

            myStopwatch.Start();

            Polymer myPolymer = new Polymer(FilePath);
            myPolymer.TakeSteps(Steps);
            ulong answer = myPolymer.GetAnswer();

            myStopwatch.Stop();

            Console.WriteLine("Using: {0} and {1} steps. Answer = {2}. // Elapsed time = {3}",
                                FilePath, Steps, answer, myStopwatch.Elapsed);
        }
    }
}