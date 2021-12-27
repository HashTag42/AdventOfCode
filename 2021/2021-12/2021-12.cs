using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;

//  Day 12: Passage Pathing
//  https://adventofcode.com/2021/day/12

namespace _2021_12
{
    class Program
    {
        static void Main(string[] args)
        {
            /// Define which input file to use
            string inputFile = default;
            inputFile = "inputTest1.txt";
            // inputFile = "inputTest2.txt";
            // inputFile = "inputTest3.txt";
            // inputFile = "input.txt";
            Console.WriteLine($"Using: {inputFile}");

            /// Load the map from the input file.
            DefaultDict<string, string> map = new DefaultDict<string, string>();
            foreach(string line in File.ReadAllLines(inputFile))
            {
                string[] caves = line.Split("-");
                map.Add(caves[0],caves[1]);
                map.Add(caves[1],caves[0]);
            }
            Debug.WriteLine(map);

            List<string> Visited = new List<string>();
            Stack<String> stack = new Stack<string>();
            stack.Push("start");
            while(stack.Count > 0)
            {
                string cave = stack.Pop();
                if(!Visited.Contains(cave))
                {
                    Console.Write($"{cave} ");
                    Visited.Add(cave);
                    List<string> neighbours = map.GetValues(cave);
                    foreach(string n in neighbours)
                    {
                        stack.Push(n);
                    }
                }
            }
        }
    }
}
