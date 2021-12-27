using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;

class Instructions
{
    public List<Command> Commands { get; init; }

    public Instructions()
    {
        this.Commands = new List<Command>();
    }
    public Instructions(string FileName) : this()
    {
        foreach(string line in File.ReadAllLines(FileName))
        {
            Commands.Add(new Command(line));
        }
    }
}

enum CommandType { turnOn, turnOff, toggle }

class Command
{
    public CommandType Cmd { get; init; }

    public (int row, int col) Start { get; init; }

    public (int row, int col) End { get; init; }

    public string Line { get; init; }

    public Command(string Line)
    {
        this.Line = Line;
        string[] cmdStartEnd    = Line.Split(" through ");
        string[] cmdStart       = cmdStartEnd[0].Split(" ");
        CommandType cmd         = default;
        if("toggle" == cmdStart[0])
        {
            cmd = CommandType.toggle;
        }
        else
        {
            if("on" == cmdStart[1])
            {
                cmd = CommandType.turnOn;
            }
            else
            {
                cmd = CommandType.turnOff;
            }
        }
        string[] start  = cmdStart[cmdStart.Length-1].Split(",");
        string[] end    = cmdStartEnd[1].Split(",");

        this.Cmd   =  cmd;
        this.Start = (int.Parse(start[0]), int.Parse(start[1]));
        this.End   = (int.Parse(end[0]),   int.Parse(end[1]));
    }

    public override string ToString()
    {
        return this.Line;
    }
}

