using System;
using System.IO;
using System.Diagnostics;

namespace _2021_05 {
    class Program {
        static void Main(string[] args) {
            Console.WriteLine(solvePart1(@".\testInput.txt")); // Expected: 5
            Console.WriteLine(solvePart2(@".\testInput.txt")); // Expected: 12
            // Console.WriteLine(solvePart1(@".\testInput2.txt")); // Expected:
            // Console.WriteLine(solvePart2(@".\testInput2.txt")); // Expected:
            Console.WriteLine(solvePart1(@".\input.txt")); // Expected: 6548
            Console.WriteLine(solvePart2(@".\input.txt")); // Expected: ????. 19633 is too low.
        }

        static int solvePart1(string FilePath) {
            Board board = new Board();
            foreach(string line in File.ReadLines(FilePath)) {
                int[] c = getCoordinates(line);
                board.AddLine(c[0], c[1], c[2],c[3], false);
            }
            // Debug.WriteLine(board);
            return board.CountPoints(2);
        }

        static int solvePart2(string FilePath) {
            Board board = new Board();
            foreach(string line in File.ReadLines(FilePath)) {
                int[] c = getCoordinates(line);
                board.AddLine(c[0], c[1], c[2], c[3], true);
            }
            // Debug.WriteLine(board);
            return board.CountPoints(2);
        }

        static int[] getCoordinates(string line) {
            int[] result = new int[4];

            int startIndex = 0, length = line.IndexOf(',');
            result[0]  = int.Parse(line.Substring(startIndex, length));
            startIndex = length + 1; length = line.IndexOf(' ') - startIndex;
            result[1]  = int.Parse(line.Substring(startIndex, length));
            startIndex = line.IndexOf("> ") + 2; length = line.IndexOf(',', startIndex) - startIndex;
            result[2]  = int.Parse(line.Substring(startIndex, length));
            startIndex = line.IndexOf(',', startIndex) + 1;
            result[3]  = int.Parse(line.Substring(startIndex));

            return result;
        }
    }
}
