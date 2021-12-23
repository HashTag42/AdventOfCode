using System;

//  Day 12: Passage Pathing
//  https://adventofcode.com/2021/day/12

namespace _2021_12
{
    class Program
    {
        static void Main(string[] args)
        {
            CaveMap map = new CaveMap("inputTest1.txt");
            // CaveMap map = new CaveMap("inputTest2.txt");
            // CaveMap map = new CaveMap("inputTest3.txt");
            // CaveMap map = new CaveMap("input.txt");
            Console.WriteLine(map);
        }
    }
}
