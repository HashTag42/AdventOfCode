using System;
using System.IO;
using System.Collections.Generic;

namespace _2021_06
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(solvePart1(@".\testInput.txt")); // Expect: 5934
            Console.WriteLine(solvePart1(@".\Input.txt")); // Expect: 379414
        }

        static int solvePart1(string FilePath) {
            // Read input list of lanternfish
            List<Lanternfish> group = new List<Lanternfish>();
            string line = File.ReadAllText(FilePath);
            string[] units = line.Split(',');
            foreach(string u in units) {
                group.Add(new Lanternfish(int.Parse(u)));
            }
            for(int day = 0; day < 80; day++) {
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
