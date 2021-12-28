// See https://aka.ms/new-console-template for more information

/// --- Day 8: Matchsticks ---
/// https://adventofcode.com/2015/day/8

string inputFile = "";
// inputFile = @".\inputTest.txt";
inputFile = @".\input.txt";

int totalCharactersOfCode   = default;
int totalCharactersInMemory = default;

foreach(string line in File.ReadAllLines(inputFile))
{
    StringLiteral str = new StringLiteral(line);
    totalCharactersOfCode   += str.CharactersOfCode;
    totalCharactersInMemory += str.CharactersInMemory;
}

int answer = totalCharactersOfCode - totalCharactersInMemory;
Console.WriteLine(answer);
// 1365 is too high
// 1608 is too high
