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

            // Answer 1: 818 --- Answer 2: LRGPRECB
            Console.WriteLine(SolvePuzzle(@".\input.txt"));
        }

        static string SolvePuzzle(string FilePath)
        {
            string[] input= File.ReadAllLines(FilePath);

            string message= null;
            message+= "Using file: " + FilePath + "\n";
            message+= "\t Part 1 answer: " + SolvePuzzle(input) + "\n";

            return message;
        }

        static string SolvePuzzle(string[] Input)
        {
            Instructions instructions= new Instructions(Input);

            Transparency transparency= new Transparency(instructions);

            // Console.WriteLine(transparency);

            foreach(FoldInstruction foldInstruction in instructions.FoldInstructions)
            {
                transparency.Fold(foldInstruction);
                // Console.WriteLine(transparency);
            }

            Console.WriteLine(transparency);

            return transparency.VisiblePoints.ToString();
        }
    }
}
