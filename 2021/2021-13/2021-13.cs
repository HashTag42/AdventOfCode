using System;
using System.IO;    // File class
using System.Collections.Generic;   // List class

// Advent of Code
// --- Day 13: Transparent Origami ---
// https://adventofcode.com/2021/day/13

namespace _2021_13
{
    class Program
    {
        static void Main(string[] args)
        {
            // Console.WriteLine(SolvePuzzle(@".\inputTest.txt")); // Expected: ?
            Console.WriteLine(SolvePuzzle(@".\input.txt"));     // Expected: 818
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
            Instructions instructions= new Instructions(Input);

            Transparency transparency= new Transparency(instructions);

            Console.WriteLine(transparency);

            foreach(FoldInstruction foldInstruction in instructions.FoldInstructions)
            {
                transparency.Fold(foldInstruction);
                Console.WriteLine(transparency);
            }

            return transparency.VisiblePoints.ToString();
        }

        static string SolvePart2(string[] Input)
        {
            string result= "Answer 2";


            return result;
        }
    }
}
