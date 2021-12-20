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
            Polymer polymer;
            polymer = new Polymer(@".\inputTest.txt", 10); // Expect 1588
            polymer = new Polymer(@".\inputTest.txt", 40); // Expect 2188189693529
            polymer = new Polymer(@".\input.txt", 10);  // Expect 2010
            polymer = new Polymer(@".\input.txt", 40);  // Expect 2437698971143
        }
    }
}