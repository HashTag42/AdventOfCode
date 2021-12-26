using System;                       // Required to use the Console class.
using System.Collections.Generic;   // Required to use the List class.
using System.Diagnostics;           // Required to use the Debug class.
using System.IO;                    // Required to use the File class.

/// This class represents a map of caves.
/// An object of this class contains a list of caves, and a list of paths to connect the caves.
class CaveMap
{
    /// This property will store all caves
    private List<CaveNode> CaveNodes { get; init; }

    /// This property will keep a list of all caves that have been visited.
    private List<CaveNode> Seen { get; set; }

    /// The default constructor initializes the object's properties.
    public CaveMap()
    {
        this.CaveNodes  = new List<CaveNode>();
        this.Seen = new List<CaveNode>();
    }

    /// This constructor intializes the map out of data read from a file.
    /// It relies on the default constructor to initialize the object's properties.
    public CaveMap(string FilePath) : this()
    {
        Console.WriteLine("Using: " + FilePath);
        LoadMapFromFile(FilePath);

        this.Seen = new List<CaveNode>();
        int answer1 = Count(1, this.Seen, this.CaveNodes.Find(n=> "start" == n.Name ));
        Console.WriteLine("Answer to part 1 = " + answer1);

        this.Seen = new List<CaveNode>();
        int answer2 = Count(2, this.Seen, this.CaveNodes.Find(n=> "start" == n.Name ));
        Console.WriteLine("Answer to part 2 = " + answer2);
    }

    /// This method searches for all valid paths in the map.
    /// This is the recursive method used to traverse the graph
    /// It relies on the IsCavePathValid method to determine if a path is valid or not.
    private int Count(int Part, List<CaveNode> Seen, CaveNode CurrentNode)
    {
        Debug.WriteLine("@" + CurrentNode.Name);
        if("end" == CurrentNode.Name)
        {
            return 1;
        }

        if(Seen.IndexOf(CurrentNode) >= 0)
        {
            if("start" == CurrentNode.Name)
            {
                return 0;
            }

            if(CaveSize.small == CurrentNode.Size)
            {
                if(1 == CurrentPart)
                {
                    return 0;
                }
                else
                {
                    Part = 1;
                }
            }
        }

        int sum = 0;
        foreach(CaveNode targetNode in CurrentNode.Links)
        {
            Seen.Add(CurrentNode);
            sum += Count(Part, Seen, targetNode);
        }

        return sum;
    }

    /// This method loads the map contents out of a file.
    private void LoadMapFromFile(string FilePath)
    {
        foreach(string line in File.ReadAllLines(FilePath))
        {
            string[] parts= line.Split('-');

            CaveNode nodeA = new CaveNode(parts[0]);
            CaveNode nodeB = new CaveNode(parts[1]);

            if(!this.CaveNodes.Contains(nodeA)) { this.CaveNodes.Add(nodeA); }
            if(!this.CaveNodes.Contains(nodeB)) { this.CaveNodes.Add(nodeB); }

            this.CaveNodes.Find(n=> n == nodeA).Add(nodeB);
            this.CaveNodes.Find(n=> n == nodeB).Add(nodeA);
        }
        Debug.WriteLine("Map: " + this);
    }

    /// This override method provides with a string representation of the object.
    public override string ToString()
    {
        string output = null;

        // Enumerate all cave nodes
        output += "Nodes:" + Environment.NewLine;
        foreach(CaveNode caveNode in this.CaveNodes)
        {
            output += "\t " + caveNode + Environment.NewLine;
        }

        return output;
    }

}