using System;
using System.IO;
using System.Collections.Generic;
using System.Diagnostics;

// --- Day 6: Lanternfish ---
// https://adventofcode.com/2021/day/6

/*  A key aspect of an efficient solution is that we only need to calculate the outcome for a single
    instance of lanternfish per days left.
*/

namespace _2021_06
{
    class Program
    {
         // The number of days left for each lanternfish goes from 0 to 8.
        const int PossibleDigits = 9;

        // A new lanterfish starts with 8 days left.
        const int NewLanterfishDaysLeft = 8;

        // An old lanternfish resets to 6 days left after creating a new one.
        const int OldLanternFishDaysLeftAfterReset = 6;

        static void Main(string[] args)
        {
            Console.WriteLine(invokeSolvePuzzle(@".\testInput.txt", 80)); // Expect: 5934
            Console.WriteLine(invokeSolvePuzzle(@".\Input.txt", 80)); // Expect: 379414
            Console.WriteLine(invokeSolvePuzzle(@".\testInput.txt", 256)); // Expect: 26984457539
            Console.WriteLine(invokeSolvePuzzle(@".\Input.txt", 256)); // Expect: 1705008653296
        }

        static string invokeSolvePuzzle(string FilePath, int Days)
        {
            string message = null;
            message += "Using " + FilePath + " & " + Days + " days.";

            // Measure elapsed time using the .NET Diagnostics.Stopwatch class
            // https://docs.microsoft.com/en-us/dotnet/api/system.diagnostics.stopwatch
            Stopwatch stopwatch = new Stopwatch();
            stopwatch.Start();
            message += " // Answer: " + SolvePuzzle(FilePath, Days);
            stopwatch.Stop();
            message += " // Elapsed time: " + stopwatch.Elapsed;

            return message;
        }

        static ulong SolvePuzzle(string FilePath, int Days)
        {
            string line = File.ReadAllText(FilePath);
            string[] input = line.Split(',');

            // Group all lanternfishes with the same number of days left.
            ulong[] groups = new ulong[PossibleDigits];
            foreach(string u in input)
            {
                groups[int.Parse(u)]++;
            }

            // Step for every day
            for(int d = 0; d < Days; d++)
            {
                groups = StepADay(groups);
            }

            return CountTotalLanternfishes(groups);
        }

        static ulong[] StepADay(ulong[] Groups)
        {
            ulong[] newGroups = new ulong[PossibleDigits];

            // Old lanternfishes that just created a new one are reset to 6 days left.
            newGroups[OldLanternFishDaysLeftAfterReset] = Groups[0];

            // New lanternfishes are created with 8 days left.
            newGroups[NewLanterfishDaysLeft] = Groups[0];

            // Add the new lanterfishes to their respective groups.
            for(int i = 0; i < NewLanterfishDaysLeft; i++)
            {
                newGroups[i] += Groups[i+1];
            }

            return newGroups;
        }

        static ulong CountTotalLanternfishes(ulong[] Groups)
        {
            ulong count = 0;

            for(int i = 0; i < PossibleDigits; i++)
            {
                count += Groups[i];
            }

            return count;
        }
    }
}
