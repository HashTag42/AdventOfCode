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
            Polymer polymer = new Polymer(@".\inputTest.txt", 4);
            // Polymer polymer = new Polymer(@".\input.txt", 10);

            Console.WriteLine("Answer to part 1: " + polymer.MostCommonMinusLeastCommon());
        }
    }
}