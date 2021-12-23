using System;                       // Required to use the Console class.
using System.Collections.Generic;   // Required to use the List class.
using System.Diagnostics;           // Required to use the Debug class.
using System.IO;                    // Required to use the File class.

/// This class represents a map of caves.
/// An object of this class contains a list of caves, and a list of paths to connect the caves.
class CaveMap
{
    /// This property stores all caves in the map.
    /// It is initialized at object construction time and cannot be modified.
    public List<Cave> Caves { get; init; }

    /// This property stores all cave links in the maps.
    /// It is initialized at object construction time and cannot be modified.
    public List<CaveLink> CaveLinks { get; init; }

    /// This property stores a list of paths of caves in the map.
    public List<CavePath> CavesPaths { get; private set; }

    /// This default constructor initializes the object's properties.
    public CaveMap()
    {
        this.Caves = new List<Cave>();
        this.CaveLinks = new List<CaveLink>();
        this.CavesPaths = new List<CavePath>();
    }

    /// This constructor intializes the map out of data read from a file.
    /// It relies on the default constructor to initialize the object's properties.
    public CaveMap(string FilePath) : this()
    {
        LoadMapFromFile(FilePath);
        BuildPaths();
    }

    /// This method builds all valid paths in the map.
    /// It relies on the IsCavePathValid method to determine if a path is valid or not.
    private void BuildPaths()
    {
        {   // Add all caves. Valid.
            CavePath cavePath = new CavePath();
            foreach(Cave cave in Caves) { cavePath.Push(cave); }
            if(IsCavePathValid(cavePath)) { this.CavesPaths.Add(cavePath); }
        }

        {   // A start and an end. Valid.
            CavePath cavePath = new CavePath();
            cavePath.Push(new Cave("start"));
            cavePath.Push(new Cave("end"));
            if(IsCavePathValid(cavePath)) { this.CavesPaths.Add(cavePath); }
        }

        {   // Invalid: missing the 'start' cave at the start of the path.
            CavePath cavePath = new CavePath();
            cavePath.Push(new Cave("end"));
            if(IsCavePathValid(cavePath)) { this.CavesPaths.Add(cavePath); }
        }

        {   // Invalid: missing the 'end' cave at the end of the path.
            CavePath cavePath = new CavePath();
            cavePath.Push(new Cave("start"));
            if(IsCavePathValid(cavePath)) { this.CavesPaths.Add(cavePath); }
        }

        {   // Invalid: 'a' is a small cave visited than once.
            CavePath cavePath = new CavePath();
            cavePath.Push(new Cave("start"));
            cavePath.Push(new Cave("a"));
            cavePath.Push(new Cave("b"));
            cavePath.Push(new Cave("a"));
            cavePath.Push(new Cave("end"));
            if(IsCavePathValid(cavePath)) { this.CavesPaths.Add(cavePath); }
        }

        do
        {
            CavePath cavePath = new CavePath();
            cavePath.Push(this.Caves.Find(x => x.Name == "start"));




            cavePath.Push(this.Caves.Find(x => x.Name == "end"));
            if(IsCavePathValid(cavePath)) { this.CavesPaths.Add(cavePath); }

            break;

        } while(true);

    }

    /// This is a requ
    private void FindPath()
    {
        throw new NotImplementedException();
    }

    /// This method determines if a path is valid.
    /// A path is valid when it starts at 'start', ends at 'end', and doesn't visit small caves more than once.
    private bool IsCavePathValid(CavePath Path)
    {
        bool result = false;

        if( // The first cave is 'start'
            Path.Caves[0].Name == "start"
            // The last cave is 'end'
         && Path.Caves[Path.Caves.Count -1].Name == "end"
        )
        {
            // Any visited small cave is not visited more than once
            List<Cave> visitedCaves = new List<Cave>();
            foreach(Cave cave in Path.Caves.FindAll(c => c.Size == CaveSize.Small))
            {
                if(visitedCaves.Contains(cave))
                {
                    result = false;
                    break;
                }
                else{
                    visitedCaves.Add(cave);
                    result = true;
                }
            }
        }

        return result;
    }

    /// This method loads the map contents out of a file.
    private void LoadMapFromFile(string FilePath)
    {
        string[] lines= File.ReadAllLines(FilePath);

        foreach(string line in lines)
        {
            string[] parts= line.Split('-');
            CaveLinks.Add(new CaveLink(new Cave(parts[0]), new Cave(parts[1])));
            foreach(string part in parts)
            {
                Cave cave= new Cave(part);
                // A cave is only added once to a map
                if(!this.Caves.Contains(cave))
                {
                    this.Caves.Add(cave);
                }
            }
        }
        Debug.WriteLine(this);
    }

    /// This override method provides with a string representation of the object.
    public override string ToString()
    {
        string output = null;

        // Enumerate the list of caves
        output += "Caves:\n";
        foreach(Cave cave in this.Caves)
        {
            output += "\t" + cave + "\n";
        }
        output += "\n";

        // Enumerate the list of links
        output += "Links:\n";
        foreach(CaveLink caveLink in this.CaveLinks)
        {
            output += "\t" + caveLink + "\n";
        }
        output += Environment.NewLine;

        // Enumerate the list of paths
        output += "Paths:\n";
        foreach(CavePath cavePath in this.CavesPaths)
        {
            output += "\t" + cavePath + "\n";
        }

        return output;
    }

}