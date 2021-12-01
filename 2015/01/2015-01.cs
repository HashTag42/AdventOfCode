using System;
using System.IO;

// Puzzle: https://adventofcode.com/2015/day/1

namespace _01
{
    class Program
    {
        static void Main(string[] args)
        {
            string text = File.ReadAllText(@".\input.txt");
            int floor = 0;
            for(int i = 0; i < text.Length; i++)
            {
                char c = text[i];
                if ('(' == c)
                {
                    floor ++;
                }
                else if (')' == c)
                {
                    floor--;
                }
            }
            Console.WriteLine(floor);
        }
    }
}
