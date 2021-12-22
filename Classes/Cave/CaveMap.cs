using System.Collections.Generic;   // List class.
using System.IO;                    // File class.

class CaveMap
{
    public List<Cave> CaveList { get; init; }

    public CaveMap(string FilePath)
    {
        this.CaveList = new List<Cave>();
        LoadCaves(FilePath);
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

        foreach(Cave cave in this.CaveList)
        {
            output += cave + "\n";
        }

        return output;
    }

}