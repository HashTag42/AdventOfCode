using System;
using System.Collections.Generic;   // List class.
using System.IO;                    // File class.

class CaveMap
{
    public List<Cave> CaveList { get; init; }

    public List<CavePath> PathList { get; private set; }

    public CaveMap()
    {
        this.CaveList = new List<Cave>();
        this.PathList = new List<CavePath>();
    }

    public CaveMap(string FilePath) : this()
    {
        LoadCaves(FilePath);
        BuildPaths();
    }

    private void BuildPaths()
    {
        CavePath cavePath = new CavePath();
        // cavePath.Path.Push(this.CaveList.Find(x => x.Name == "start"));
        foreach(Cave cave in CaveList)
        {
            cavePath.Push(cave);
        }
        this.PathList.Add(cavePath);
    }

    private bool IsCavePathValid(CavePath Path)
    {
        bool result = false;

        // Verify the first cave is 'start'

        // Verify all small caves in the map are visited at least once

        // Verify the last cave is 'end'

        return result;
    }

    private void LoadCaves(string FilePath)
    {
        string[] lines= File.ReadAllLines(FilePath);

        foreach(string line in lines)
        {
            string[] parts= line.Split('-');
            foreach(string part in parts)
            {
                Cave cave= new Cave(part);
                if(!this.CaveList.Contains(cave))
                {
                    this.CaveList.Add(cave);
                }
            }
        }

    }

    public override string ToString()
    {
        string output = null;

        output += "Caves:\n";
        foreach(Cave cave in this.CaveList)
        {
            output += "\t" + cave + "\n";
        }
        output += "\n";

        output += "Paths:\n";
        foreach(CavePath path in this.PathList)
        {
            output += "\t" + path + "\n";
        }

        return output;
    }

}