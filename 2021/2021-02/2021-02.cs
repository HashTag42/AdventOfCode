using System;
using System.IO;

// Puzzle: https://adventofcode.com/2021/day/2

namespace _2021_02
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(processFile(@".\inputTest.txt"));
            Console.WriteLine(processFile(@".\input.txt"));
        }

        private static string processFile(string FilePath)
        {
            Coordinates result = processLines(FilePath);

            string  message  = "Processing "    + FilePath + " // ";
                    message += "Position: "     + result.Position + " // ";
                    message += "Depth = "       + result.Depth   + " // ";
                    message += "Product = "     + result.Multiplied ;

            return message;
        }

        private static Coordinates processLines(string FilePath)
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
    }
}
