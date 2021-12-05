using System;
using System.IO;
using System.Diagnostics;

namespace _2021_05 {
    class Program {
        static void Main(string[] args) {
            Console.WriteLine(solvePuzzleFromFile(@".\inputTest.txt")); // Expected: 5
            Console.WriteLine(solvePuzzleFromFile(@".\input.txt")); // Expected: 6548
        }

        static int solvePuzzleFromFile(string FilePath) {
            Board board = new Board();
            foreach(string line in File.ReadLines(FilePath)) {
                board.AddLine(line);
            }
            return board.CountPoints(2);
        }
    }
}
