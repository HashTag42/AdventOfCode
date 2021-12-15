using System;
using System.IO;    // File class.
using System.Collections.Generic;   // List class.
using System.Diagnostics;   // Debug class

namespace _2021_12
{
    class Program
    {
        static void Main(string[] args)
        {
            Puzzle puzzle= new Puzzle("Day 12: Passage Pathing", "https://adventofcode.com/2021/day/12" );
            Console.WriteLine(puzzle);

            puzzle.AddPuzzlePart(new PuzzlePart("Part 1", "How many paths through this cave system are there that visit small caves at most once?"));
            foreach(PuzzlePart part in puzzle.Parts)
            {
                Console.WriteLine(part);
            }

            Console.WriteLine(solvePuzzle(@".\inputTest1.txt"));
        }

        static string solvePuzzle(string FilePath)
        {
            string answer= null;
            string[] lines= File.ReadAllLines(FilePath);

            #if DEBUG
                Debug.WriteLine("Input lines:");
                foreach(string line in lines)
                {
                    Debug.WriteLine(line);
                }
                Debug.WriteLine("-------------");
            #endif

            List<Cave> caves = ParseCaves(lines);
            foreach(Cave cave in caves)
            {
                Console.WriteLine("Cave {0}: {1}", cave.Name, cave.Size);
            }

            return answer;
        }

        static List<Cave> ParseCaves(string[] Lines)
        {
            List<Cave> caves= new List<Cave>();
            foreach(string line in Lines)
            {
                string[] terms= line.Split('-');
                foreach(string term in terms)
                {
                    Cave cave= new Cave(term);
                    if(!caves.Contains(cave))
                    {
                        caves.Add(new Cave(term));
                    }
                }
            }
            return caves;
        }
    }
}
