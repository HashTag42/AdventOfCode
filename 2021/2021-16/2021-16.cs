﻿// See https://aka.ms/new-console-template for more information

// --- Day 16: Packet Decoder ---
// https://adventofcode.com/2021/day/16

using MyNamespace;

Console.WriteLine("Hello, 2021-16!");

int hex = 0x2F;
int binary = 0b_0010_1111;

Console.WriteLine(hex);
Console.WriteLine(binary);

Console.WriteLine(Utilities.ConvertFromBinary("100"));

List<string> input = new List<string>(File.ReadLines("input.txt"));

foreach(string line in input)
{
    Console.WriteLine(line);
}

Packet myPacket = new Packet();
