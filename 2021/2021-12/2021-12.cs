﻿//  Day 12: Passage Pathing
//  https://adventofcode.com/2021/day/12

/// Define which input file to use
string inputFile = "";
inputFile = "inputTest1.txt";
// inputFile = "inputTest2.txt";
// inputFile = "inputTest3.txt";
// inputFile = "input.txt";
Console.WriteLine($"Using: {inputFile}");

CaveMap caveMap = new CaveMap(inputFile);
Console.WriteLine(caveMap);
Console.WriteLine(caveMap.PathCount);