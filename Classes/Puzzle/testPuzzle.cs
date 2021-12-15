using System;

namespace _Puzzle
{
    class Program
    {
        static void Main(string[] args)
        {
            Puzzle myPuzzle = new Puzzle("Day 7: The Treachery of Whales", "https://adventofcode.com/2021/day/7");
            Console.WriteLine(myPuzzle);

            PuzzlePart part1 = new PuzzlePart(
                "Part 1",
                "How much fuel must they spend to align to that position?"
            );
            myPuzzle.AddPuzzlePart(part1);



            myPuzzle.AddPuzzlePart(new PuzzlePart(
                "Part 2",
                "How much fuel must they spend to align to that position?"
            ));

            foreach(PuzzlePart puzzlePart in myPuzzle.Parts) { Console.WriteLine(puzzlePart); }
        }
    }
}
