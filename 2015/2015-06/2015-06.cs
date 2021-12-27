using System;
using System.Diagnostics;
using System.IO;

/// --- Day 6: Probably a Fire Hazard ---
/// https://adventofcode.com/2015/day/6

namespace _2015_06
{
    class Program
    {
        static void Main(string[] args)
        {
            // string input = @".\inputTest.txt";
            string input = @".\input.txt";
            Instructions instructions = new Instructions(input);

            Grid grid1 = new Grid(1, instructions);
            Console.WriteLine(grid1.Sum());

            Grid grid2 = new Grid(2, instructions);
            Console.WriteLine(grid2.Sum());
        }
    }
}
