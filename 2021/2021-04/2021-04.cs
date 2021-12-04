using System;
using System.IO;
using System.Collections.Generic;
using System.Diagnostics;

namespace _2021_04 {
    class Program {
        static void Main(string[] args) {

            // The expected results are 4512 and <PART2>
            Console.WriteLine(SolvePuzzleUsingFile(@".\inputTest.txt"));

            // The expected results are 31424 and <PART2>
            Console.WriteLine(SolvePuzzleUsingFile(@".\input.txt"));
        }

        private static string SolvePuzzleUsingFile(string FilePath) {
            List<string> input = new List<string>();
            foreach(string line in File.ReadAllLines(FilePath)) { input.Add(line); }
            string result = null;
            result  = "Solving puzzle using file: " + FilePath;
            result += "\n\t Answer to Part 1: " + solvePart1(input);
            result += "\n\t Answer to Part 2: " + solvePart2(input);
            return result;
        }

        private static int solvePart1(List<string> input) {
            List<BingoBoard> boards = new List<BingoBoard>();
            for(int i=2 ; i<input.Count; i+=6) {
                int firstLineIndex = i;
                int lineCount = 5;
                List<string> boardInput = input.GetRange(firstLineIndex, lineCount);
                BingoBoard newBoard = new BingoBoard(boardInput);
                boards.Add(newBoard);
                // Console.WriteLine(newBoard);
            }

            // Draw numbers to determine the winning board
            int winningNumber = -1;
            int sumUnmarkedCells = -1;
            string numbersLine = input[0];
            string[] numbers = numbersLine.Split(',');
            foreach(string number in numbers) {
                int num = int.Parse(number);
                foreach(BingoBoard board in boards) {
                    board.MarkCell(num);
                    if(board.IsBingo) {
                        winningNumber = num;
                        sumUnmarkedCells = board.SumUnmarkedCells();
                        Debug.WriteLine("Winning number: {0}", winningNumber);
                        Debug.WriteLine("Winning board number {0}", boards.IndexOf(board));
                        Debug.WriteLine(board);
                        goto Bingo;
                    }
                }
            }

        Bingo:
            int score = sumUnmarkedCells * winningNumber;
            return score;
        }

        private static int solvePart2(List<string> input) {
            int answer = input.Count;
            return answer;
        }

    }
}
