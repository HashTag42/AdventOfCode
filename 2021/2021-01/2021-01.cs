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
            uint[] results = processLines(FilePath);

            uint increasedCount = results[0];
            uint increasedSumCount = results[1];

            string message = "Processing " + FilePath + " // ";
            message += "Increased count: " + increasedCount + " // ";
            message += "Rolling sum increased count: " + increasedSumCount;

            return message;
        }

        private static uint[] processLines(string FilePath)
        {
            uint previous2          = 0;
            uint previous1          = 0;
            uint current            = 0;
            uint increasedCount     = 0;

            uint currentRollingSum  = 0;
            uint priorRollingSum    = 0;
            uint increasedSumCount  = 0;

            uint lineCount          = 1;

            foreach(string line in File.ReadLines(FilePath))
            {
                previous2   = previous1;
                previous1   = current;
                current     = uint.Parse(line);

                priorRollingSum     = currentRollingSum;
                currentRollingSum   = previous2 + previous1 + current;

                if ((lineCount > 1) && (current > previous1))
                {
                    increasedCount++;
                }

                if ((lineCount > 3) && (currentRollingSum > priorRollingSum))
                {
                    increasedSumCount++;
                }

                lineCount++;
            }

            uint[] result = new uint[] { increasedCount, increasedSumCount };
            return result;
        }
    }
}
