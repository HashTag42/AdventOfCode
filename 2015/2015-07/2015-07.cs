using System.Diagnostics;

#nullable disable

/// --- Day 7: Some Assembly Required ---
/// https://adventofcode.com/2015/day/7

// string input = @".\inputTest.txt";
string input = @".\input.txt";

Instructions instructions = new Instructions(input);

while(instructions.HasUnprocessedCommands())
{
    instructions.ProcessCommands();
}

foreach(string wire in instructions.Wires.Keys)
{
    Debug.WriteLine($"{wire}: {instructions.Wires[wire]}");
}

Console.WriteLine(instructions.Wires["a"]);
