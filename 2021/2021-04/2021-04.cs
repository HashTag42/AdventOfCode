using System;
using System.IO;
using System.Collections.Generic;

namespace _2021_04
{
    class Program
    {
        static void Main(string[] args)
        {
            List<string> input = new List<string>();

            string inputFile = null;
            inputFile = @"inputTest.txt";
            // inputFile = @"input.txt";

            foreach(string line in File.ReadAllLines(inputFile)) {
                input.Add(line);
            }

            Console.WriteLine(solvePart1(input));
        }
        private static int solvePart1(List<string> input) {
            int answer = input.Count;
            BingoBoard board = new BingoBoard();
            return answer;
        }
    }
}
