using System;
using System.IO;

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
            Coordinates result = processFilePart1(FilePath);

            string  message  = "Processing " + FilePath + " // ";
                    message += "Part 1 // ";
                    message += "Position: " + result.Position + " // ";
                    message += "Depth = " + result.Depth   + " // ";
                    message += "Answer = " + result.Multiplied ;

            return message;
        }

        private static string getPart2(string FilePath)
        {
            Coordinates result = processFilePart2(FilePath);

            string  message  = "Processing " + FilePath + " // ";
                    message += "Part 2 // ";
                    message += "Position: " + result.Position + " // ";
                    message += "Depth = " + result.Depth + " // ";
                    message += "Answer = " + result.Multiplied;

            return message;
        }

        private static Coordinates processFilePart1(string FilePath)
        {
            uint position   = 0;
            uint depth      = 0;
            foreach(string line in File.ReadLines(FilePath))
            {
                string[] terms  = line.Split(' ');
                string command  = terms[0];
                uint value      = uint.Parse(terms[1]);

                switch(command)
                {
                    case "forward":
                        position += value;
                        break;

                    case "down":
                        depth += value;
                        break;

                    case "up":
                        depth -= value;
                        break;

                    default:
                        break;
                }
            }

            Coordinates coordinates = new Coordinates( position, depth);

            return coordinates;
        }

        private static Coordinates processFilePart2(string FilePath)
        {
            uint position   = 0;
            uint depth      = 0;
            uint aim        = 0;
            foreach(string line in File.ReadLines(FilePath))
            {
                string[] terms  = line.Split(' ');
                string command  = terms[0];
                uint value      = uint.Parse(terms[1]);

                switch(command)
                {
                    case "forward":
                        position += value;
                        depth += aim * value;
                        break;

                    case "down":
                        aim += value;
                        break;

                    case "up":
                        aim -= value;
                        break;

                    default:
                        break;
                }
            }

            Coordinates coordinates = new Coordinates(position, depth);

            return coordinates;
        }
    }
}
