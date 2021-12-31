// See https://aka.ms/new-console-template for more information

// string inputFile = @".\inputTest.txt";
string inputFile = @".\input.txt";

Map map = new Map(inputFile);

Console.WriteLine(map);
Console.WriteLine($"Shortest distance: {map.ShortestDistance}");
// Expected: 251