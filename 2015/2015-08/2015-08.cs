// See https://aka.ms/new-console-template for more information

/// --- Day 8: Matchsticks ---
/// https://adventofcode.com/2015/day/8

string inputFile = "";
// inputFile = @".\inputTest.txt";
inputFile = @".\input.txt";

int totalCharactersOfCode   = default;
int totalCharactersInMemory = default;
int totalEncodedCharacters  = default;

foreach(string line in File.ReadAllLines(inputFile))
{
    StringLiteral str = new StringLiteral(line);
    totalCharactersOfCode   += str.CharactersOfCode;
    totalCharactersInMemory += str.CharactersInMemory;
    totalEncodedCharacters  += str.EncodedCharacters;
}

int answerPart1 = totalCharactersOfCode - totalCharactersInMemory;
Console.WriteLine(answerPart1); // Expect: 1350

int answerPart2 = totalCharactersOfCode + totalEncodedCharacters - totalCharactersOfCode;
Console.WriteLine(answerPart2); // Expect: 2085
