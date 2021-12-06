using System;
using System.IO;
using System.Collections.Generic;

namespace _2021_06
{
    class Program
    {
        static void Main(string[] args)
        {
            // Console.WriteLine(solvePuzzle(@".\testInput.txt", 80)); // Expect: 5934
            // Console.WriteLine(solvePuzzle(@".\Input.txt", 80)); // Expect: 379414
            Console.WriteLine(solvePuzzle(@".\testInput.txt", 256)); // Expect: 26984457539
            // Console.WriteLine(solvePuzzle(@".\Input.txt", 256)); // Expect: ?
        }

        static int solvePuzzle(string FilePath, int Days) {
            // Read input list of lanternfish
            List<Lanternfish> group = new List<Lanternfish>();
            string line = File.ReadAllText(FilePath);
            string[] units = line.Split(',');
            foreach(string u in units) {
                group.Add(new Lanternfish(int.Parse(u)));
            }
            for(int day = 0; day < Days; day++) {
                Console.WriteLine("Day {0}", day);
                int newFish = 0;
                foreach(Lanternfish f in group) {
                    if(f.NextDay()) {
                        newFish++;
                    }
                }
                for(int i = 0; i < newFish; i++) {
                    group.Add(new Lanternfish());
                }
            }
            return group.Count;
        }
    }
}
