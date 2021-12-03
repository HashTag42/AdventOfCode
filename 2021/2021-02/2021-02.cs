using System;
using System.IO;
using System.Diagnostics;

// Puzzle: https://adventofcode.com/2021/day/2

namespace _2021_02
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(getPart1(@".\inputTest.txt"));
            Console.WriteLine(getPart2(@".\inputTest.txt"));

            Console.WriteLine(getPart1(@".\input.txt"));
            Console.WriteLine(getPart2(@".\input.txt"));
        }

        private static string getPart1(string FilePath)
        {
            uint answer = solvePart1(FilePath);
            string  message  = "Processing " + FilePath + " // ";
                    message += "Part 1 // ";
                    message += "Answer = " + answer;

            return message;
        }

        private static string getPart2(string FilePath)
        {
            uint answer = solvePart2(FilePath);
            string  message  = "Processing " + FilePath + " // ";
                    message += "Part 2 // ";
                    message += "Answer = " + answer;
            return message;
        }

        private static uint solvePart1(string inputPath) {
            uint position   = 0;
            uint depth      = 0;
            foreach(string line in File.ReadLines(inputPath)) {
                string[] terms  = line.Split(' ');
                string command  = terms[0];
                uint value      = uint.Parse(terms[1]);
                switch(command) {
                    case "forward": position += value; break;
                    case "down": depth += value; break;
                    case "up": depth -= value; break;
                }
            }
            return (position * depth);
        }

        private static uint solvePart2(string FilePath) {
            uint position = 0;
            uint depth    = 0;
            uint aim      = 0;
            foreach(string line in File.ReadLines(FilePath)) {
                string[] terms  = line.Split(' ');
                string command  = terms[0];
                uint value      = uint.Parse(terms[1]);
                switch(command) {
                    case "forward": position += value; depth += aim * value; break;
                    case "down": aim += value; break;
                    case "up": aim -= value; break;
                }
            }
            return (position * depth);
        }
    }
}
