using System.Diagnostics;

#nullable disable

/// --- Day 7: Some Assembly Required ---
/// https://adventofcode.com/2015/day/7

// string input = @".\inputTest.txt";
string input = @".\input.txt";

Instructions instructions = new Instructions(input);

instructions.ProcessCommands();

Console.WriteLine(instructions.Wires["a"]);

ushort tmp = instructions.Wires["a"].Value;

Instructions newInstructions = new Instructions(input);

newInstructions.OverrideWireName = "b";
newInstructions.OverrideValue = tmp;

newInstructions.ProcessCommands();

Console.WriteLine(newInstructions.Wires["a"]);
// 3176 is too low
