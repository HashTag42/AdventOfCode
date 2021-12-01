using System;
using System.IO;

// Puzzle: https://adventofcode.com/2021/day/1



namespace _2021_01
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(processFile(@".\inputTest.txt"));
            Console.WriteLine(processFile(@".\input.txt"));
        }

        private static string processFile(string FilePath)
        {
            uint result = processLines(FilePath);
            string theString = "Processing " + FilePath + " // ";
            theString += "Increased count: " + result;

            return theString;
        }

        private static uint processLines(string FilePath)
        {
            uint increasedCount = 0;
            uint previous = 0;
            uint current = 0;
            uint lineCount = 1;

            foreach(string line in File.ReadLines(FilePath))
            {
                previous = current;
                current  = uint.Parse(line);
                if (lineCount > 1)
                {
                    if (current > previous)
                    {
                        increasedCount++;
                    }
                }
                lineCount++;
            }

            return increasedCount;
        }

    }
}
